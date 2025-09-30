# @File    :   instruction2code.py
# @Time    :   2024/01/04
# @Author  :   Your Name
# @Version :   1.0
# @Desc    :   将CAD instruction转换为CADQuery代码

from DeepCADProcess.cadlib.instruction_base import *
import os
import sys
import importlib.util
import argparse

def load_instructions(file_path):
    """
    从指定路径加载instruction对象
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"找不到文件: {file_path}")
    
    # 获取文件所在目录
    dir_path = os.path.dirname(file_path)
    # 将目录添加到Python路径中
    if dir_path not in sys.path:
        sys.path.append(dir_path)
    
    # 获取文件名（不含扩展名）
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    
    try:
        # 使用 importlib 动态加载模块
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # 获取模块中的所有变量
        all_vars = vars(module)
        # 筛选出所有Extrude对象
        extrude_objects = [var for var in all_vars.values() if isinstance(var, Extrude)]
        return extrude_objects
        
    except Exception as e:
        raise ImportError(f"导入模块失败: {str(e)}")


def convert_to_cadquery(extrude_list, if_visualize=True):
    """
    将Extrude对象列表转换为CadQuery代码
    Args:
        extrude_list: List[Extrude] Extrude对象列表
    Returns:
        str: CadQuery代码字符串
    """
    # 初始化代码
    code_lines = [
        "import cadquery as cq",
        "from cadquery.selectors import DirectionSelector, NearestToPointSelector",
        ""
    ]
    
    # 操作类型映射
    operation_map = {
        "newbody": "union",
        "join": "union",
        "cut": "cut",
        "intersect": "intersect"
    }
    
    result_initialized = False
    
    for idx, extrude in enumerate(extrude_list, 1):
        sketch = extrude.sketch
        
        # 处理每个profile
        profile_names = []
        for profile_idx, profile in enumerate(sketch.profiles, 1):
            profile_name = f"profile_{profile_idx}"
            profile_names.append(profile_name)
            
            code_lines.extend([
                f"{profile_name} = (",
                "    cq.Sketch()"
            ])
            
            # 处理profile中的每个loop
            for loop_idx, loop in enumerate(profile.loops, 1):
                code_lines.append(f"    # loop_{profile_idx}_{loop_idx}")
                first_curve = True
                
                for element in loop.curves:
                    if isinstance(element, Line):
                        if first_curve:
                            code_lines.append(f"    .segment({tuple(element.start_point)}, {tuple(element.end_point)}, '{element.name}')")
                            first_curve = False
                        else:
                            code_lines.append(f"    .segment({tuple(element.end_point)}, '{element.name}')")
                            
                    elif isinstance(element, Arc):
                        if first_curve:
                            code_lines.append(
                                f"    .arc({tuple(element.start_point)}, {tuple(element.mid_point)}, {tuple(element.end_point)}, '{element.name}')"
                            )
                            first_curve = False
                        else:
                            code_lines.append(
                                f"    .arc({tuple(element.mid_point)}, {tuple(element.end_point)}, '{element.name}')"
                            )
                            
                    elif isinstance(element, Circle):
                        code_lines.append(
                            f"    .arc({tuple(element.center_point)}, {element.radius}, 0.0, 360.0, '{element.name}')"
                        )
            
            code_lines.extend([
                "    .assemble()",
                ")",
                ""
            ])
        
        # 组合所有的profile生成最终的sketch
        code_lines.append(f"sketch_{idx} = {profile_names[0]}")
        for profile_name in profile_names[1:]:
            code_lines.append(f"sketch_{idx} = sketch_{idx}.face({profile_name}, mode='a')")
        code_lines.append("")
        
        # 处理工作平面
        workplane = extrude.workplane
        if isinstance(workplane, WorkplanePre):
            workplane_code = f"cq.Workplane('{workplane.plane_name}')"
        elif isinstance(workplane, WorkplaneRef):
            if workplane.reference_line:
                ref_point = [(p1 + p2) / 2 for p1, p2 in zip(
                    workplane.reference_line[0],  # 第一个点
                    workplane.reference_line[1]   # 第二个点
                )]
                workplane_code = (
                    f"cq.Workplane().copyWorkplane({workplane.reference_part}.faces("
                    f"DirectionSelector(cq.Vector{tuple(workplane.z_axis)}) and "
                    f"NearestToPointSelector({tuple(ref_point)})).workplane())"
                )
            else:
                workplane_code = (
                    f"cq.Workplane().copyWorkplane({workplane.reference_part}.faces("
                    f"DirectionSelector(cq.Vector{tuple(workplane.z_axis)})).workplane())"
                )
        else:
            workplane_code = (
                f"cq.Workplane().transformed("
                f"offset=cq.Vector{tuple(workplane.origin)}, "
                f"rotate=cq.Vector{tuple(workplane.ratate)})"
            )
        
        # 生成extrude代码
        extrude_code_extra = False
        if extrude.distance_1 == 0:
            code_lines.append(
                f"extrude_{idx} = {workplane_code}.placeSketch(sketch_{idx})"
                f".extrude(-{extrude.distance_2}, both={extrude.symmetric})"
            )
        else:
            code_lines.append(
                f"extrude_{idx} = {workplane_code}.placeSketch(sketch_{idx})"
                f".extrude({extrude.distance_1}, both={extrude.symmetric})"
            )
            if extrude.symmetric == False and extrude.distance_2 != 0:
                code_lines.append(
                    f"extrude_{idx}_extra = {workplane_code}.placeSketch(sketch_{idx})"
                    f".extrude(-{extrude.distance_2}, both=False)"
                )
                extrude_code_extra = True

        # 获取操作类型
        operation = operation_map.get(extrude.operate)

        if not result_initialized:
            code_lines.append(f"result = extrude_{idx}")
            result_initialized = True
        else:
            code_lines.append(f"result = result.{operation}(extrude_{idx})")

        if extrude_code_extra:
            code_lines.append(f"result = result.{operation}(extrude_{idx}_extra)")

    
    # 添加显示代码
    if if_visualize:
        code_lines.append("show_object(result)")
    
    return "\n".join(code_lines)
    
    
def instruction2code(instruction_path, filename="code.py"):
    try:
        extrude_list = load_instructions(instruction_path)
        code_lines = convert_to_cadquery(extrude_list)
        # 保存到文件
        saved_path = os.path.join(os.path.dirname(instruction_path), filename)  
        with open(saved_path, "w") as file:
            file.write(code_lines)
        print(f"转换成功，已保存到 {saved_path}")
    except Exception as e:
        print(f"转换失败: {str(e)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, default="DeepCADProcess/dataset/cad_sequence", help="json folder")
    args = parser.parse_args()

    # 获取所有json文件的路径
    json_files = []
    for folder_name in os.listdir(args.src):
        folder_path = os.path.join(args.src, folder_name)
        if os.path.isdir(folder_path):
            for subfolder_name in os.listdir(folder_path):
                subfolder_path = os.path.join(folder_path, subfolder_name)
                if os.path.isdir(subfolder_path):
                    json_file_path = os.path.join(subfolder_path, "instruction.py")
                    if os.path.exists(json_file_path):
                        instruction2code(json_file_path)