# @Time    : 2024/12/26 10:05
# @Author  : 吕超凡
# @File    : render_util.py
# @Description : 根据组件的颜色，给图片中的组件添加数字标签。 标签位置有待改进，基本够用
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import random


def calculate_label_color(rgb):
    """
    根据背景颜色计算标号颜色。
    如果背景颜色亮度高，返回黑色；否则返回白色。
    """
    brightness = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]  # 计算亮度
    return (0, 0, 0) if brightness > 0.5 else (255, 255, 255)  # 黑色或白色


# 修改 color_list，添加对比标号颜色
color_list = [
    {"label": 1, "rgb": (0.8, 0.0, 0.0), "label_color": calculate_label_color((0.8, 0.0, 0.0))},  # 红色
    {"label": 2, "rgb": (0.0, 1.0, 0.0), "label_color": calculate_label_color((0.0, 1.0, 0.0))},  # 绿色
    {"label": 3, "rgb": (0.0, 0.0, 1.0), "label_color": calculate_label_color((0.0, 0.0, 1.0))},  # 蓝色
    {"label": 4, "rgb": (1.0, 1.0, 0.0), "label_color": calculate_label_color((1.0, 1.0, 0.0))},  # 黄色
    {"label": 5, "rgb": (0.0, 1.0, 1.0), "label_color": calculate_label_color((0.0, 1.0, 1.0))},  # 青色
    {"label": 6, "rgb": (1.0, 0.0, 1.0), "label_color": calculate_label_color((1.0, 0.0, 1.0))},  # 品红
    {"label": 7, "rgb": (1.0, 0.5, 0.0), "label_color": calculate_label_color((1.0, 0.5, 0.0))},  # 橙色
    {"label": 8, "rgb": (0.5, 0.0, 1.0), "label_color": calculate_label_color((0.5, 0.0, 1.0))},  # 紫色
    {"label": 9, "rgb": (0.6, 0.3, 0.0), "label_color": calculate_label_color((0.6, 0.3, 0.0))},  # 棕色
    {"label": 10, "rgb": (1.0, 0.7, 0.8), "label_color": calculate_label_color((1.0, 0.7, 0.8))},  # 粉色
]


def is_square_color_match(image, center, rgb, side_length=15, tolerance=20):
    """
    检查以 center 为中心的边长为 side_length 的正方形区域的四个顶点是否都为指定颜色。
    
    :param image: 输入图像的 RGB 数组。
    :param center: 正方形的中心坐标 (cx, cy)。
    :param rgb: 目标颜色的 RGB 值 (r, g, b)。
    :param side_length: 正方形的边长。
    :param tolerance: 颜色匹配的容差范围。
    :return: True 如果正方形的四个顶点都匹配目标颜色，否则 False。
    """
    cx, cy = center
    half_side = side_length // 2  # 半边长

    # 定义正方形的四个顶点
    square_points = [
        (cx - half_side, cy - half_side),  # 左上角
        (cx + half_side, cy - half_side),  # 右上角
        (cx - half_side, cy + half_side),  # 左下角
        (cx + half_side, cy + half_side),  # 右下角
    ]

    # 将目标颜色转换为上下界
    lower_bound = np.array([max(0, c * 255 - tolerance) for c in rgb])
    upper_bound = np.array([min(255, c * 255 + tolerance) for c in rgb])

    # 检查四个顶点的颜色是否匹配
    for x, y in square_points:
        if not (0 <= x < image.shape[1] and 0 <= y < image.shape[0]):
            return False  # 顶点超出图像范围
        pixel_color = image[y, x]  # 注意 OpenCV 的坐标是 (y, x)
        if not (lower_bound <= pixel_color).all() or not (pixel_color <= upper_bound).all():
            return False  # 如果顶点颜色不匹配，返回 False

    return True  # 所有顶点颜色匹配



def get_part_position(image_path):
    """
    获取图像中每个颜色对应的最大连通区域的中心位置，并返回标号和位置列表。

    :param image_path: 输入图像文件路径。
    :return: [(label, (x, y))] 列表，其中 label 是颜色序号，(x, y) 是对应最大连通区域的中心坐标。
    """
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("无法读取图像，请检查路径是否正确！")
    
    # 转换为 RGB 格式
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    labels_positions = []

    # 遍历 color_list 中的每种颜色
    for color_dict in color_list:
        label = color_dict["label"]
        rgb = color_dict["rgb"]

        # 将颜色值从 [0, 1] 转换为 [0, 255]
        rgb_scaled = tuple(int(c * 255) for c in rgb)

        # 创建掩码，找到与目标颜色相近的区域
        lower_bound = np.array(rgb_scaled) - 20  # 颜色下界 (容差20)
        upper_bound = np.array(rgb_scaled) + 20  # 颜色上界 (容差20)
        mask = cv2.inRange(image_rgb, lower_bound, upper_bound)

        # 寻找连通区域
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 如果找到连通区域，选择最大的区域
        max_area = 0
        max_center = None
        for contour in contours:
            area = cv2.contourArea(contour)  # 计算连通区域面积
            if area > max_area:  # 保留最大的连通区域
                max_area = area
                M = cv2.moments(contour)  # 计算图像矩
                if M["m00"] > 0:  # 确保面积非零
                    cx = int(M["m10"] / M["m00"])  # 计算重心 x 坐标
                    cy = int(M["m01"] / M["m00"])  # 计算重心 y 坐标

                    # 检查正方形是否完全在区域内
                    if is_square_color_match(image_rgb, (cx, cy), rgb, side_length=15, tolerance=20):
                        max_center = (cx, cy)  # 如果满足要求，直接使用
                    else:
                        # 从 mask 中随机选择像素点
                        mask_indices = np.transpose(np.nonzero(mask))  # 获取所有非零点坐标
                        random.shuffle(mask_indices)  # 随机打乱坐标
                        for point in mask_indices:
                            px, py = point[1], point[0]  # OpenCV 的坐标顺序为 (y, x)
                            if is_square_color_match(image_rgb, (px, py), rgb, side_length=15, tolerance=20):
                                max_center = (px, py)
                                break  # 找到满足要求的点后退出

        # 如果找到有效的最大区域中心，则记录
        if max_center:
            labels_positions.append((label, max_center))

    return labels_positions


def add_labels_to_image(labels_positions, image_path, output_path, font_path="arial.ttf", font_size=20):
    """
    在图片指定位置添加标号。
    
    :param labels_positions: 标号和位置列表，每项是 (label, (x, y))，表示标号及其在图像上的位置。
    :param image_path: 输入图像文件路径。
    :param output_path: 输出带标号的图像文件路径。
    :param font_path: 字体文件路径（默认为 Arial 字体）。
    :param font_size: 字号大小。
    """
    # 打开输入图像
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # 尝试加载字体
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("指定字体文件未找到，使用默认字体！")
        font = ImageFont.load_default()

    # 遍历标号和位置，在图像上绘制标号
    for label, position in labels_positions:
        x, y = position  # 提取位置坐标

        # 获取对应的标号颜色
        label_color = next((c["label_color"] for c in color_list if c["label"] == label), (255, 255, 255))

        # 绘制标号
        draw.text((x, y), str(label), fill=label_color, font=font)

    # 保存修改后的图像
    image.save(output_path)


if __name__ == '__main__':
    image_path = r"D:\project\CADComment\DeepCADProcess\dataset\cad_sequence\0000\00004956\images_with_color_and_label\back_top_right.png"
    output_path = r"D:\project\CADComment\DeepCADProcess\utils\demo.png"
    labels_positions = get_part_position(image_path)
    add_labels_to_image(labels_positions, image_path, output_path)
    