import numpy as np
import random
from .sketch import Profile
from .macro import *
from .math_utils import cartesian2polar, polar2cartesian, polar_parameterization, polar_parameterization_inverse, calculate_rotation_angles


class CoordSystem(object):
    """局部坐标系统,用于草图平面。"""

    def __init__(self, origin, theta, phi, gamma, x_degree, y_degree, z_degree, y_axis=None, is_numerical=False):
        self.origin = origin  # 原点
        self._theta = theta
        self._phi = phi
        self._gamma = gamma
        self.x_degree = x_degree
        self.y_degree = y_degree
        self.z_degree = z_degree
        self._y_axis = y_axis  # (theta, phi), y轴方向
        self.is_numerical = is_numerical  # 是否为数值表示

    @property
    def normal(self):
        """返回法线方向"""
        return polar2cartesian([self._theta, self._phi])

    @property
    def x_axis(self):
        """返回x轴方向"""
        normal_3d, x_axis_3d = polar_parameterization_inverse(self._theta, self._phi, self._gamma)
        return x_axis_3d

    @property
    def y_axis(self):
        """返回y轴方向"""
        if self._y_axis is None:
            return np.cross(self.normal, self.x_axis)
        return polar2cartesian(self._y_axis)

    @staticmethod
    def from_dict(stat):
        """从字典创建CoordSystem实例"""
        origin = np.array([stat["origin"]["x"], stat["origin"]["y"], stat["origin"]["z"]])
        normal_3d = np.array([stat["z_axis"]["x"], stat["z_axis"]["y"], stat["z_axis"]["z"]])
        x_axis_3d = np.array([stat["x_axis"]["x"], stat["x_axis"]["y"], stat["x_axis"]["z"]])
        y_axis_3d = np.array([stat["y_axis"]["x"], stat["y_axis"]["y"], stat["y_axis"]["z"]])
        theta, phi, gamma = polar_parameterization(normal_3d, x_axis_3d)
        x_degree, y_degree, z_degree = calculate_rotation_angles(x_axis_3d, y_axis_3d, normal_3d)
        return CoordSystem(origin, theta, phi, gamma, x_degree, y_degree, z_degree, y_axis=cartesian2polar(y_axis_3d))


    @staticmethod
    def from_vector(vec, is_numerical=False, n=256):
        """从向量创建CoordSystem实例"""
        origin = vec[:3]
        theta, phi, gamma = vec[3:]
        system = CoordSystem(origin, theta, phi, gamma)
        if is_numerical:
            system.denumericalize(n)
        return system

    def __str__(self):
        """返回坐标系统的字符串表示"""
        return "origin: {}, normal: {}, x_axis: {}, y_axis: {}".format(
            self.origin.round(4), self.normal.round(4), self.x_axis.round(4), self.y_axis.round(4))

    def transform(self, translation, scale):
        """对坐标系统进行平移和缩放变换"""
        self.origin = (self.origin + translation) * scale

    def numericalize(self, n=256):
        """NOTE: shall only be called after normalization"""
        # assert np.max(self.origin) <= 1.0 and np.min(self.origin) >= -1.0 # TODO: origin can be out-of-bound!
        """将坐标系统转换为数值表示"""
        self.origin = ((self.origin + 1.0) / 2 * n).round().clip(min=0, max=n - 1).astype(np.integer)
        tmp = np.array([self._theta, self._phi, self._gamma])
        self._theta, self._phi, self._gamma = ((tmp / np.pi + 1.0) / 2 * n).round().clip(
            min=0, max=n - 1).astype(np.integer)
        self.is_numerical = True

    def denumericalize(self, n=256):
        """将数值表示转换回原始坐标系统"""
        self.origin = self.origin / n * 2 - 1.0
        tmp = np.array([self._theta, self._phi, self._gamma])
        self._theta, self._phi, self._gamma = (tmp / n * 2 - 1.0) * np.pi
        self.is_numerical = False

    def to_vector(self):
        """将坐标系统转换为向量表示"""
        return np.array([*self.origin, self._theta, self._phi, self._gamma])


