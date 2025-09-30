from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Circ, gp_Pln, gp_Vec, gp_Ax3, gp_Ax2, gp_Lin
from OCC.Core.BRepBuilderAPI import (BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeFace, BRepBuilderAPI_MakeWire)
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse, BRepAlgoAPI_Common
from OCC.Core.GC import GC_MakeArcOfCircle
from OCC.Extend.DataExchange import write_stl_file
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRepBndLib import brepbndlib_Add
from copy import copy
from .extrude import *
from .sketch import Loop, Profile
from .curves import *
import os
import trimesh
from trimesh.sample import sample_surface
import random


def vec2CADsolid(vec, is_numerical=True, n=256):
    """
    将向量转换为CAD实体

    参数:
    vec (numpy.array): 包含CAD信息的向量
    is_numerical (bool): 是否进行数值化处理
    n (int): 数值化参数

    返回:
    CAD实体
    """
    cad = CADSequence.from_vector(vec, is_numerical=is_numerical, n=256)
    cad = create_CAD(cad)
    return cad


def create_CAD(cad_seq: CADSequence):
    """
    从CADSequence创建3D CAD模型。仅支持带布尔操作的拉伸。

    参数:
    cad_seq (CADSequence): CAD序列

    返回:
    3D CAD模型
    """
    body = create_by_extrude(cad_seq.seq[0])
    for extrude_op in cad_seq.seq[1:]:
        new_body = create_by_extrude(extrude_op)
        if extrude_op.operation == EXTRUDE_OPERATIONS.index("NewBodyFeatureOperation") or \
                extrude_op.operation == EXTRUDE_OPERATIONS.index("JoinFeatureOperation"):
            body = BRepAlgoAPI_Fuse(body, new_body).Shape()
        elif extrude_op.operation == EXTRUDE_OPERATIONS.index("CutFeatureOperation"):
            body = BRepAlgoAPI_Cut(body, new_body).Shape()
        elif extrude_op.operation == EXTRUDE_OPERATIONS.index("IntersectFeatureOperation"):
            body = BRepAlgoAPI_Common(body, new_body).Shape()
    return body


def create_by_extrude(extrude_op: Extrude):
    """
    从Extrude实例创建实体

    参数:
    extrude_op (Extrude): 拉伸操作实例

    返回:
    实体
    """
    profile = copy(extrude_op.profile) # 使用副本以防止内部更改extrude_op
    profile.denormalize(extrude_op.sketch_size)

    sketch_plane = copy(extrude_op.sketch_plane)
    sketch_plane.origin = extrude_op.sketch_pos

    face = create_profile_face(profile, sketch_plane)
    normal = gp_Dir(*extrude_op.sketch_plane.normal)
    ext_vec = gp_Vec(normal).Multiplied(extrude_op.extent_one)
    body = BRepPrimAPI_MakePrism(face, ext_vec).Shape()
    if extrude_op.extent_type == EXTENT_TYPE.index("SymmetricFeatureExtentType"):
        body_sym = BRepPrimAPI_MakePrism(face, ext_vec.Reversed()).Shape()
        body = BRepAlgoAPI_Fuse(body, body_sym).Shape()
    if extrude_op.extent_type == EXTENT_TYPE.index("TwoSidesFeatureExtentType"):
        ext_vec = gp_Vec(normal.Reversed()).Multiplied(extrude_op.extent_two)
        body_two = BRepPrimAPI_MakePrism(face, ext_vec).Shape()
        body = BRepAlgoAPI_Fuse(body, body_two).Shape()
    return body


def create_profile_face(profile: Profile, sketch_plane: CoordSystem):
    """
    从草图轮廓和草图平面创建面

    参数:
    profile (Profile): 草图轮廓
    sketch_plane (CoordSystem): 草图平面

    返回:
    面
    """
    origin = gp_Pnt(*sketch_plane.origin)
    normal = gp_Dir(*sketch_plane.normal)
    x_axis = gp_Dir(*sketch_plane.x_axis)
    gp_face = gp_Pln(gp_Ax3(origin, normal, x_axis))

    all_loops = [create_loop_3d(loop, sketch_plane) for loop in profile.children]
    topo_face = BRepBuilderAPI_MakeFace(gp_face, all_loops[0])
    for loop in all_loops[1:]:
        topo_face.Add(loop.Reversed())
    return topo_face.Face()


def create_loop_3d(loop: Loop, sketch_plane: CoordSystem):
    """
    创建3D草图环

    参数:
    loop (Loop): 草图环
    sketch_plane (CoordSystem): 草图平面

    返回:
    3D草图环
    """
    topo_wire = BRepBuilderAPI_MakeWire()
    for curve in loop.children:
        topo_edge = create_edge_3d(curve, sketch_plane)
        if topo_edge == -1: # 忽略
            continue
        topo_wire.Add(topo_edge)
    return topo_wire.Wire()


def create_edge_3d(curve: CurveBase, sketch_plane: CoordSystem):
    """
    创建3D边

    参数:
    curve (CurveBase): 曲线
    sketch_plane (CoordSystem): 草图平面

    返回:
    3D边
    """
    if isinstance(curve, Line):
        if np.allclose(curve.start_point, curve.end_point):
            return -1
        start_point = point_local2global(curve.start_point, sketch_plane)
        end_point = point_local2global(curve.end_point, sketch_plane)
        topo_edge = BRepBuilderAPI_MakeEdge(start_point, end_point)
    elif isinstance(curve, Circle):
        center = point_local2global(curve.center, sketch_plane)
        axis = gp_Dir(*sketch_plane.normal)
        gp_circle = gp_Circ(gp_Ax2(center, axis), abs(float(curve.radius)))
        topo_edge = BRepBuilderAPI_MakeEdge(gp_circle)
    elif isinstance(curve, Arc):
        # 打印起点、中点和终点
        start_point = point_local2global(curve.start_point, sketch_plane)
        mid_point = point_local2global(curve.mid_point, sketch_plane)
        end_point = point_local2global(curve.end_point, sketch_plane)
        arc = GC_MakeArcOfCircle(start_point, mid_point, end_point).Value()
        topo_edge = BRepBuilderAPI_MakeEdge(arc)
    else:
        raise NotImplementedError(type(curve))
    return topo_edge.Edge()


def point_local2global(point, sketch_plane: CoordSystem, to_gp_Pnt=True):
    """
    将草图平面局部坐标中的点转换为全局坐标

    参数:
    point (array-like): 点的局部坐标
    sketch_plane (CoordSystem): 草图平面
    to_gp_Pnt (bool): 是否转换为gp_Pnt对象

    返回:
    全局坐标点
    """
    g_point = point[0] * sketch_plane.x_axis + point[1] * sketch_plane.y_axis + sketch_plane.origin
    if to_gp_Pnt:
        return gp_Pnt(*g_point)
    return g_point


def CADsolid2pc(shape, n_points, name=None):
    """
    将OpenCASCADE实体转换为点云

    参数:
    shape: OpenCASCADE实体
    n_points (int): 点云中的点数
    name (str): 临时文件名

    返回:
    点云
    """
    bbox = Bnd_Box()
    brepbndlib_Add(shape, bbox)
    if bbox.IsVoid():
        raise ValueError("box check failed")

    if name is None:
        name = random.randint(100000, 999999)
    write_stl_file(shape, "tmp_out_{}.stl".format(name))
    out_mesh = trimesh.load("tmp_out_{}.stl".format(name))
    os.system("rm tmp_out_{}.stl".format(name))
    out_pc, _ = sample_surface(out_mesh, n_points)
    return out_pc
