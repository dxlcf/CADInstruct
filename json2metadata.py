# @File    :   json2metadata.py
# @Time    :   2024/12/27 11:58:25
# @Author  :   Chaofan Lv 
# @Version :   1.0
# @Desc    :   提取cad_json中的草图拉伸信息，以及cad_features中的约束信息，并生成metadata.json

import os
import sys
import json
import glob
import os.path
import matplotlib
import argparse
from multiprocessing import Process, cpu_count
import logging
from datetime import datetime

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import gc
import sketchgraphs.data as datalib

from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse, BRepAlgoAPI_Common
from DeepCADProcess.cadlib.extrude import CADSequence, CoordSystem
from DeepCADProcess.cadlib.curves import Line, Arc, Circle
from DeepCADProcess.cadlib.macro import *
from DeepCADProcess.cadlib.sketch import Profile
from DeepCADProcess.cadlib.math_utils import *
from sketchgraphs.data.sketch import Sketch
from sketchgraphs.data._entity import EntityType
from sketchgraphs.data._constraint import (
    ConstraintType,
    LocalReferenceParameter,
    ExternalReferenceParameter,
    QuantityParameter,
    ConstraintParameterType
)
from sketchgraphs.data import sequence
from sketchgraphs.pipeline.numerical_parameters import normalize_expression


CONSTRAINT_TYPE = {
    ConstraintType.Coincident,
    ConstraintType.Distance,
    ConstraintType.Horizontal,
    ConstraintType.Parallel,
    ConstraintType.Vertical,
    ConstraintType.Tangent,
    ConstraintType.Length,
    ConstraintType.Perpendicular,
    ConstraintType.Equal,
    ConstraintType.Diameter,
    ConstraintType.Radius,
    ConstraintType.Concentric,
    ConstraintType.Fix,
    ConstraintType.Angle
}

def determine_base_plane(x_axis, y_axis, z_axis, origin):
    """
    判断给定的x_axis, y_axis, z_axis是否属于某个基准平面，并检查origin是否在该平面内。
    返回:str: 基准平面名称（如"XY", "YZ", "XZ"等）或"None"如果不属于任何基准平面或origin不在平面内
    """
    # 定义一个小的阈值来判断向量是否相等
    threshold = 1e-3

    # 遍历BASE_PlANE中的每个基准平面
    for plane_name, axes in BASE_PlANE.items():
        base_x, base_y, base_z = axes
        if (all(abs(x - bx) < threshold for x, bx in zip(x_axis, base_x)) and
            all(abs(y - by) < threshold for y, by in zip(y_axis, base_y)) and
            all(abs(z - bz) < threshold for z, bz in zip(z_axis, base_z))):
            
            # 检查origin是否在平面内
            if abs(np.dot(z_axis, origin)) < threshold:
                return plane_name

    # 如果不属于任何基准平面或origin不在平面内
    return "None"


