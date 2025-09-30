import math
import numpy as np
from scipy.spatial.transform import Rotation as R

def rads_to_degs(rads):
    """
    将角度从弧度转换为度数
    
    参数:
    rads (float): 弧度表示的角度
    
    返回:
    float: 度数表示的角度
    """
    return 180 * rads / math.pi


def angle_from_vector_to_x(vec):
    """
    计算单位向量与正x轴之间的角度（0~2pi）
    
    参数:
    vec (numpy.array): 二维单位向量
    
    返回:
    float: 向量与正x轴之间的角度（0~2pi）
    """
    angle = 0.0
    # 将平面分为四个象限:
    # 2 | 1
    # -------
    # 3 | 4
    if vec[0] >= 0:
        if vec[1] >= 0:
            # 第一象限
            angle = math.asin(vec[1])
        else:
            # 第四象限
            angle = 2.0 * math.pi - math.asin(-vec[1])
    else:
        if vec[1] >= 0:
            # 第二象限
            angle = math.pi - math.asin(vec[1])
        else:
            # 第三象限
            angle = math.pi + math.asin(-vec[1])
    return angle


def cartesian2polar(vec, with_radius=False):
    """
    将笛卡尔坐标系中的向量转换为极坐标（球坐标）系
    
    参数:
    vec (numpy.array): 笛卡尔坐标系中的向量
    with_radius (bool): 是否包含半径信息
    
    返回:
    numpy.array: 极坐标（球坐标）系中的向量
    """
    vec = vec.round(6)
    norm = np.linalg.norm(vec)
    theta = np.arccos(vec[2] / norm)  # (0, pi)  极角，也称为仰角或天顶角，是从正z轴到点P的连线与正z轴之间的角度。
    phi = np.arctan(vec[1] / (vec[0] + 1e-15))  # (-pi, pi) 方位角是从正x轴到点P在xy平面上的投影点与正x轴之间的角度。
    if not with_radius:
        return np.array([theta, phi])
    else:
        return np.array([theta, phi, norm])


def polar2cartesian(vec):
    """
    将极坐标（球坐标）系中的向量转换为笛卡尔坐标系
    
    参数:
    vec (numpy.array): 极坐标（球坐标）系中的向量
    
    返回:
    numpy.array: 笛卡尔坐标系中的向量
    """
    r = 1 if len(vec) == 2 else vec[2]
    theta, phi = vec[0], vec[1]
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return np.array([x, y, z])


def rotate_by_x(vec, theta):
    """
    绕x轴旋转向量
    
    参数:
    vec (numpy.array): 待旋转的向量
    theta (float): 旋转角度（弧度）
    
    返回:
    numpy.array: 旋转后的向量
    """
    mat = np.array([[1, 0, 0],
                    [0, np.cos(theta), -np.sin(theta)],
                    [0, np.sin(theta), np.cos(theta)]])
    return np.dot(mat, vec)


def rotate_by_y(vec, theta):
    """
    绕y轴旋转向量
    
    参数:
    vec (numpy.array): 待旋转的向量
    theta (float): 旋转角度（弧度）
    
    返回:
    numpy.array: 旋转后的向量
    """
    mat = np.array([[np.cos(theta), 0, np.sin(theta)],
                    [0, 1, 0],
                    [-np.sin(theta), 0, np.cos(theta)]])
    return np.dot(mat, vec)


def rotate_by_z(vec, phi):
    """
    绕z轴旋转向量
    
    参数:
    vec (numpy.array): 待旋转的向量
    phi (float): 旋转角度（弧度）
    
    返回:
    numpy.array: 旋转后的向量
    """
    mat = np.array([[np.cos(phi), -np.sin(phi), 0],
                    [np.sin(phi), np.cos(phi), 0],
                    [0, 0, 1]])
    return np.dot(mat, vec)


def polar_parameterization(normal_3d, x_axis_3d):
    """
    通过从标准3D坐标系的旋转来表示一个坐标系
    
    参数:
    normal_3d (numpy.array): 法线方向（z轴）的单位向量
    x_axis_3d (numpy.array): x轴的单位向量
    
    返回:
    tuple: (theta, phi, gamma)
    极角：是一个从z轴到投影在xy平面的向量之间的角度；
    方位角：是从正x轴开始逆时针旋转到投影在xy平面上的向量之间的角度。
    旋转角：gamma是在由theta和 phi所定义的平面内，沿着法向量 (normal vector) 的方向，x轴的向量围绕z轴旋转的角度。
    """
    normal_polar = cartesian2polar(normal_3d)
    theta = normal_polar[0]
    phi = normal_polar[1]

    ref_x = rotate_by_z(rotate_by_y(np.array([1, 0, 0]), theta), phi)

    gamma = np.arccos(np.dot(x_axis_3d, ref_x).round(6))
    if np.dot(np.cross(ref_x, x_axis_3d), normal_3d) < 0:
        gamma = -gamma
    return theta, phi, gamma