class Extrude(object):
    """单个拉伸操作及其对应的草图轮廓。
    注意：仅支持单个草图轮廓。多个轮廓的拉伸会被分解。"""
    # TODO,这里该怎么办

    def __init__(self, profile: Profile, sketch_plane: CoordSystem,
                 operation, extent_type, extent_one, extent_two, sketch_pos, sketch_size):
        """
        初始化Extrude对象
        Args:
            profile (Profile): 归一化的草图轮廓
            sketch_plane (CoordSystem): 草图平面的坐标系统
            operation (int): EXTRUDE_OPERATIONS中的索引，见macro.py
            extent_type (int): EXTENT_TYPE中的索引，见macro.py
            extent_one (float): 法线方向的拉伸距离（注意：在某些数据中可能为负）
            extent_two (float): 相反方向的拉伸距离
            sketch_pos (np.array): 草图起点的全局3D位置
            sketch_size (float): 草图的大小
        """
        self.profile = profile  # 归一化的草图
        self.sketch_plane = sketch_plane
        self.operation = operation
        self.extent_type = extent_type
        self.extent_one = extent_one
        self.extent_two = extent_two

        self.sketch_pos = sketch_pos
        self.sketch_size = sketch_size

    @staticmethod
    def from_dict(all_stat, extrude_id, sketch_dim=256):
        """从json数据构造Extrude对象

        Args:
            all_stat (dict): 所有json数据
            extrude_id (str): 此拉伸的实体ID
            sketch_dim (int, optional): 草图归一化尺寸。默认为256。

        Returns:
            list: 一个或多个Extrude实例
        """
        extrude_entity = all_stat["entities"][extrude_id]
        assert extrude_entity["start_extent"]["type"] == "ProfilePlaneStartDefinition"

        all_skets = []
        n = len(extrude_entity["profiles"])
        for i in range(len(extrude_entity["profiles"])):
            sket_id, profile_id = extrude_entity["profiles"][i]["sketch"], extrude_entity["profiles"][i]["profile"]
            sket_entity = all_stat["entities"][sket_id]
            sket_profile = Profile.from_dict(sket_entity["profiles"][profile_id])
            sket_plane = CoordSystem.from_dict(sket_entity["transform"])
            # 归一化轮廓
            point = sket_profile.start_point
            sket_pos = point[0] * sket_plane.x_axis + point[1] * sket_plane.y_axis + sket_plane.origin
            sket_size = sket_profile.bbox_size
            sket_profile.normalize(sketch_dim)
            # print("sket_profile:", str(sket_profile))
            all_skets.append((sket_profile, sket_plane, sket_pos, sket_size))

        operation = EXTRUDE_OPERATIONS.index(extrude_entity["operation"])
        extent_type = EXTENT_TYPE.index(extrude_entity["extent_type"])
        extent_one = extrude_entity["extent_one"]["distance"]["value"]
        extent_two = 0.0
        if extrude_entity["extent_type"] == "TwoSidesFeatureExtentType":
            extent_two = extrude_entity["extent_two"]["distance"]["value"]

        if operation == EXTRUDE_OPERATIONS.index("NewBodyFeatureOperation"):
            all_operations = [operation] + [EXTRUDE_OPERATIONS.index("JoinFeatureOperation")] * (n - 1)
        else:
            all_operations = [operation] * n

        return [Extrude(all_skets[i][0], all_skets[i][1], all_operations[i], extent_type, extent_one, extent_two,
                        all_skets[i][2], all_skets[i][3]) for i in range(n)]

    @staticmethod
    def from_vector(vec, is_numerical=False, n=256):
        """从向量表示构造Extrude对象"""
        assert vec[-1][0] == EXT_IDX and vec[0][0] == SOL_IDX
        profile_vec = np.concatenate([vec[:-1], EOS_VEC[np.newaxis]])
        profile = Profile.from_vector(profile_vec, is_numerical=is_numerical)
        ext_vec = vec[-1][-N_ARGS_EXT:]

        sket_pos = ext_vec[N_ARGS_PLANE:N_ARGS_PLANE + 3]
        sket_size = ext_vec[N_ARGS_PLANE + N_ARGS_TRANS - 1]
        sket_plane = CoordSystem.from_vector(np.concatenate([sket_pos, ext_vec[:N_ARGS_PLANE]]))
        ext_param = ext_vec[-N_ARGS_EXT_PARAM:]

        res = Extrude(profile, sket_plane, int(ext_param[2]), int(ext_param[3]), ext_param[0], ext_param[1],
                      sket_pos, sket_size)
        if is_numerical:
            res.denumericalize(n)
        return res

    def __str__(self):
        """返回Extrude对象的字符串表示"""
        s = "Sketch-Extrude pair:"
        s += "\n  -" + str(self.sketch_plane)
        s += "\n  -sketch position: {}, sketch size: {}".format(self.sketch_pos.round(4), self.sketch_size.round(4))
        s += "\n  -operation:{}, type:{}, extent_one:{}, extent_two:{}".format(
            self.operation, self.extent_type, round(self.extent_one, 4), round(self.extent_two, 4))
        s += "\n  -" + str(self.profile)
        return s

    def transform(self, translation, scale):
        """对Extrude对象进行线性变换"""
        self.sketch_plane.transform(translation, scale)
        self.extent_one *= scale
        self.extent_two *= scale
        self.sketch_pos = (self.sketch_pos + translation) * scale
        self.sketch_size *= scale

    def numericalize(self, n=256):
        """将Extrude对象转换为数值表示。
        注意：应在CADSequence.normalize之后调用（形状位于单位立方体内，-1~1）"""
        assert -2.0 <= self.extent_one <= 2.0 and -2.0 <= self.extent_two <= 2.0
        self.profile.numericalize(n)
        self.sketch_plane.numericalize(n)
        self.extent_one = ((self.extent_one + 1.0) / 2 * n).round().clip(min=0, max=n - 1).astype(np.integer)
        self.extent_two = ((self.extent_two + 1.0) / 2 * n).round().clip(min=0, max=n - 1).astype(np.integer)
        self.operation = int(self.operation)
        self.extent_type = int(self.extent_type)

        self.sketch_pos = ((self.sketch_pos + 1.0) / 2 * n).round().clip(min=0, max=n - 1).astype(np.integer)
        self.sketch_size = (self.sketch_size / 2 * n).round().clip(min=0, max=n - 1).astype(np.integer)

    def denumericalize(self, n=256):
        """将数值表示转换回原始Extrude对象"""
        self.extent_one = self.extent_one / n * 2 - 1.0
        self.extent_two = self.extent_two / n * 2 - 1.0
        self.sketch_plane.denumericalize(n)
        self.sketch_pos = self.sketch_pos / n * 2 - 1.0
        self.sketch_size = self.sketch_size / n * 2

        self.operation = self.operation
        self.extent_type = self.extent_type

    def flip_sketch(self, axis):
        """翻转草图"""
        self.profile.flip(axis)
        self.profile.normalize()

    def to_vector(self, max_n_loops=6, max_len_loop=15, pad=True):
        """将Extrude对象转换为向量表示"""
        profile_vec = self.profile.to_vector(max_n_loops, max_len_loop, pad=False)
        if profile_vec is None:
            return None
        sket_plane_orientation = self.sketch_plane.to_vector()[3:]
        ext_param = list(sket_plane_orientation) + list(self.sketch_pos) + [self.sketch_size] + \
                    [self.extent_one, self.extent_two, self.operation, self.extent_type]
        ext_vec = np.array([EXT_IDX, *[PAD_VAL] * N_ARGS_SKETCH, *ext_param])
        vec = np.concatenate([profile_vec[:-1], ext_vec[np.newaxis], profile_vec[-1:]], axis=0)  # NOTE: last one is EOS
        if pad:
            pad_len = max_n_loops * max_len_loop - vec.shape[0]
            vec = np.concatenate([vec, EOS_VEC[np.newaxis].repeat(pad_len, axis=0)], axis=0)
        return vec