def determine_reference_plane(x_axis, y_axis, z_axis, origin, result):
    """
    确定特征的参考平面。
    
    参数:
        x_axis, y_axis, z_axis: 当前特征的坐标轴
        result: 包含草图和拉伸信息的字典
    
    返回:
        dict: 包含参考平面名称、法向量和偏移量的字典
    """
    # 将输入参数转换为numpy数组
    x_axis_np = np.array(x_axis)
    y_axis_np = np.array(y_axis)
    z_axis_np = np.array(z_axis)
    origin_np = np.array(origin)

    plane_name = determine_base_plane(x_axis_np, y_axis_np, z_axis_np, origin_np)
    if plane_name != "None":    
        reference_plane = {
            "base_plane": plane_name,
            "offset": origin,
            "offset_2d": convert_offset_3d_to_2d(origin, x_axis_np, y_axis_np),
            "normalized_origin": [0, 0, 0]
        }
        return reference_plane

    for sketch_name, sketch_data in result.items():
        if not sketch_name.startswith("sketch_"):
            continue

        extrude_name = sketch_name.replace("sketch_", "extrude_")
        e1, e2 = result[extrude_name]["extent_one"], result[extrude_name]["extent_two"]
        extent_type = result[extrude_name]["extent_type"]

        transform = sketch_data["transform"]
        sketch_origin_np = np.array(transform["origin"])
        sketch_x_axis_np = np.array(transform["x_axis"])
        sketch_y_axis_np = np.array(transform["y_axis"])
        sketch_z_axis_np = np.array(transform["z_axis"])
        sketch_reference_plane = sketch_data["reference_plane"]

        # 判断法向量是否与草图的法向量平行
        if are_vectors_parallel(z_axis_np, sketch_z_axis_np):
            # 计算平面间的距离
            distance = calculate_point_2_plane_distance(origin_np, sketch_origin_np, sketch_z_axis_np)
            if distance == 0:
                offset = (origin_np - sketch_origin_np).tolist()    
                reference_plane = {
                    "reference_object": sketch_reference_plane["reference_object"],
                    "z_axis": z_axis,
                    "offset_2d": convert_offset_3d_to_2d(offset, x_axis_np, y_axis_np),
                    "normalized_origin": sketch_reference_plane["normalized_origin"],
                }
                return reference_plane
            elif distance in [e1, e2]:
                # 计算投影点
                projection_point = calculate_projection_point(sketch_reference_plane["normalized_origin"], origin_np, z_axis_np)
                # 计算偏移量，相对于全局坐标系
                offset = (origin_np - projection_point).tolist()
                offset_2d = convert_offset_3d_to_2d(offset, x_axis_np, y_axis_np)
                # TODO 待验证：将这个偏移转换相对于二维草图上x方向和y方向的偏移量
                reference_plane = {
                    "reference_object": extrude_name,
                    "z_axis": z_axis,
                    "offset_2d": offset_2d,
                    "normalized_origin": projection_point.tolist()
                }
                return reference_plane

        # 判断法向量是否与草图的法向量垂直
        elif are_vectors_orthogonal(z_axis_np, sketch_z_axis_np):
            for loop in sketch_data["sequences"]:
                for curve in loop["loops"]:
                    for line in curve["curves"]:
                        if line["type"] == "Line":
                            point1 = convert_2d_to_3d(np.array(line["start_point"]), sketch_origin_np, sketch_x_axis_np, sketch_y_axis_np)
                            point2 = convert_2d_to_3d(np.array(line["end_point"]), sketch_origin_np, sketch_x_axis_np, sketch_y_axis_np)
                            
                            # 计算拉伸后的四个顶点
                            vertices = []
                            vertices.append(point1 + sketch_z_axis_np * e1)
                            vertices.append(point2 + sketch_z_axis_np * e1)
                            # 判断是否为双向拉伸
                            if extent_type == 1:
                                vertices.append(point1 - sketch_z_axis_np * e2)
                                vertices.append(point2 - sketch_z_axis_np * e2)
                            else:
                                vertices.append(point1)
                                vertices.append(point2) 

                            if is_point_in_rectangle(origin_np, vertices):
                                projection_point = calculate_projection_point(sketch_reference_plane["normalized_origin"], origin_np, z_axis_np)
                                offset = (origin_np - projection_point).tolist()
                                offset_2d = convert_offset_3d_to_2d(offset, x_axis_np, y_axis_np)
                                reference_plane = { 
                                    "reference_object": extrude_name,
                                    "reference_line": [point1.tolist(), point2.tolist()],
                                    "z_axis": z_axis,
                                    "offset_2d": offset_2d,
                                    "normalized_origin": projection_point.tolist(),
                                }
                                return reference_plane


    return "Unknown"


def get_constraint_parameters(constraint):
    value = None

    for param in constraint.parameters:
        if param.type == ConstraintParameterType.Quantity:
            if param.parameterId == "angle":
                value = param.expression
                value = normalize_expression(value, "angle")
                value = float(value.split()[0])
            elif param.parameterId == "length":
                value = param.expression
                value = normalize_expression(value, "length")
                value = round(float(value.split()[0]) * 1000, 3)
        # elif param.type in (ConstraintParameterType.Enum, ConstraintParameterType.Boolean):
        #     parameters[param_id] = param.value

    return value


