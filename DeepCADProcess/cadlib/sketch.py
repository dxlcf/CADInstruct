import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from .curves import *
from .macro import *


##########################   基类  ###########################
class SketchBase(object):
    """草图的基类，表示一组曲线的集合。"""
    def __init__(self, children, reorder=True):
        self.children = children  # 存储草图中的子元素（曲线）

        if reorder:
            self.reorder()  # 如果需要，重新排序子元素

    @staticmethod
    def from_dict(stat):
        """
        从JSON数据构造草图

        参数:
            stat (dict): 包含草图数据的字典
        """
        raise NotImplementedError

    @staticmethod
    def from_vector(vec, start_point, is_numerical=True):
        """
        从向量表示构造草图

        参数:
            vec (np.array): 形状为(seq_len, n_args)的向量表示
            start_point (np.array): 形状为(2,)的起始点。如果为None，则隐式定义为最后一个终点。
            is_numerical (bool): 是否为数值表示
        """
        raise NotImplementedError

    def reorder(self):
        """重新排列曲线以遵循逆时针方向"""
        raise NotImplementedError

    @property
    def start_point(self):
        """返回草图的起始点"""
        return self.children[0].start_point

    @property
    def end_point(self):
        """返回草图的终点"""
        return self.children[-1].end_point

    @property
    def bbox(self):
        """计算草图的边界框（最小/最大点）"""
        all_points = np.concatenate([child.bbox for child in self.children], axis=0)
        return np.stack([np.min(all_points, axis=0), np.max(all_points, axis=0)], axis=0)

    @property
    def bbox_size(self):
        """计算边界框大小（高度和宽度的最大值）"""
        bbox_min, bbox_max = self.bbox[0], self.bbox[1]
        bbox_size = np.max(np.abs(np.concatenate([bbox_max - self.start_point, bbox_min - self.start_point])))
        return bbox_size

    @property
    def global_trans(self):
        """返回起始点和草图大小（边界框大小）"""
        return np.concatenate([self.start_point, np.array([self.bbox_size])])

    def transform(self, translate, scale):
        """对草图进行线性变换"""
        for child in self.children:
            child.transform(translate, scale)

    def flip(self, axis):
        """沿指定轴翻转草图"""
        for child in self.children:
            child.flip(axis)
        self.reorder()

    def numericalize(self, n=256):
        """将曲线参数量化为整数"""
        for child in self.children:
            child.numericalize(n)

    def normalize(self, size=256):
        """
        在给定大小内归一化草图，使起始点位于中心

        参数:
            size (int): 归一化后的大小
        """
        cur_size = self.bbox_size
        scale = (size / 2 * NORM_FACTOR - 1) / cur_size  # 防止数据增强时可能的溢出
        self.transform(-self.start_point, scale)  # 平移草图，使其起始点移动到原点，并且缩放草图
        self.transform(np.array((size / 2, size / 2)), 1)   # 再次平移草图，使其中心位于目标大小的中心，归一化后的草图应该没有负值。

    def denormalize(self, bbox_size, size=256):
        """
        归一化的逆过程，
        【归一化的逆过程少了一个平移步骤是合理的，因为在归一化过程中，草图的起始点已经被移动到中心位置。逆过程只需要将草图从中心位置移动回原来的位置，并进行适当的缩放即可。】

        参数:
            bbox_size (float): 目标边界框大小
            size (int): 归一化时使用的大小
        """
        scale = bbox_size / (size / 2 * NORM_FACTOR - 1)
        self.transform(-np.array((size / 2, size / 2)), scale)

    def to_vector(self):
        """将草图转换为向量表示"""
        raise NotImplementedError

    def draw(self, ax):
        """在matplotlib轴上绘制草图"""
        raise NotImplementedError

    def to_image(self):
        """将草图转换为图像"""
        fig, ax = plt.subplots()
        self.draw(ax)
        ax.axis('equal')
        fig.canvas.draw()
        X = np.array(fig.canvas.renderer.buffer_rgba())[:, :, :3]
        plt.close(fig)
        return X

    def sample_points(self, n=32):
        """从草图上均匀采样点"""
        raise NotImplementedError


