# @Time    : 2024/12/26 10:05
# @Author  : 吕超凡
# @File    : render_util.py
# @Description : 提供用于渲染CAD模型的工具函数，包括草图渲染、step渲染和构造序列渲染。

from DeepCADProcess.cadlib.visualize import create_by_extrude
from DeepCADProcess.cadlib.macro import *
from DeepCADProcess.cadlib.sketch import Profile
from DeepCADProcess.utils.part_label import get_part_position, add_labels_to_image

from OCC.Display.OCCViewer import Viewer3d
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCC.Core.AIS import AIS_Shape, AIS_WireFrame, AIS_Shaded
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut, BRepAlgoAPI_Fuse, BRepAlgoAPI_Common
import os
from pathlib import Path
from PIL import Image  # 导入Image
import matplotlib.pyplot as plt



color_list = [
    Quantity_Color(0.8, 0.0, 0.0, Quantity_TOC_RGB),  # 红色
    Quantity_Color(0.0, 1.0, 0.0, Quantity_TOC_RGB),  # 绿色
    Quantity_Color(0.0, 0.0, 1.0, Quantity_TOC_RGB),  # 蓝色
    Quantity_Color(1.0, 1.0, 0.0, Quantity_TOC_RGB),  # 黄色
    Quantity_Color(0.0, 1.0, 1.0, Quantity_TOC_RGB),  # 青色
    Quantity_Color(1.0, 0.0, 1.0, Quantity_TOC_RGB),  # 品红
    Quantity_Color(1.0, 0.5, 0.0, Quantity_TOC_RGB),  # 橙色
    Quantity_Color(0.5, 0.0, 1.0, Quantity_TOC_RGB),  # 紫色
    Quantity_Color(0.6, 0.3, 0.0, Quantity_TOC_RGB),  # 棕色
    Quantity_Color(1.0, 0.7, 0.8, Quantity_TOC_RGB),  # 粉色
]

views = [
    ("front_top_left.png", (1, 1, 1)),  # 前上左斜视图
    ("front_bottom_left.png", (1, 1, -1)),  # 前下左斜视图
    ("front_top_right.png", (1, -1, 1)),  # 前上右斜视图, 也是默认视图
    ("front_bottom_right.png", (1, -1, -1)),  # 前下左斜视图
    ("back_top_left.png", (-1, 1, 1)),  # 后上左斜视图
    ("back_top_right.png", (-1, -1, 1)),  # 后上右斜视图
    ("back_bottom_left.png", (-1, 1, -1)),  # 后下左斜视图
    ("back_bottom_right.png", (-1, -1, -1))  # 后下右斜视图
]


def render_with_colors(bodies, saved_folder_path, view_direction=None, width=512, height=512):
    # 不同的实体使用不同的颜色来渲染
    ################   离屏渲染  #############################
    # 创建离屏渲染器
    offscreen_renderer = Viewer3d()
    offscreen_renderer.Create()
    offscreen_renderer.SetModeShaded()

    label_images_folder = saved_folder_path.replace("images_with_color", "images_with_color_and_label")
    os.makedirs(label_images_folder, exist_ok=True)

    for index, body in enumerate(bodies):
        ais_shape = AIS_Shape(body)
        ais_shape.SetColor(color_list[index])
        ais_shape.SetDisplayMode(AIS_Shaded)
        offscreen_renderer.Context.Display(ais_shape, True)  # 显示实体

        # 创建一个新的形状实例用于显示线框
        ais_wire = AIS_Shape(body)
        ais_wire.SetColor(Quantity_Color(0.0, 0.0, 0.0, Quantity_TOC_RGB))
        # 设置线框显示模式
        ais_wire.SetDisplayMode(AIS_WireFrame)
        offscreen_renderer.Context.Display(ais_wire, True)  # 显示边框

    
    for (name, direction) in views:
        offscreen_renderer.View.SetProj(*direction)
        image_path = os.path.join(saved_folder_path, name)
        offscreen_renderer.FitAll()
        offscreen_renderer.View.Dump(image_path)
        # 添加标号
        output_path = os.path.join(label_images_folder, name)
        labels_positions = get_part_position(image_path)
        add_labels_to_image(labels_positions, image_path, output_path)




def render_sketch(data, saved_folder_path):
    index = 0
    for item in data["sequence"]:
        if item["type"] == "ExtrudeFeature":
            extrude_entity = data["entities"][item["entity"]]
            assert extrude_entity["start_extent"]["type"] == "ProfilePlaneStartDefinition"

            profiles = extrude_entity["profiles"]
            fig, ax = plt.subplots()
            for profile in profiles:
                sket_id, profile_id = profile["sketch"], profile["profile"]
                # 草图参数
                sket_entity = data["entities"][sket_id]
                sket_profile = Profile.from_dict(sket_entity["profiles"][profile_id])
                sket_profile.draw(ax)
            
            # 隐藏坐标轴和边框
            plt.axis('off')
            plt.gca().spines[['top', 'bottom', 'left', 'right']].set_visible(False)
            plt.savefig(os.path.join(saved_folder_path, f"sketch_{index}.png"))
            plt.close(fig)

            index += 1


