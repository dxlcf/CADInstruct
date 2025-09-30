# @File    :   metadata2instruction.py
# @Time    :   2024/12/27 13:40:20
# @Author  :   Chaofan Lv 
# @Version :   1.0
# @Desc    :   将json文件中的metadata转换为CAD instruction

import json
import os
import glob
import argparse
from multiprocessing import Process, cpu_count
from multiprocessing import Manager

def json_to_cad_instructions(json_path, filename="instruction.py"):
    instructions = []
    instructions.append("from DeepCADProcess.cadlib.instruction_base import * \n")
    sketch_count = 1
    profile_count = 1
    extrude_count = 1
    json_data = json.load(open(json_path, "r"))
    
    for key, value in json_data.items():
        if key.startswith("sketch"):
            sketch_var = f"sketch_{sketch_count}"
            instructions.append(f"# part_{sketch_count}")
            sketch_count += 1
            instructions.append(f"{sketch_var} = Sketch()")
            
            # 获取offset_2d
            reference_plane = value.get("reference_plane", {})
            if reference_plane == "Unknown":
                offset_2d = [0, 0]
            else:
                offset_2d = reference_plane.get("offset_2d", [0, 0])
                
            profiles = []
            # 每个sequence创建一个Profile
            for sequence in value.get("sequences", []):
                profile_loops = []
                for loop in sequence.get("loops", []):
                    profile_dict = {}
                    first_curve = True
                    for curve in loop.get("curves", []):
                        curve_type = curve.get("type", "")
                        curve_name = curve.get("name", "")
                        if curve_type == "Line":
                            # 添加offset_2d到2D坐标
                            if first_curve:
                                start_point = tuple(curve['start_point'][i] + offset_2d[i] for i in range(2))    
                                end_point = tuple(curve['end_point'][i] + offset_2d[i] for i in range(2))
                                profile_dict[curve_name] = f"Line({start_point}, {end_point}, name=\"{curve_name}\")"
                                first_curve = False
                            else:
                                end_point = tuple(curve['end_point'][i] + offset_2d[i] for i in range(2))
                                profile_dict[curve_name] = f"Line({end_point}, name=\"{curve_name}\")"
                        elif curve_type == "Arc":
                            if first_curve:
                                start_point = tuple(curve['start_point'][i] + offset_2d[i] for i in range(2))
                                mid_point = tuple(curve['mid_point'][i] + offset_2d[i] for i in range(2))
                                end_point = tuple(curve['end_point'][i] + offset_2d[i] for i in range(2))
                                profile_dict[curve_name] = f"Arc({start_point}, {mid_point}, {end_point}, name=\"{curve_name}\")"
                                first_curve = False
                            else:
                                mid_point = tuple(curve['mid_point'][i] + offset_2d[i] for i in range(2))
                                end_point = tuple(curve['end_point'][i] + offset_2d[i] for i in range(2))
                                profile_dict[curve_name] = f"Arc({mid_point}, {end_point}, name=\"{curve_name}\")"
                        elif curve_type == "Circle":
                            center_point = tuple(curve['center_point'][i] + offset_2d[i] for i in range(2))
                            radius = curve.get("radius", 0.0)
                            profile_dict[curve_name] = f"Circle({center_point}, {radius}, name=\"{curve_name}\")"
                    profile_loops.append(profile_dict)
                
                # 为当前sequence创建Profile
                profile_var = f"profile_{profile_count}"
                instructions.append(f"{profile_var} = Profile([")
                
                # 添加该Profile的所有Loop
                for loop in profile_loops:
                    instructions.append(f"    Loop([")
                    for name, definition in loop.items():
                        instructions.append(f"        {definition},")
                    instructions.append("    ]),")
                
                instructions.append("])")
                profiles.append(profile_var)
                profile_count += 1
            
            # 将所有Profile添加到Sketch
            instructions.append(f"{sketch_var}.add_profile([{', '.join(profiles)}])")
            if "constraints" in value:
                instructions.append(f"{sketch_var}.add_constraint([")
                for constraint in value["constraints"]:
                    constraint_type = constraint.get("constraint_type")
                    related_entities = constraint.get("related_entity", [])
                    parameter = constraint.get("parameter")
                    if len(related_entities) == 1:
                        instructions.append(f"    Constraint(['{related_entities[0]}'], '{constraint_type}', {parameter}),")
                    else:
                        entities_str = "', '".join(related_entities)
                        instructions.append(f"    Constraint(['{entities_str}'], '{constraint_type}', {parameter}),")
                instructions.append("])")
            reference_plane = value.get("reference_plane", {})
            if reference_plane == "Unknown":
                origin = value.get("transform", {}).get("origin", [0, 0, 0])
                rotate = value.get("transform", {}).get("rotate", [0, 0, 0])
                instructions.append(f"workplane_{extrude_count} = Workplane({tuple(origin)}, {tuple(rotate)})")
            
            elif "base_plane" in reference_plane:
                pre_plane = reference_plane["base_plane"]
                instructions.append(f"workplane_{extrude_count} = WorkplanePre('{pre_plane}')")
            
            elif "reference_object" in reference_plane:
                ref_obj = reference_plane["reference_object"]
                z_axis = reference_plane.get("z_axis")
                ref_line = reference_plane.get("reference_line", None)
                
                if ref_line:
                    ref_line_str = f"[{tuple(ref_line[0])}, {tuple(ref_line[1])}]"
                else:
                    ref_line_str = "None"
                
                instructions.append(f"workplane_{extrude_count} = WorkplaneRef('{ref_obj}', {tuple(z_axis)}, {ref_line_str})")
        elif key.startswith("extrude"):
            operation = value.get("operation", 0)
            extent_one = value.get("extent_one", 0.0)
            extent_two = value.get("extent_two", 0.0)
            # 如果value.get("extent_type") 的值为1，则both_side = False
            extent_type = value.get("extent_type", 0)
            if extent_one == extent_two:
                symmetric = True
            else:
                symmetric = extent_type == 1
            operation_type = ["Newbody", "Join", "Cut", "Intersect"][operation]

            instructions.append(f"extrude_{extrude_count} = Extrude(workplane_{extrude_count}, sketch_{extrude_count}, '{operation_type.lower()}', {extent_one}, {extent_two}, {symmetric})")

            instructions.append("\n")
            extrude_count += 1
    
    output_dir = os.path.dirname(json_path)
    saved_path = os.path.join(output_dir, filename)
    with open(saved_path, "w") as file:
        for instruction in instructions:
            file.write(instruction + "\n")

def process_file(process_id, json_files, num_processes, error_files):
    for index in range(process_id, len(json_files), num_processes):
        json_file = json_files[index]
        try:
            json_to_cad_instructions(json_file)
            print(f"成功处理文件: {json_file}")
        except Exception as e:
            print(f"处理文件 {json_file} 时出错: {e}")
            error_files.append(json_file)

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
                    json_file_path = os.path.join(subfolder_path, "metatdata.json")
                    if os.path.exists(json_file_path):
                        json_files.append(json_file_path)

    # 创建进程池
    num_processes = int(cpu_count() / 2)
    processes = []
    manager = Manager()
    error_files = manager.list()  # 使用 Manager 来共享错误文件列表

    # 启动多个进程
    for i in range(num_processes):
        process = Process(target=process_file, args=(i, json_files, num_processes, error_files))
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()

    # 打印并保存出错的文件列表
    if error_files:
        print("以下文件处理时出错:")
        for error_file in error_files:
            print(error_file)
        
        with open("metadata2instruction_error_files.txt", "w") as f:
            for error_file in error_files:
                f.write(error_file + "\n")

    print('所有任务完成')