####################### 环和轮廓 #######################
class Loop(SketchBase):
    """草图环，表示一系列连接的曲线。"""
    @staticmethod
    def from_dict(stat):
        """从字典构造环"""
        all_curves = [construct_curve_from_dict(item) for item in stat['profile_curves']]
        this_loop = Loop(all_curves)
        this_loop.is_outer = stat['is_outer']
        return this_loop

    def __str__(self):
        """返回环的字符串表示"""
        return "Loop:" + "\n      -" + "\n      -".join([str(curve) for curve in self.children])

    @staticmethod
    def from_vector(vec, start_point=None, is_numerical=True):
        """
        从向量表示构造环

        参数:
            vec (np.array): 向量表示
            start_point (np.array): 起始点
            is_numerical (bool): 是否为数值表示
        """
        all_curves = []
        if start_point is None:
            # FIXME: 这里可以避免显式的for循环
            for i in range(vec.shape[0]):
                if vec[i][0] == EOS_IDX:
                    start_point = vec[i - 1][1:3]
                    break
        for i in range(vec.shape[0]):
            type = vec[i][0]
            if type == SOL_IDX:
                continue
            elif type == EOS_IDX:
                break
            else:
                curve = construct_curve_from_vector(vec[i], start_point, is_numerical=is_numerical)
                start_point = vec[i][1:3]  # 当前曲线的终点作为下一条曲线的起点
            all_curves.append(curve)
        return Loop(all_curves)

    def reorder(self):
        """重新排序，从最左侧开始并按逆时针方向排列"""
        if len(self.children) <= 1:
            return

        start_curve_idx = -1
        sx, sy = 10000, 10000

        # 修正起点-终点顺序
        if np.allclose(self.children[0].start_point, self.children[1].start_point) or \
            np.allclose(self.children[0].start_point, self.children[1].end_point):
            self.children[0].reverse()

        # 修正起点-终点顺序并找到最左侧点
        for i, curve in enumerate(self.children):
            if i < len(self.children) - 1 and np.allclose(curve.end_point, self.children[i + 1].end_point):
                self.children[i + 1].reverse()
            if round(curve.start_point[0], 6) < round(sx, 6) or \
                    (round(curve.start_point[0], 6) == round(sx, 6) and round(curve.start_point[1], 6) < round(sy, 6)):
                start_curve_idx = i
                sx, sy = curve.start_point

        self.children = self.children[start_curve_idx:] + self.children[:start_curve_idx]

        # 确保大部分是逆时针方向
        if isinstance(self.children[0], Circle) or isinstance(self.children[-1], Circle):  # FIXME: 硬编码
            return
        start_vec = self.children[0].direction()
        end_vec = self.children[-1].direction(from_start=False)
        if np.cross(end_vec, start_vec) <= 0:
            for curve in self.children:
                curve.reverse()
            self.children.reverse()

    def to_vector(self, max_len=None, add_sol=True, add_eos=True):
        """
        将环转换为向量表示

        参数:
            max_len (int): 最大长度
            add_sol (bool): 是否添加起始标记
            add_eos (bool): 是否添加结束标记
        """
        loop_vec = np.stack([curve.to_vector() for curve in self.children], axis=0)
        if add_sol:
            loop_vec = np.concatenate([SOL_VEC[np.newaxis], loop_vec], axis=0)
        if add_eos:
            loop_vec = np.concatenate([loop_vec, EOS_VEC[np.newaxis]], axis=0)
        if max_len is None:
            return loop_vec

        if loop_vec.shape[0] > max_len:
            return None
        elif loop_vec.shape[0] < max_len:
            pad_vec = np.tile(EOS_VEC, max_len - loop_vec.shape[0]).reshape((-1, len(EOS_VEC)))
            loop_vec = np.concatenate([loop_vec, pad_vec], axis=0)  # (max_len, 1 + N_ARGS)
        return loop_vec

    def draw(self, ax):
        """在给定的轴上绘制环"""
        # colors = ['red', 'blue', 'green', 'brown', 'pink', 'yellow', 'purple', 'black'] * 10
        for i, curve in enumerate(self.children):
            # curve.draw(ax, colors[i])
            curve.draw(ax, color="black")

    def sample_points(self, n=32):
        """从环上均匀采样点"""
        points = np.stack([curve.sample_points(n) for curve in self.children], axis=0)  # (n_curves, n, 2)
        return points