def polar_parameterization_inverse(theta, phi, gamma):
    """
    根据给定的从标准3D坐标系的旋转来构建一个坐标系
    
    参数:
    theta (float): 极角
    phi (float): 方位角
    gamma (float): 绕法线方向的旋转角
    
    返回:
    tuple: (normal_3d, x_axis_3d) 新坐标系的法线方向和x轴方向
    """
    normal_3d = polar2cartesian([theta, phi])
    ref_x = rotate_by_z(rotate_by_y(np.array([1, 0, 0]), theta), phi)
    ref_y = np.cross(normal_3d, ref_x)
    x_axis_3d = ref_x * np.cos(gamma) + ref_y * np.sin(gamma)
    return normal_3d, x_axis_3d


def calculate_rotation_angles(x_axis_3d, y_axis_3d, normal_3d):
    """
    从标准笛卡尔坐标系 (世界坐标系) 旋转到你定义的工作平面坐标系 (由 x_axis_3d、y_axis_3d和 normal_3d定义) 所需的绕 x、y 和 z 轴的旋转角度
    Args:
        x_axis_3d:
        y_axis_3d:
        normal_3d:

    Returns:

    """
    # 使用 np.eye(3) 创建初始矩阵（单位矩阵）
    original_basis = np.eye(3)

    # 将三个轴标准化成一个旋转矩阵（列向量互为正交）
    target_basis = np.column_stack([x_axis_3d, y_axis_3d, normal_3d])

    # 创建从初始基地到目标基的旋转
    rotation_matrix = np.dot(target_basis, original_basis.T)

    # 使用 scipy.spatial.transform.Rotation 从旋转矩阵计算出欧拉角
    rotation = R.from_matrix(rotation_matrix)

    # 获取 XYZ 轴上的旋转角度（单位为度）
    x_degree, y_degree, z_degree = rotation.as_euler('xyz', degrees=True)

    return x_degree, y_degree, z_degree


def get_rotation_angles(x_axis_3d, y_axis_3d, normal_3d):
    # 2. 按X-Y-Z顺序计算旋转角度
    # 2. 分解为X-Y-Z顺序的欧拉角
    def get_angles(R):
        # 注意:按右手螺旋法则确定正方向
        # 例如:Y轴旋转到Z轴,需要绕X轴逆时针旋转90°,所以是+90°

        if abs(R[2, 0]) != 1:  # 非奇异情况
            theta_y = np.arcsin(-R[2, 0])  # 绕Y轴旋转角
            cos_y = np.cos(theta_y)

            # 绕X轴旋转:拇指指向X轴正方向,逆时针为正
            theta_x = np.arctan2(R[2, 1] / cos_y, R[2, 2] / cos_y)

            # 绕Y轴旋转:拇指指向Y轴正方向,逆时针为正
            # theta_y 已计算

            # 绕Z轴旋转:拇指指向Z轴正方向,逆时针为正
            theta_z = np.arctan2(R[1, 0] / cos_y, R[0, 0] / cos_y)

        else:  # 万向节死锁
            theta_z = 0
            if R[2, 0] == -1:
                theta_y = np.pi / 2
                theta_x = theta_z + np.arctan2(R[0, 1], R[0, 2])
            else:
                theta_y = -np.pi / 2
                theta_x = -theta_z + np.arctan2(-R[0, 1], -R[0, 2])

        return np.array([theta_x, theta_y, theta_z])

    # 3. 构建目标旋转矩阵
    R_target = np.array([
        x_axis_3d,
        y_axis_3d,
        normal_3d
    ])

    # 4. 计算角度并转换为度数
    angles = - get_angles(R_target) * 180.0 / np.pi

    return angles[0], angles[1], angles[2]


def point_to_line_distance(point, start, end):
    """计算点到线段的最短距离
    
    参数:
        point: 点的坐标 [x, y]
        start: 线段起点坐标 [x, y]
        end: 线段终点坐标 [x, y]
        
    返回:
        float: 点到线段的最短距离
    """
    # 将坐标转换为向量
    line_vec = [end[0] - start[0], end[1] - start[1]]  # 线段向量
    point_vec = [point[0] - start[0], point[1] - start[1]]  # 点到起点的向量
    line_len = (line_vec[0]**2 + line_vec[1]**2)**0.5  # 线段长度
    
    # 如果线段长度为0，则直接返回点到起点的距离
    if line_len == 0:
        return (point_vec[0]**2 + point_vec[1]**2)**0.5
        
    # 计算投影比例 t
    t = max(0, min(1, (point_vec[0]*line_vec[0] + point_vec[1]*line_vec[1]) / (line_len**2)))
    
    # 计算投影点坐标
    proj_point = [
        start[0] + t * line_vec[0],
        start[1] + t * line_vec[1]
    ]
    
    # 返回点到投影点的距离
    return ((point[0] - proj_point[0])**2 + (point[1] - proj_point[1])**2)**0.5