def check_origin_constraint(constraint_type, parameter, entity, suffix):
    """检查图元与原点之间的约束关系是否满足
    
    参数:
        constraint_type: 约束类型
        parameter: 约束参数值
        entity: 图元数据
        suffix: 后缀, 用于匹配图元的start, end, center等
    返回:
        bool: 约束关系是否满足
    """
    origin = [0, 0]  # 原点坐标，二维平面上的点
    
    if constraint_type == "Distance":
        if suffix == "start":
            distance = point_to_point_distance(origin, entity["start_point"])
        elif suffix == "end":
            distance = point_to_point_distance(origin, entity["end_point"])
        elif suffix == "center":
            distance = point_to_point_distance(origin, entity["center_point"])
        else:
            if entity["entity_type"] == "Line":
                distance = point_to_line_distance(origin, entity["start_point"], entity["end_point"])
            else:
                distance = point_to_point_distance(origin, entity["center_point"])
        return abs(distance - parameter) < 1e-3
                   
    elif constraint_type == "Coincident":
        if suffix == "start":
            return all(abs(x) < 1e-3 for x in entity["start_point"])
        elif suffix == "end":
            return all(abs(x) < 1e-3 for x in entity["end_point"])
        elif suffix == "center":
            return all(abs(x) < 1e-3 for x in entity["center_point"])
        else:
            if entity["entity_type"] == "Line": 
                return any(all(abs(x) < 1e-3 for x in point) 
                          for point in [entity["start_point"], entity["end_point"]])
            elif entity["entity_type"] == "Circle" or entity["entity_type"] == "Arc":
                return all(abs(x) < 1e-3 for x in entity["center_point"])
            
    elif constraint_type == "Horizontal":
        # 检查是否水平（y坐标相等）
        if entity["entity_type"] == "Line":
            return abs(entity["start_point"][1]) < 1e-3 and abs(entity["end_point"][1]) < 1e-3
        elif entity["entity_type"] == "Circle" or entity["entity_type"] == "Arc":
            return abs(entity["center_point"][1]) < 1e-3
            
    elif constraint_type == "Vertical":
        # 检查是否垂直（x坐标相等）
        if entity["entity_type"] == "Line":
            return abs(entity["start_point"][0]) < 1e-3 and abs(entity["end_point"][0]) < 1e-3
        elif entity["entity_type"] == "Circle" or entity["entity_type"] == "Arc":
            return abs(entity["center_point"][0]) < 1e-3
    
    return False


def _normalize_constraint_parameters(seq):
    """标准化约束参数

    参数:
        seq: 要标准化的序列
    """
    for op in seq:
        if not isinstance(op, sequence.EdgeOp):
            continue

        for param in ('angle', 'length'):
            if param not in op.parameters:
                continue
            value = op.parameters[param]
            op.parameters[param] = normalize_expression(value, param) or value


def round_coordinates(coords):
    return [round(coord * 1000, 3) for coord in coords]


def get_sketch_data(profile, profile_count):
    profile_data = []

    for loop_index, loop in enumerate(profile.children):
        loop_data = {
            "loop_name": f"loop_{profile_count}_{loop_index+1}",
            "curves": []
        }

        for curve_index, curve in enumerate(loop.children):
            curve_data = {}
            if isinstance(curve, Line):
                curve_data = {
                    "name": f"line_{profile_count}_{loop_index+1}_{curve_index+1}",
                    "type": "Line",
                    "start_point": round_coordinates(curve.start_point),
                    "end_point": round_coordinates(curve.end_point),
                }
            elif isinstance(curve, Circle):
                curve_data = {
                    "name": f"circle_{profile_count}_{loop_index+1}_{curve_index+1}",
                    "type": "Circle",
                    "center_point": round_coordinates(curve.center),
                    "radius": round(curve.radius * 1000, 3),
                }
            elif isinstance(curve, Arc):
                curve_data = {
                    "name": f"arc_{profile_count}_{loop_index+1}_{curve_index+1}",
                    "type": "Arc",
                    "start_point": round_coordinates(curve.start_point),
                    "mid_point": round_coordinates(curve.mid_point),
                    "end_point": round_coordinates(curve.end_point),
                    "center_point": round_coordinates(curve.center),
                    "radius": round(curve.radius * 1000, 3),
                }
            loop_data["curves"].append(curve_data)

        profile_data.append(loop_data)
    return profile_data