def render_step(body, image_path, width=800, height=600):
    offscreen_renderer = Viewer3d()
    offscreen_renderer.Create()
    offscreen_renderer.SetSize(width, height)
    offscreen_renderer.SetModeShaded()   

    ais_shape = AIS_Shape(body)
    # ais_shape.SetTransparency(0.05)  # 设置透明度，0.0 完全不透明，1.0 完全透明
    offscreen_renderer.Context.Display(ais_shape, True)
    offscreen_renderer.FitAll()
    offscreen_renderer.View.Dump(image_path)


def render_step_with_highlight(old_body, new_body, image_path, is_cut_operation=False, width=800, height=600):
    ################   离屏渲染  #############################
    # 创建离屏渲染器
    offscreen_renderer = Viewer3d()
    offscreen_renderer.Create()
    offscreen_renderer.SetSize(width, height)
    offscreen_renderer.SetModeShaded()

    if old_body:
        ais_shape = AIS_Shape(old_body)
        ais_shape.SetTransparency(0.5)  # 设置透明度，0.0 完全不透明，1.0 完全透明
        offscreen_renderer.Context.Display(ais_shape, True)

    # 创建新实体的着色显示
    new_ais_shape = AIS_Shape(new_body)
    if is_cut_operation:
        new_color = Quantity_Color(0, 0, 1, Quantity_TOC_RGB)  # 蓝色
    else:
        new_color = Quantity_Color(1, 0, 0, Quantity_TOC_RGB)  # 红色
    new_ais_shape.SetColor(new_color)
    new_ais_shape.SetTransparency(0.1)  # 设置透明度
    offscreen_renderer.Context.Display(new_ais_shape, True)

    # 创建新实体的线框显示
    ais_wire = AIS_Shape(new_body)
    ais_wire.SetColor(Quantity_Color(0.0, 0.0, 0.0, Quantity_TOC_RGB))
    # 设置线框显示模式
    ais_wire.SetDisplayMode(AIS_WireFrame)
    offscreen_renderer.Context.Display(ais_wire, True)  # 显示边框

    offscreen_renderer.FitAll()
    offscreen_renderer.View.Dump(image_path)


def get_extrude_body(extrude_seq):
    body = create_by_extrude(extrude_seq[0])
    for extrude_op in extrude_seq[1:]:
        new_body = create_by_extrude(extrude_op)
        body = BRepAlgoAPI_Fuse(body, new_body).Shape()
    return body


def render_construction_sequence(cad_seq_list, saved_folder_path):
    # body_list用于将每个实体用不同的颜色显示
    body_list = []
    body = None
    for index, extrude_seq in enumerate(cad_seq_list):
        new_body = get_extrude_body(extrude_seq)
        operation = extrude_seq[0].operation
        is_cut = True if operation == EXTRUDE_OPERATIONS.index("CutFeatureOperation") else False
        image_path = os.path.join(saved_folder_path, f"extrude_{index}"+".png")
        render_step_with_highlight(body, new_body, image_path, is_cut)
        if body is None:
            body = new_body
        else:
            if operation == EXTRUDE_OPERATIONS.index("NewBodyFeatureOperation") or \
                operation == EXTRUDE_OPERATIONS.index("JoinFeatureOperation"):
                body = BRepAlgoAPI_Fuse(body, new_body).Shape()
            elif operation == EXTRUDE_OPERATIONS.index("IntersectFeatureOperation"):
                body = BRepAlgoAPI_Common(body, new_body).Shape()
            elif operation == EXTRUDE_OPERATIONS.index("CutFeatureOperation"):
                body = BRepAlgoAPI_Cut(body, new_body).Shape()
                # 剪切body_list中的相关实体
                for i in range(len(body_list)):
                    # 检测是否有交集
                    # if not BRepAlgoAPI_Common(body_list[i], new_body).IsDone():
                    #     continue  # 如果没有交集，跳过剪切
                    body_list[i] = BRepAlgoAPI_Cut(body_list[i], new_body).Shape()
                continue
        body_list.append(new_body)
    render_step(body, os.path.join(saved_folder_path, "final_modal.png"))
    images_folder = os.path.join(saved_folder_path, "images_with_color")
    os.makedirs(images_folder, exist_ok=True)
    render_with_colors(body_list, images_folder)
    return body


def render_step_to_image(step_file_path, output_image_path, width=512, height=512,
                         view_direction=None):
    """
    Renders a STEP file to an image.
    :param step_file_path: The path to the STEP file.
    :param output_image_path: The path where the output image will be saved.
    :param width: The width of the output image.
    :param height: The height of the output image.
    :param view_direction: A tuple (x, y, z) specifying the view direction.
    """
    if not os.path.exists(step_file_path):
        raise FileNotFoundError(f"STEP file '{step_file_path}' not found.")

    # Create the renderer
    offscreen_renderer = Viewer3d()

    offscreen_renderer.SetSize(width, height)
    offscreen_renderer.Create()
    offscreen_renderer.SetModeShaded()

    step_reader = STEPControl_Reader()
    status = step_reader.ReadFile(step_file_path)

    if status != 1:
        raise ValueError(f"Error reading STEP file '{step_file_path}'.")

    step_reader.TransferRoots()
    shape = step_reader.Shape()

    # Send the shape to the renderer
    offscreen_renderer.DisplayShape(shape, update=True)

    if view_direction is not None:
        offscreen_renderer.View.SetProj(*view_direction)

    # Export the view to image
    offscreen_renderer.View.Dump(output_image_path)


if __name__ == "__main__":
    render_step("test/test.step", "test/output.png")