def point_to_point_distance(point1, point2):
    """计算二维点之间的距离"""
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def are_vectors_parallel(vector1, vector2):
    """判断两个三维向量是否平行"""
    dot_product = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    if magnitude1 * magnitude2 == 0:
        return True  # 如果其中一个向量的长度为0，则认为它们平行
    cos_angle = dot_product / (magnitude1 * magnitude2)
    return abs(cos_angle) == 1  # 如果夹角的余弦值为1或-1，则向量平行

def are_vectors_orthogonal(vector1, vector2):
    """判断两个三维向量是否垂直"""
    dot_product = np.dot(vector1, vector2)
    return dot_product == 0  # 如果两个向量的点积为0，则它们垂直


def calculate_point_2_plane_distance(point, plane_origin, plane_normal):
    """计算点到平面的距离"""
    return np.dot(point - plane_origin, plane_normal)

# 判断线段的起点和终点是否在平面上
def check_point_in_plane(start_point, end_point, plane_origin, plane_normal):
    return np.dot(start_point - plane_origin, plane_normal) == 0 and np.dot(end_point - plane_origin, plane_normal) == 0


#计算指定点在某个平面（x_axis, z_axis, origin）上的投影点
def calculate_projection_point(point, plane_origin, plane_normal):
    return point - np.dot(point - plane_origin, plane_normal) * plane_normal


def convert_2d_to_3d(point_2d, origin, x_axis, y_axis):
    """将2D点转换为3D点"""
    return point_2d[0] * x_axis + point_2d[1] * y_axis + origin


def convert_offset_3d_to_2d(offset_3d, x_axis, y_axis):
    """将3D偏移量转换为2D偏移量"""
    return [np.dot(offset_3d, x_axis), np.dot(offset_3d, y_axis)]


def is_point_in_rectangle(point, vertices):
    """
    判断点point是否在由vertices定义的矩形内。
    
    参数:
    point: 一个三维点，形式为一个包含三个坐标的numpy数组
    vertices: 矩形的四个顶点，形式为一个包含四个三维点的列表或数组
    
    返回:
    bool: 如果点在矩形内，返回True，否则返回False
    """
    vertices = np.array(vertices)
    point = np.array(point)
    
    # 1. 计算平面法向量（使用前三个点）
    v1 = vertices[1] - vertices[0]
    v2 = vertices[2] - vertices[0]
    normal = np.cross(v1, v2)
    normal = normal / np.linalg.norm(normal)  # 单位化
    
    # 2. 判断点是否在平面上
    distance_to_plane = abs(np.dot(point - vertices[0], normal))
    if distance_to_plane > 1e-10:  # 使用小阈值来处理浮点数精度问题
        return False
        
    # 3. 将3D点投影到2D平面
    # 选择最适合的投影平面（选择法向量分量最大的轴）
    max_axis = np.argmax(np.abs(normal))
    indices = [i for i in range(3) if i != max_axis]
    
    # 投影点和顶点到2D平面
    point_2d = point[indices]
    vertices_2d = vertices[:, indices]
    
    # 4. 对顶点进行排序，确保它们按照逆时针或顺时针顺序排列
    # 计算质心
    center = np.mean(vertices_2d, axis=0)
    # 计算各点相对于质心的角度
    angles = np.arctan2(vertices_2d[:, 1] - center[1], 
                       vertices_2d[:, 0] - center[0])
    # 按角度排序顶点
    sorted_indices = np.argsort(angles)
    vertices_2d = vertices_2d[sorted_indices]
    
    # 5. 使用射线法判断点是否在多边形内
    inside = False
    n = len(vertices_2d)
    j = n - 1
    
    for i in range(n):
        if (((vertices_2d[i, 1] > point_2d[1]) != (vertices_2d[j, 1] > point_2d[1])) and
            (point_2d[0] < (vertices_2d[j, 0] - vertices_2d[i, 0]) * 
             (point_2d[1] - vertices_2d[i, 1]) / 
             (vertices_2d[j, 1] - vertices_2d[i, 1]) + vertices_2d[i, 0])):
            inside = not inside
        j = i
    
    return inside


def determine_base_plane(x_axis, y_axis, z_axis):
    """
    判断给定的x_axis, y_axis, z_axis是否属于某个基准平面。
    返回:str: 基准平面名称（如"XY", "YZ", "XZ"等）或"None"如果不属于任何基准平面
    """
    # 定义一个小的阈值来判断向量是否相等
    threshold = 1e-3

    # 遍历BASE_PlANE中的每个基准平面
    for plane_name, axes in BASE_PlANE.items():
        base_x, base_y, base_z = axes
        if (all(abs(x - bx) < threshold for x, bx in zip(x_axis, base_x)) and
            all(abs(y - by) < threshold for y, by in zip(y_axis, base_y)) and
            all(abs(z - bz) < threshold for z, bz in zip(z_axis, base_z))):
            return plane_name

    # 如果不属于任何基准平面
    return "None"