class Profile(SketchBase):
    """草图轮廓，由一个或多个环组成的闭合区域。最外层环放在第一位。"""
    @staticmethod
    def from_dict(stat):
        """从字典构造轮廓"""
        all_loops = [Loop.from_dict(item) for item in stat['loops']]
        return Profile(all_loops)

    def __str__(self):
        """返回轮廓的字符串表示"""
        return "Profile:" + "\n    -".join([str(loop) for loop in self.children])

    @staticmethod
    def from_vector(vec, start_point=None, is_numerical=True):
        """
        从向量表示构造轮廓

        参数:
            vec (np.array): 向量表示
            start_point (np.array): 起始点
            is_numerical (bool): 是否为数值表示
        """
        all_loops = []
        command = vec[:, 0]
        end_idx = command.tolist().index(EOS_IDX)
        indices = np.where(command[:end_idx] == SOL_IDX)[0].tolist() + [end_idx]
        for i in range(len(indices) - 1):
            loop_vec = vec[indices[i]:indices[i + 1]]
            loop_vec = np.concatenate([loop_vec, EOS_VEC[np.newaxis]], axis=0)
            if loop_vec[0][0] == SOL_IDX and loop_vec[1][0] not in [SOL_IDX, EOS_IDX]:
                all_loops.append(Loop.from_vector(loop_vec, is_numerical=is_numerical))
        return Profile(all_loops)

    def reorder(self):
        """重新排序轮廓中的环"""
        if len(self.children) <= 1:
            return
        all_loops_bbox_min = np.stack([loop.bbox[0] for loop in self.children], axis=0).round(6)
        ind = np.lexsort(all_loops_bbox_min.transpose()[[1, 0]])
        self.children = [self.children[i] for i in ind]

    def draw(self, ax):
        """在给定的轴上绘制轮廓"""
        for i, loop in enumerate(self.children):
            loop.draw(ax)
            # ax.text(loop.start_point[0], loop.start_point[1], str(i))

    def to_vector(self, max_n_loops=None, max_len_loop=None, pad=True):
        """
        将轮廓转换为向量表示

        参数:
            max_n_loops (int): 最大环数
            max_len_loop (int): 每个环的最大长度
            pad (bool): 是否进行填充
        """
        loop_vecs = [loop.to_vector(None, add_eos=False) for loop in self.children]
        if max_n_loops is not None and len(loop_vecs) > max_n_loops:
            return None
        for vec in loop_vecs:
            if max_len_loop is not None and vec.shape[0] > max_len_loop:
                return None
        profile_vec = np.concatenate(loop_vecs, axis=0)
        profile_vec = np.concatenate([profile_vec, EOS_VEC[np.newaxis]], axis=0)
        if pad:
            pad_len = max_n_loops * max_len_loop - profile_vec.shape[0]
            profile_vec = np.concatenate([profile_vec, EOS_VEC[np.newaxis].repeat(pad_len, axis=0)], axis=0)
        return profile_vec

    def sample_points(self, n=32):
        """从轮廓上均匀采样点"""
        points = np.concatenate([loop.sample_points(n) for loop in self.children], axis=0)
        return points
