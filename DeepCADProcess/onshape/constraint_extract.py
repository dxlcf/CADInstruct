"""
从onshape公开文档中提取约束信息
"""

import os.path
import argparse
import yaml
from onshape_client.client import Client
from onshape_client.onshape_url import OnshapeElement
from joblib import delayed, Parallel
import json
import numpy as np
from pathlib import Path
from functools import lru_cache
from multiprocessing import Pool

class OnshapeAPI:
    _instance = None
    
    @classmethod
    @lru_cache(None)
    def get_instance(cls):
        """获取 OnshapeAPI 单例"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.base = 'https://cad.onshape.com'
        self.access = 'xqaB9ssZ1laWJBjWrbmrOf6H'
        self.secret = 'nDPHEPQYKwL0muosoi4baQJoGKvHhXiFhBW2rRC02V98C0TW'
        self._init_client()

    def _init_client(self):
        """初始化 Onshape 客户端"""
        self.client = Client(configuration={
            "base_url": self.base,
            "access_key": self.access,
            "secret_key": self.secret
        })

    def getFeatureList(self, url: str):
        """获取特征列表"""
        fixed_url = '/api/partstudios/d/did/w/wid/e/eid/features'

        element = OnshapeElement(url)
        fixed_url = fixed_url.replace('did', element.did)
        fixed_url = fixed_url.replace('wid', element.wvmid)
        fixed_url = fixed_url.replace('eid', element.eid)

        method = 'GET'
        params = {}
        payload = {}
        headers = {
            'Accept': 'application/vnd.onshape.v1+json; charset=UTF-8;qs=0.1',
            'Content-Type': 'application/json'
        }

        response = self.client.api_client.request(
            method, 
            url=self.base + fixed_url, 
            query_params=params, 
            headers=headers,
            body=payload
        )
        return json.loads(response.data)


def process_one(data_id: str, link: str, save_dir: str):
    """处理单个文件"""
    # 使用单例获取 API 实例
    onshapeAPI = OnshapeAPI.get_instance()
    
    save_path = os.path.join(save_dir, data_id + ".json")
    
    if os.path.exists(save_path):
        print(f"跳过 {data_id}: 文件已存在")
        return 0
    
    try:
        response = onshapeAPI.getFeatureList(link)
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(response, f, ensure_ascii=False, indent=4)
        print(f"成功处理 {data_id}")
        return 1
    except Exception as e:
        print(f"处理 {data_id} 时发生错误: {str(e)}")
        return 0




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", default=False, help="test with some examples")
    parser.add_argument("--deepcad_data_folder", default="DeepCADProcess/dataset/cad_json", help="data folder of Deepcad dataset")
    parser.add_argument("--saved_folder", default="DeepCADProcess/dataset/cad_feature", help="data folder of Deepcad dataset")
    parser.add_argument("--link_data_folder", default="DeepCADProcess/dataset/abc_objects", type=str, help="data folder of onshape links from ABC dataset")
    args = parser.parse_args()

    if args.test:
        data_id = '00000076'
        link = 'https://cad.onshape.com/documents/767e4372b5f94a88a7a17d90/w/194c02e4f65d47dabd006030/e/652c71b2f1d742fb9f342027'
        save_dir = "examples"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        count = process_one(data_id, link, save_dir)
    else:
        DWE_DIR = args.link_data_folder
        DATA_ROOT = os.path.dirname(DWE_DIR)
        filenames = sorted(os.listdir(DWE_DIR))
        for name in filenames:
            truck_id = name.split('.')[0].split('_')[-1]
            # 跳过 0073 及之前的文件夹
            if int(truck_id) < 97:
                print(f"跳过 {truck_id}: 已处理")
                continue
            print("Processing truck: {}".format(truck_id))

            # 1. 首先读取cad_json/{truck_id}目录下的文件名
            cad_json_dir = os.path.join(args.deepcad_data_folder, truck_id)
            if not os.path.exists(cad_json_dir):
                print(f"Skip {truck_id}: no corresponding cad_json directory")
                continue
            existing_files = os.listdir(cad_json_dir)
            existing_keys = sorted(set(os.path.splitext(f)[0] for f in existing_files))

            # 2. 创建保存目录
            save_dir = os.path.join(args.saved_folder, truck_id)
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            # 3. 读取并过滤yml数据
            dwe_path = os.path.join(DWE_DIR, name)
            with open(dwe_path, 'r') as fp:
                dwe_data = yaml.safe_load(fp)
            
            # 只保留cad_json目录中存在的文件对应的键值对
            filtered_dwe_data = {
                k: v for k, v in dwe_data.items() 
                if k in existing_keys
            }

            total_n = len(filtered_dwe_data)

            # 替换 joblib 并行处理为进程池
            with Pool(processes=4) as pool:
                tasks = [(data_id, link, save_dir) 
                        for data_id, link in filtered_dwe_data.items()]
                count = pool.starmap(process_one, tasks)
            
            count = np.array(count)
            print("valid: {}\ntotal:{}".format(np.sum(count > 0), total_n))
            print("distribution:")
            for n in np.unique(count):
                print(n, np.sum(count == n))