class CADSequence(object):
    """CAD建模序列，由一系列拉伸操作组成。"""

    def __init__(self, extrude_seq, bbox=None):
        """
        初始化CADSequence对象
        
        参数:
        extrude_seq: 拉伸操作序列
        bbox: 边界框，默认为None
        """
        self.seq = extrude_seq
        self.bbox = bbox

    @staticmethod
    def from_dict(all_stat):
        """
        从json数据构造CADSequence对象
        
        参数:
        all_stat: 包含CAD序列信息的字典
        
        返回:
        CADSequence对象
        """
        seq = []
        for item in all_stat["sequence"]:
            if item["type"] == "ExtrudeFeature":
                extrude_ops = Extrude.from_dict(all_stat, item["entity"])
                # print("extrude_ops:", str(extrude_ops[0]))
                seq.append(extrude_ops)

        # 提取边界框信息
        bbox_info = all_stat["properties"]["bounding_box"]
        max_point = np.array([bbox_info["max_point"]["x"], bbox_info["max_point"]["y"], bbox_info["max_point"]["z"]])
        min_point = np.array([bbox_info["min_point"]["x"], bbox_info["min_point"]["y"], bbox_info["min_point"]["z"]])
        bbox = np.stack([max_point, min_point], axis=0)

        return CADSequence(seq, bbox)

    @staticmethod
    def from_vector(vec, is_numerical=False, n=256):
        """
        从向量表示构造CADSequence对象
        
        参数:
        vec: 向量表示
        is_numerical: 是否为数值表示，默认为False
        n: 数值化参数，默认为256
        
        返回:
        CADSequence对象
        """
        commands = vec[:, 0]
        ext_indices = [-1] + np.where(commands == EXT_IDX)[0].tolist()
        ext_seq = []
        for i in range(len(ext_indices) - 1):
            start, end = ext_indices[i], ext_indices[i + 1]
            ext_seq.append(Extrude.from_vector(vec[start + 1:end + 1], is_numerical, n))
        cad_seq = CADSequence(ext_seq)
        return cad_seq

    def __str__(self):
        """返回CADSequence对象的字符串表示"""
        return "" + "\n".join(["({})".format(i) + str(ext) for i, ext in enumerate(self.seq)])

    def to_vector(self, max_n_ext=10, max_n_loops=6, max_len_loop=15, max_total_len=60, pad=False):
        """
        将CADSequence对象转换为向量表示
        
        参数:
        max_n_ext: 最大拉伸操作数，默认为10
        max_n_loops: 最大环数，默认为6
        max_len_loop: 每个环的最大长度，默认为15
        max_total_len: 最大总长度，默认为60
        pad: 是否进行填充，默认为False
        
        返回:
        向量表示或None（如果转换失败）
        """
        if len(self.seq) > max_n_ext:
            return None
        vec_seq = []
        for item in self.seq:
            vec = item.to_vector(max_n_loops, max_len_loop, pad=False)
            if vec is None:
                return None
            vec = vec[:-1]  # 移除最后一个EOS标记
            vec_seq.append(vec)

        vec_seq = np.concatenate(vec_seq, axis=0)
        vec_seq = np.concatenate([vec_seq, EOS_VEC[np.newaxis]], axis=0)

        # 添加EOS填充
        if pad and vec_seq.shape[0] < max_total_len:
            pad_len = max_total_len - vec_seq.shape[0]
            vec_seq = np.concatenate([vec_seq, EOS_VEC[np.newaxis].repeat(pad_len, axis=0)], axis=0)

        return vec_seq

    def transform(self, translation, scale):
        """
        对CADSequence进行线性变换
        
        参数:
        translation: 平移向量
        scale: 缩放因子
        """
        for item in self.seq:
            item.transform(translation, scale)

    def normalize(self, size=1.0):
        """
        将形状归一化到单位立方体（-1~1）内
        
        参数:
        size: 目标大小，默认为1.0
        """
        scale = size * NORM_FACTOR / np.max(np.abs(self.bbox))
        self.transform(0.0, scale)

    def numericalize(self, n=256):
        """
        将CADSequence对象数值化
        
        参数:
        n: 数值化参数，默认为256
        """
        for item in self.seq:
            item.numericalize(n)

    def flip_sketch(self, axis):
        """
        翻转CADSequence中的所有草图
        
        参数:
        axis: 翻转轴
        """
        for item in self.seq:
            item.flip_sketch(axis)

    def random_transform(self):
        """对CADSequence进行随机变换"""
        for item in self.seq:
            # 随机变换草图
            scale = random.uniform(0.8, 1.2)
            item.profile.transform(-np.array([128, 128]), scale)
            translate = np.array([random.randint(-5, 5), random.randint(-5, 5)], dtype=np.integer) + 128
            item.profile.transform(translate, 1)

            # 随机变换和缩放拉伸
            t = 0.05
            translate = np.array([random.uniform(-t, t), random.uniform(-t, t), random.uniform(-t, t)])
            scale = random.uniform(0.8, 1.2)
            item.sketch_pos = (item.sketch_pos + translate) * scale
            item.extent_one *= random.uniform(0.8, 1.2)
            item.extent_two *= random.uniform(0.8, 1.2)

    def random_flip_sketch(self):
        """随机翻转CADSequence中的草图"""
        for item in self.seq:
            flip_idx = random.randint(0, 3)
            if flip_idx > 0:
                item.flip_sketch(['x', 'y', 'xy'][flip_idx - 1])
