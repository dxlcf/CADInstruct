import numpy as np

# 基准平面方向定义
BASE_PlANE = {
    "XY": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],      # xDir: +x, yDir: +y, zDir: +z
    "YZ": [[0, 1, 0], [0, 0, 1], [1, 0, 0]],      # xDir: +y, yDir: +z, zDir: +x
    "ZX": [[0, 0, 1], [1, 0, 0], [0, 1, 0]],      # xDir: +z, yDir: +x, zDir: +y
    "XZ": [[1, 0, 0], [0, 0, 1], [0, -1, 0]],     # xDir: +x, yDir: +z, zDir: -y
    "YX": [[0, 1, 0], [1, 0, 0], [0, 0, -1]],     # xDir: +y, yDir: +x, zDir: -z
    "ZY": [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],     # xDir: +z, yDir: +y, zDir: -x
    "front": [[0, 0, 1], [1, 0, 0], [0, 1, 0]],   # xDir: +z, yDir: +x, zDir: +y
    "back": [[-1, 0, 0], [0, 1, 0], [0, 0, -1]],  # xDir: -x, yDir: +y, zDir: -z
    "left": [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],   # xDir: +z, yDir: +y, zDir: -x
    "right": [[0, 0, -1], [0, 1, 0], [1, 0, 0]],  # xDir: -z, yDir: +y, zDir: +x
    "top": [[1, 0, 0], [0, -1, 0], [0, 0, 1]],    # xDir: +x, yDir: -z, zDir: +y
    "bottom": [[1, 0, 0], [0, -1, 0], [0, 0, -1]] # xDir: +x, yDir: -z, zDir: -y
}

# 定义所有可能的命令
ALL_COMMANDS = ['Line', 'Arc', 'Circle', 'EOS', 'SOL', 'Ext']
# 为每个命令分配索引
LINE_IDX = ALL_COMMANDS.index('Line')
ARC_IDX = ALL_COMMANDS.index('Arc')
CIRCLE_IDX = ALL_COMMANDS.index('Circle')
EOS_IDX = ALL_COMMANDS.index('EOS')  # EOS: End of Sequence
SOL_IDX = ALL_COMMANDS.index('SOL')  # SOL: Start of Loop
EXT_IDX = ALL_COMMANDS.index('Ext')  # Ext: Extrude

# 定义拉伸操作类型
EXTRUDE_OPERATIONS = ["NewBodyFeatureOperation", "JoinFeatureOperation",
                      "CutFeatureOperation", "IntersectFeatureOperation"]
# 定义拉伸范围类型
EXTENT_TYPE = ["OneSideFeatureExtentType", "SymmetricFeatureExtentType",
               "TwoSidesFeatureExtentType"]

PAD_VAL = -1  # 填充值，用于向量表示中的空白位置

# 定义各种参数的数量
N_ARGS_SKETCH = 5  # 草图参数：x, y, alpha, f, r
N_ARGS_PLANE = 3   # 草图平面方向：theta, phi, gamma
N_ARGS_TRANS = 4   # 草图平面原点 + 草图缩放比例：p_x, p_y, p_z, s
N_ARGS_EXT_PARAM = 4  # 拉伸参数：e1, e2, b, u
N_ARGS_EXT = N_ARGS_PLANE + N_ARGS_TRANS + N_ARGS_EXT_PARAM  # 拉伸总参数数量
N_ARGS = N_ARGS_SKETCH + N_ARGS_EXT  # 总参数数量

# 定义特殊向量
SOL_VEC = np.array([SOL_IDX, *([PAD_VAL] * N_ARGS)])  # 循环开始向量
EOS_VEC = np.array([EOS_IDX, *([PAD_VAL] * N_ARGS)])  # 序列结束向量

# 定义命令参数掩码，用于指示每个命令使用哪些参数
CMD_ARGS_MASK = np.array([[1, 1, 0, 0, 0, *[0]*N_ARGS_EXT],  # 直线
                          [1, 1, 1, 1, 0, *[0]*N_ARGS_EXT],  # 圆弧
                          [1, 1, 0, 0, 1, *[0]*N_ARGS_EXT],  # 圆
                          [0, 0, 0, 0, 0, *[0]*N_ARGS_EXT],  # EOS
                          [0, 0, 0, 0, 0, *[0]*N_ARGS_EXT],  # SOL
                          [*[0]*N_ARGS_SKETCH, *[1]*N_ARGS_EXT]]) # 拉伸

NORM_FACTOR = 0.75  # 归一化缩放因子，用于防止增强过程中的溢出

MAX_N_EXT = 10     # 最大拉伸次数
MAX_N_LOOPS = 6    # 每个草图的最大循环数
MAX_N_CURVES = 15  # 每个循环的最大曲线数
MAX_TOTAL_LEN = 60 # CAD序列的最大长度
ARGS_DIM = 256     # 参数维度
