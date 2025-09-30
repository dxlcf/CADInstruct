# @Time    : 2024/10/30 10:05
# @Author  : 吕超凡
# @File    : metadata_filter.py
# @Description : 将json转换为step格式，并渲染各个拉伸实体和草图的图片

import os
import json
import os.path
import matplotlib
from multiprocessing import Process, cpu_count, Manager
import glob

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from DeepCADProcess.cadlib.extrude import CADSequence
from DeepCADProcess.cadlib.macro import *
from DeepCADProcess.utils.render_util import render_construction_sequence, render_sketch
from OCC.Extend.DataExchange import write_step_file
import argparse

def json2images(json_path):
    with open(json_path, 'r') as fp:
        data = json.load(fp)

    saved_folder_path = json_path.replace('cad_json', 'cad_sequence').replace(".json", "")
    os.makedirs(saved_folder_path, exist_ok=True)
    print(saved_folder_path)

    # 渲染草图
    render_sketch(data, saved_folder_path)

    # 多个轮廓的拉伸会被分解，每个拉伸操作有一个或多个cad_seq
    cad_seq = CADSequence.from_dict(data)  
    # 渲染各阶段的实体图片
    body = render_construction_sequence(cad_seq.seq, saved_folder_path)
    # 保存最终的step文件
    save_path = os.path.join(saved_folder_path, "final_modal.step")
    write_step_file(body, save_path)

    # create_CAD_with_colors(cad_seq)

def process_json_files(process_id, json_files, num_processes):
    for index in range(process_id, len(json_files), num_processes):
        json_path = json_files[index]
        try:
            json2images(json_path)
        except Exception as e:
            print(f"处理文件 {json_path} 时出错: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, default="DeepCADProcess/dataset/cad_json", help="source folder")
    args = parser.parse_args()

    # 获取所有json文件的路径
    json_files = []
    for folder_name in os.listdir(args.src):
        folder_path = os.path.join(args.src, folder_name)
        if os.path.isdir(folder_path):
            json_files.extend(glob.glob(os.path.join(folder_path, "*.json")))

    num_processes = cpu_count()
    processes = []

    for i in range(num_processes):
        process = Process(target=process_json_files, args=(i, json_files, num_processes))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print('所有任务完成')