def get_constraint_data(json_path):
    with open(json_path, 'r') as fp:
        data = json.load(fp)

    sketch_data = []

    for item in data['features']:
        if item['message']['featureType'] not in ['newSketch', 'extrude']:
            return 0
        if item['message']['featureType'] == 'newSketch':
            sketches_json = item['message']
            sketch = Sketch.from_fs_json(sketches_json)
            datalib.render_sketch(sketch, show_axes=True, show_origin=True, show_points=True)
            # plt.savefig('sketch_output.png', dpi=300, bbox_inches='tight')
            # plt.close()

            entities = []
            constraints = []
            seq = sequence.sketch_to_sequence(sketch)
            _normalize_constraint_parameters(seq)

            for key, value in sketch.entities.items():
                if value.type == EntityType.Line:
                    line_data = {
                        "start_point": round_coordinates(value.start_point),
                        "end_point": round_coordinates(value.end_point),
                        "entity_id": key,
                        "entity_type": "Line"
                    }
                    entities.append(line_data)
                elif value.type == EntityType.Circle:
                    circle_data = {
                        "center_point": round_coordinates(value.center_point),
                        "radius": round(value.radius * 1000, 3),
                        "entity_id": key,
                        "entity_type": "Circle"
                    }
                    entities.append(circle_data)
                elif value.type == EntityType.Arc:
                    arc_data = {
                        "start_point": round_coordinates(value.start_point),
                        "mid_point": round_coordinates(value.mid_point),
                        "end_point": round_coordinates(value.end_point),
                        "center_point": round_coordinates(value.center_point),
                        "entity_id": key,
                        "entity_type": "Arc"
                    }
                    entities.append(arc_data)

            for key, constraint in sketch.constraints.items():
                if constraint.type in CONSTRAINT_TYPE:
                    # 获取约束的图元
                    reference_entity = []
                    value = None
                    for parameter in constraint.parameters:
                        if isinstance(parameter, LocalReferenceParameter):
                            reference_entity.append(parameter.value)
                        elif isinstance(parameter, ExternalReferenceParameter):
                            # FIXME: onshape暂不支持查询外部图元，跳过这个约束
                            # 外部约束先默认为草图原点，后续通过数值来确定
                            reference_entity.append("external")
                        elif isinstance(parameter, QuantityParameter):
                            if parameter.parameterId == "angle":
                                value = normalize_expression(parameter.expression, "angle")
                                value = float(value.split()[0])
                            elif parameter.parameterId == "length":
                                value = normalize_expression(parameter.expression, "length")
                                value = round(float(value.split()[0]) * 1000, 3)


                    constraint_data = {
                        "reference_entity": reference_entity,
                        "parameter": value,
                        "constraint_type": ConstraintType(constraint.type).name,
                    }
                    constraints.append(constraint_data)

            sketch_data.append({
                "sketch_id": sketches_json["featureId"],
                "entities": entities,
                "constraints": constraints
            })

    return sketch_data


