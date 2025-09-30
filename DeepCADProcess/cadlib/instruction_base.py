from enum import Enum
from typing import List, Tuple, Union, Optional
import numpy as np

class OperationType(Enum):
    NEWBODY = "newbody"
    JOIN = "join"
    CUT = "cut"
    INTERSECT = "intersect"


class Curve():
    """线段、圆弧、圆等曲线的基类"""
    pass

class Line(Curve):
    def __init__(self, *args, name: str = None):
        super().__init__()
        if len(args) == 1:
            # 只有一个点参数时，认为是终点
            self.start_point = None
            self.end_point = args[0]
        elif len(args) == 2:
            # 两个点参数时，分别是起点和终点
            self.start_point = args[0]
            self.end_point = args[1]
        else:
            raise ValueError("Line必须提供1个或2个点坐标参数")
        self.name = name

class Arc(Curve):
    def __init__(self, *args, name: str = None):
        super().__init__()
        if len(args) == 2:
            # 两个点参数时，认为是中点和终点
            self.start_point = None
            self.mid_point = args[0]
            self.end_point = args[1]
        elif len(args) == 3:
            # 三个点参数时，分别是起点、中点和终点
            self.start_point = args[0]
            self.mid_point = args[1]
            self.end_point = args[2]
        else:
            raise ValueError("Arc必须提供2个或3个点坐标参数")
        self.name = name

class Circle(Curve):
    def __init__(self, *args, name: str = None):
        super().__init__()
        if len(args) == 2 and isinstance(args[1], (int, float)):
            # 当第二个参数是数字时，认为是(圆心, 半径)
            self.center_point = args[0]
            self.radius = args[1]
        else:
            raise ValueError("Circle必须提供圆心坐标和半径两个参数")
        self.name = name

class Loop:
    """表示一个闭合的轮廓"""
    def __init__(self, curves: List[Union[Line, Arc, Circle]]):
        """
        参数:
            curves: 组成闭合轮廓的曲线列表
        """
        self.curves = curves

class Profile:
    def __init__(self, loops: List[Loop]):
        self.loops = loops

class Constraint:
    def __init__(self, curves: List[Curve], constraint_type: str, parameter: Optional[float] = None):
        self.curves = curves
        self.constraint_type = constraint_type
        self.parameter = parameter

class Sketch:
    def __init__(self, profiles: List[Profile] = None, constraints: List[Constraint] = None):
        self.profiles = profiles if profiles else []
        self.constraints = constraints if constraints else []
    
    def add_profile(self, profiles: List[Profile]):
        """添加轮廓到草图中"""
        if not isinstance(profiles, list):
            profiles = [profiles]
        self.profiles.extend(profiles)
    
    def add_constraint(self, constraints: List[Constraint]):
        """添加约束到草图中"""
        if not isinstance(constraints, list):
            constraints = [constraints]
        self.constraints.extend(constraints)

class Workplane():
    def __init__(self, origin: np.ndarray, ratate: np.ndarray):
        self.origin = origin
        self.ratate = ratate

class WorkplanePre():
    def __init__(self, plane_name: str):
        self.plane_name = plane_name

class WorkplaneRef():
    def __init__(self, reference_part: str, z_axis: np.ndarray, reference_line: Optional[Line] = None):
        self.reference_part = reference_part
        self.z_axis = z_axis
        self.reference_line = reference_line

class Extrude():
    def __init__(self, workplane: Union[Workplane, WorkplanePre, WorkplaneRef],
                 sketch: Sketch,
                 operate: OperationType,
                 distance_1: float,
                 distance_2: float = 0,
                 symmetric: bool = False):
        self.workplane = workplane
        self.sketch = sketch
        self.operate = operate
        self.distance_1 = distance_1
        self.distance_2 = distance_2
        self.symmetric = symmetric