def json2metadata(json_path, constraint_json_path, saved_path):
    with open(json_path, 'r') as fp:
        data = json.load(fp)

    result = {}
    sketch_count, extrude_count = 1, 1

    # 创建草图序号到result中草图名称的映射
    sketch_id_mapping = {}
    
    for item in data["sequence"]:
        if item["type"] != "ExtrudeFeature":
            continue

        extrude_entity = data["entities"][item["entity"]]
        assert extrude_entity["start_extent"]["type"] == "ProfilePlaneStartDefinition"

        profiles = extrude_entity["profiles"]
        sketch_id = profiles[0]["sketch"]
        if sketch_id not in sketch_id_mapping:
            sketch_id_mapping[sketch_id] = []
            
        # 提取草图参数
        sketch_id_mapping[sketch_id].append(f"sketch_{sketch_count}")
        transform = data["entities"][sketch_id]["transform"]
        origin = [round(coord * 1000, 3) for coord in [
            transform["origin"]["x"],
            transform["origin"]["y"],
            transform["origin"]["z"]
        ]]

        x_axis = [transform["x_axis"]["x"], transform["x_axis"]["y"], transform["x_axis"]["z"]]
        y_axis = [transform["y_axis"]["x"], transform["y_axis"]["y"], transform["y_axis"]["z"]]
        z_axis = [transform["z_axis"]["x"], transform["z_axis"]["y"], transform["z_axis"]["z"]]
        phi, theta, gamma = get_rotation_angles(x_axis, y_axis, z_axis)
        rotate = [phi, theta, gamma]

        # 添加草图信息
        sketch_name = f"sketch_{sketch_count}"
        result[sketch_name] = {
            "reference_plane": determine_reference_plane(x_axis, y_axis, z_axis, origin, result),
            "transform": {
                "origin": origin,
                "x_axis": x_axis,
                "y_axis": y_axis,
                "z_axis": z_axis,
                "rotate": rotate,   # 旋转角度，cadquery代码用
            },
            "sequences": {}
        }
        
        # 提取草图轮廓
        profile_count = 1
        sequences = []
        for profile in profiles:
            sketch_id, profile_id = profile["sketch"], profile["profile"]
            # 草图参数
            sketch_entity = data["entities"][sketch_id]
            sketch_profile = Profile.from_dict(sketch_entity["profiles"][profile_id])
            profile_data = {
                "profile_name": f"profile_{profile_count}",
                "loops": get_sketch_data(sketch_profile, profile_count)
            }
            sequences.append(profile_data)
            profile_count += 1

        result[sketch_name]["sequences"] = sequences    

        # 添加拉伸信息
        extrude_name = f"extrude_{extrude_count}"
        extent_two = 0.0
        if extrude_entity["extent_type"] == "TwoSidesFeatureExtentType":
            extent_two = extrude_entity["extent_two"]["distance"]["value"]
        result[extrude_name] = {
            "operation": EXTRUDE_OPERATIONS.index(extrude_entity["operation"]),
            "extent_type": EXTENT_TYPE.index(extrude_entity["extent_type"]),
            "extent_one": round(extrude_entity["extent_one"]["distance"]["value"] * 1000, 3),
            "extent_two": round(extent_two * 1000, 3)
        }

        sketch_count += 1
        extrude_count += 1

    
    try:
        # 约束信息提取
        sketch_data = get_constraint_data(constraint_json_path)
        sketch_constraint = []
        for index, sketch in enumerate(sketch_data, start=1):
            sketch_sequence = sketch["entities"]
            
            # 为sketch_id_mapping中的每个草图创建约束列表
            for sketch_name in sketch_id_mapping.get(sketch["sketch_id"], []):
                current_sketch_constraint = []
                
                for constraint in sketch["constraints"]:
                    related_entity = []
                    # 为每个草图的图元找到result中的对应图元
                    # TODO: 也需要匹配图元的start，end，center等
                    for parameter in constraint["reference_entity"]:
                        # 解析参数中的实体ID和后缀
                        suffix = parameter.split(".")[-1] if "." in parameter else None
                        if suffix not in ["start", "end", "center"]:
                            suffix = None
                        
                        for entity in sketch_sequence:
                            if entity["entity_id"] in parameter:
                                for profile in result[sketch_name]["sequences"]:
                                    for loop in profile["loops"]:
                                        for curve in loop["curves"]:
                                            # 检查类型是否匹配
                                            if entity["entity_type"] != curve["type"]:
                                                continue
                                                
                                            # 根据不同类型进行匹配判断
                                            entity_match = False
                                            is_reverse = False  # 是否为反向匹配，默认为False
                                            
                                            if curve["type"] == "Line":
                                                # 正向匹配
                                                if (entity["start_point"] == curve["start_point"] and 
                                                    entity["end_point"] == curve["end_point"]):
                                                    entity_match = True
                                                # 反向匹配
                                                elif (entity["start_point"] == curve["end_point"] and 
                                                      entity["end_point"] == curve["start_point"]):
                                                    entity_match = True
                                                    is_reverse = True
                                                    
                                            elif curve["type"] == "Circle":
                                                if (entity["center_point"] == curve["center_point"] and 
                                                    entity["radius"] == curve["radius"]):
                                                    entity_match = True
                                                    
                                            elif curve["type"] == "Arc":
                                                # 正向匹配
                                                if (entity["start_point"] == curve["start_point"] and 
                                                    entity["mid_point"] == curve["mid_point"] and 
                                                    entity["end_point"] == curve["end_point"]):
                                                    entity_match = True
                                                # 反向匹配
                                                elif (entity["start_point"] == curve["end_point"] and 
                                                      entity["mid_point"] == curve["mid_point"] and 
                                                      entity["end_point"] == curve["start_point"]):
                                                    entity_match = True
                                                    is_reverse = True

                                            if entity_match:
                                                if suffix:
                                                    if is_reverse:
                                                        if suffix == "start":
                                                            related_entity.append(f"{curve['name']}.end_point")
                                                        elif suffix == "end":
                                                            related_entity.append(f"{curve['name']}.start_point")
                                                        else:
                                                            related_entity.append(f"{curve['name']}.{suffix}_point")
                                                    else:
                                                        related_entity.append(f"{curve['name']}.{suffix}_point")
                                                else:
                                                    related_entity.append(curve["name"])

                    if not related_entity:
                        continue

                    if "external" in constraint["reference_entity"]:
                        # 获取非external的reference实体
                        ref = next(ref for ref in constraint["reference_entity"] if ref != "external")
                        for entity in sketch_sequence:
                            if entity["entity_id"] == ref:
                                suffix = None
                            elif entity["entity_id"] in ref:
                                suffix = ref.split(".")[-1] if "." in ref else None
                            else:
                                continue

                            if check_origin_constraint(constraint["constraint_type"], constraint["parameter"], entity, suffix):
                                related_entity.append("origin")
                                break

                    if len(related_entity) != len(constraint["reference_entity"]):
                        continue

                    current_sketch_constraint.append({
                        "related_entity": related_entity,
                        "parameter": constraint["parameter"],
                        "constraint_type": constraint["constraint_type"]
                    })
                
                # 将当前草图的约束添加到结果中
                sketch_constraint.append(current_sketch_constraint)

        # 将sketch_constraint加入到result中
        for index, constraints in enumerate(sketch_constraint, start=1):
            sketch_name = f"sketch_{index}"
            if sketch_name in result:
                result[sketch_name]["constraints"] = constraints

        print(os.path.join(saved_path, f'metatdata.json'))

        # 将结果写入到json文件中
        with open(os.path.join(saved_path, f'metatdata.json'), "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"处理约束信息时发生错误: {e}")

    gc.collect()


# 在 process_json_file 函数前添加日志配置函数
def setup_logger(saved_folder):
    """配置日志记录器"""
    # 创建logs文件夹
    log_dir = os.path.join(saved_folder, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # 创建日志文件名，包含时间戳
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(log_dir, f'error_log_{timestamp}.txt')
    
    # 配置日志记录器
    logger = logging.getLogger('error_logger')
    logger.setLevel(logging.ERROR)
    
    # 创建文件处理器
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.ERROR)
    
    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # 添加处理器到日志记录器
    logger.addHandler(file_handler)
    
    return logger


# 修改 process_json_file 函数
def process_json_file(args, process_id, json_files, num_processes):
    # 设置日志记录器
    logger = setup_logger(args.saved_folder)
    
    for index in range(process_id, len(json_files), num_processes):
        json_path = json_files[index]
        try:
            # 构建constraint_json_path
            folder_name = os.path.basename(os.path.dirname(json_path))
            file_name = os.path.basename(json_path)
            constraint_json_path = os.path.join(args.constraint_json_src, folder_name, file_name)
            
            # 构建saved_path
            saved_path = os.path.join(args.saved_folder, folder_name, os.path.splitext(file_name)[0])
            os.makedirs(saved_path, exist_ok=True)
            
            json2metadata(json_path, constraint_json_path, saved_path)
            print(f"处理文件 {json_path} 完成")
            
        except Exception as e:
            error_msg = f"处理文件 {json_path} 时出错: {str(e)}"
            print(error_msg)
            # 记录错误到日志文件
            logger.error(error_msg, exc_info=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--json_src', type=str, default="DeepCADProcess/dataset/cad_json", help="json folder")
    parser.add_argument('--constraint_json_src', type=str, default="DeepCADProcess/dataset/cad_feature", help="constraint json folder")
    parser.add_argument('--saved_folder', type=str, default="DeepCADProcess/dataset/cad_sequence", help="saved folder")
    args = parser.parse_args()

    # 获取所有json文件的路径
    json_files = []
    for folder_name in os.listdir(args.json_src):
        folder_path = os.path.join(args.json_src, folder_name)
        if os.path.isdir(folder_path):
            json_files.extend(glob.glob(os.path.join(folder_path, "*.json")))

    # 创建进程池
    num_processes = int(cpu_count() / 2) - 4
    processes = []


    # 启动多个进程
    for i in range(num_processes):
        process = Process(target=process_json_file, args=(args, i, json_files, num_processes))
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()

    print('所有任务完成')



    







