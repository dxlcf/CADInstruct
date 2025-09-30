import cadquery as cq
from cadquery.selectors import DirectionSelector, NearestToPointSelector

profile_1 = (
    cq.Sketch()
    # loop_1_1
    .arc((5.958, 0.709), (5.977, 0.523), (5.991, 0.336), 'arc_1_1_1')
    .segment((6.975, 0.51), 'line_1_1_2')
    .segment((6.967, 0.61), 'line_1_1_3')
    .segment((6.958, 0.709), 'line_1_1_4')
    .segment((5.958, 0.709), 'line_1_1_5')
    .assemble()
)

profile_2 = (
    cq.Sketch()
    # loop_2_1
    .arc((5.873, 1.226), (5.909, 1.042), (5.938, 0.857), 'arc_2_1_1')
    .segment((6.904, 1.116), 'line_2_1_2')
    .segment((6.887, 1.214), 'line_2_1_3')
    .segment((6.87, 1.313), 'line_2_1_4')
    .segment((5.873, 1.226), 'line_2_1_5')
    .assemble()
)

profile_3 = (
    cq.Sketch()
    # loop_3_1
    .arc((5.744, 1.733), (5.796, 1.553), (5.841, 1.371), 'arc_3_1_1')
    .segment((6.781, 1.713), 'line_3_1_2')
    .segment((6.755, 1.81), 'line_3_1_3')
    .segment((6.729, 1.907), 'line_3_1_4')
    .segment((5.744, 1.733), 'line_3_1_5')
    .assemble()
)

profile_4 = (
    cq.Sketch()
    # loop_4_1
    .arc((5.571, 2.227), (5.638, 2.052), (5.699, 1.875), 'arc_4_1_1')
    .segment((6.606, 2.298), 'line_4_1_2')
    .segment((6.572, 2.392), 'line_4_1_3')
    .segment((6.537, 2.486), 'line_4_1_4')
    .segment((5.571, 2.227), 'line_4_1_5')
    .assemble()
)

profile_5 = (
    cq.Sketch()
    # loop_5_1
    .arc((5.356, 2.704), (5.438, 2.536), (5.514, 2.365), 'arc_5_1_1')
    .segment((6.38, 2.865), 'line_5_1_2')
    .segment((6.338, 2.955), 'line_5_1_3')
    .segment((6.296, 3.046), 'line_5_1_4')
    .segment((5.356, 2.704), 'line_5_1_5')
    .assemble()
)

profile_6 = (
    cq.Sketch()
    # loop_6_1
    .arc((5.1, 3.161), (5.196, 3.0), (5.287, 2.836), 'arc_6_1_1')
    .segment((6.106, 3.41), 'line_6_1_2')
    .segment((6.056, 3.497), 'line_6_1_3')
    .segment((6.006, 3.583), 'line_6_1_4')
    .segment((5.1, 3.161), 'line_6_1_5')
    .assemble()
)

profile_7 = (
    cq.Sketch()
    # loop_7_1
    .arc((4.805, 3.593), (4.915, 3.441), (5.02, 3.286), 'arc_7_1_1')
    .segment((5.786, 3.929), 'line_7_1_2')
    .segment((5.729, 4.011), 'line_7_1_3')
    .segment((5.671, 4.093), 'line_7_1_4')
    .segment((4.805, 3.593), 'line_7_1_5')
    .assemble()
)

profile_8 = (
    cq.Sketch()
    # loop_8_1
    .arc((4.474, 3.998), (4.596, 3.857), (4.714, 3.711), 'arc_8_1_1')
    .segment((5.421, 4.419), 'line_8_1_2')
    .segment((5.357, 4.495), 'line_8_1_3')
    .segment((5.293, 4.572), 'line_8_1_4')
    .segment((4.474, 3.998), 'line_8_1_5')
    .assemble()
)

profile_9 = (
    cq.Sketch()
    # loop_9_1
    .arc((4.108, 4.373), (4.243, 4.243), (4.373, 4.108), 'arc_9_1_1')
    .segment((5.016, 4.874), 'line_9_1_2')
    .segment((4.945, 4.945), 'line_9_1_3')
    .segment((4.874, 5.016), 'line_9_1_4')
    .segment((4.108, 4.373), 'line_9_1_5')
    .assemble()
)

profile_10 = (
    cq.Sketch()
    # loop_10_1
    .arc((3.711, 4.714), (3.857, 4.596), (3.998, 4.474), 'arc_10_1_1')
    .segment((4.572, 5.293), 'line_10_1_2')
    .segment((4.495, 5.357), 'line_10_1_3')
    .segment((4.419, 5.421), 'line_10_1_4')
    .segment((3.711, 4.714), 'line_10_1_5')
    .assemble()
)

profile_11 = (
    cq.Sketch()
    # loop_11_1
    .arc((3.286, 5.02), (3.441, 4.915), (3.593, 4.805), 'arc_11_1_1')
    .segment((4.093, 5.671), 'line_11_1_2')
    .segment((4.011, 5.729), 'line_11_1_3')
    .segment((3.929, 5.786), 'line_11_1_4')
    .segment((3.286, 5.02), 'line_11_1_5')
    .assemble()
)

profile_12 = (
    cq.Sketch()
    # loop_12_1
    .arc((2.836, 5.287), (3.0, 5.196), (3.161, 5.1), 'arc_12_1_1')
    .segment((3.583, 6.006), 'line_12_1_2')
    .segment((3.497, 6.056), 'line_12_1_3')
    .segment((3.41, 6.106), 'line_12_1_4')
    .segment((2.836, 5.287), 'line_12_1_5')
    .assemble()
)

profile_13 = (
    cq.Sketch()
    # loop_13_1
    .arc((2.365, 5.514), (2.536, 5.438), (2.704, 5.356), 'arc_13_1_1')
    .segment((3.046, 6.296), 'line_13_1_2')
    .segment((2.955, 6.338), 'line_13_1_3')
    .segment((2.865, 6.38), 'line_13_1_4')
    .segment((2.365, 5.514), 'line_13_1_5')
    .assemble()
)

profile_14 = (
    cq.Sketch()
    # loop_14_1
    .arc((1.875, 5.699), (2.052, 5.638), (2.227, 5.571), 'arc_14_1_1')
    .segment((2.486, 6.537), 'line_14_1_2')
    .segment((2.392, 6.572), 'line_14_1_3')
    .segment((2.298, 6.606), 'line_14_1_4')
    .segment((1.875, 5.699), 'line_14_1_5')
    .assemble()
)

profile_15 = (
    cq.Sketch()
    # loop_15_1
    .arc((1.371, 5.841), (1.553, 5.796), (1.733, 5.744), 'arc_15_1_1')
    .segment((1.907, 6.729), 'line_15_1_2')
    .segment((1.81, 6.755), 'line_15_1_3')
    .segment((1.713, 6.781), 'line_15_1_4')
    .segment((1.371, 5.841), 'line_15_1_5')
    .assemble()
)

profile_16 = (
    cq.Sketch()
    # loop_16_1
    .arc((0.857, 5.938), (1.042, 5.909), (1.226, 5.873), 'arc_16_1_1')
    .segment((1.313, 6.87), 'line_16_1_2')
    .segment((1.214, 6.887), 'line_16_1_3')
    .segment((1.116, 6.904), 'line_16_1_4')
    .segment((0.857, 5.938), 'line_16_1_5')
    .assemble()
)

profile_17 = (
    cq.Sketch()
    # loop_17_1
    .arc((0.336, 5.991), (0.523, 5.977), (0.709, 5.958), 'arc_17_1_1')
    .segment((0.709, 6.958), 'line_17_1_2')
    .segment((0.61, 6.967), 'line_17_1_3')
    .segment((0.51, 6.975), 'line_17_1_4')
    .segment((0.336, 5.991), 'line_17_1_5')
    .assemble()
)

profile_18 = (
    cq.Sketch()
    # loop_18_1
    .arc((-0.187, 5.997), (0.0, 6.0), (0.187, 5.997), 'arc_18_1_1')
    .segment((0.1, 6.993), 'line_18_1_2')
    .segment((0.0, 6.993), 'line_18_1_3')
    .segment((-0.1, 6.993), 'line_18_1_4')
    .segment((-0.187, 5.997), 'line_18_1_5')
    .assemble()
)

profile_19 = (
    cq.Sketch()
    # loop_19_1
    .arc((-0.709, 5.958), (-0.523, 5.977), (-0.336, 5.991), 'arc_19_1_1')
    .segment((-0.51, 6.975), 'line_19_1_2')
    .segment((-0.61, 6.967), 'line_19_1_3')
    .segment((-0.709, 6.958), 'line_19_1_4')
    .segment((-0.709, 5.958), 'line_19_1_5')
    .assemble()
)

profile_20 = (
    cq.Sketch()
    # loop_20_1
    .segment((-1.313, 6.87), (-1.226, 5.873), 'line_20_1_1')
    .arc((-1.042, 5.909), (-0.857, 5.938), 'arc_20_1_2')
    .segment((-1.116, 6.904), 'line_20_1_3')
    .segment((-1.214, 6.887), 'line_20_1_4')
    .segment((-1.313, 6.87), 'line_20_1_5')
    .assemble()
)

profile_21 = (
    cq.Sketch()
    # loop_21_1
    .segment((-1.907, 6.729), (-1.733, 5.744), 'line_21_1_1')
    .arc((-1.553, 5.796), (-1.371, 5.841), 'arc_21_1_2')
    .segment((-1.713, 6.781), 'line_21_1_3')
    .segment((-1.81, 6.755), 'line_21_1_4')
    .segment((-1.907, 6.729), 'line_21_1_5')
    .assemble()
)

profile_22 = (
    cq.Sketch()
    # loop_22_1
    .segment((-2.486, 6.537), (-2.227, 5.571), 'line_22_1_1')
    .arc((-2.052, 5.638), (-1.875, 5.699), 'arc_22_1_2')
    .segment((-2.298, 6.606), 'line_22_1_3')
    .segment((-2.392, 6.572), 'line_22_1_4')
    .segment((-2.486, 6.537), 'line_22_1_5')
    .assemble()
)

profile_23 = (
    cq.Sketch()
    # loop_23_1
    .segment((-3.046, 6.296), (-2.704, 5.356), 'line_23_1_1')
    .arc((-2.536, 5.438), (-2.365, 5.514), 'arc_23_1_2')
    .segment((-2.865, 6.38), 'line_23_1_3')
    .segment((-2.955, 6.338), 'line_23_1_4')
    .segment((-3.046, 6.296), 'line_23_1_5')
    .assemble()
)

profile_24 = (
    cq.Sketch()
    # loop_24_1
    .segment((-3.583, 6.006), (-3.161, 5.1), 'line_24_1_1')
    .arc((-3.0, 5.196), (-2.836, 5.287), 'arc_24_1_2')
    .segment((-3.41, 6.106), 'line_24_1_3')
    .segment((-3.497, 6.056), 'line_24_1_4')
    .segment((-3.583, 6.006), 'line_24_1_5')
    .assemble()
)

profile_25 = (
    cq.Sketch()
    # loop_25_1
    .segment((-4.093, 5.671), (-3.593, 4.805), 'line_25_1_1')
    .arc((-3.441, 4.915), (-3.286, 5.02), 'arc_25_1_2')
    .segment((-3.929, 5.786), 'line_25_1_3')
    .segment((-4.011, 5.729), 'line_25_1_4')
    .segment((-4.093, 5.671), 'line_25_1_5')
    .assemble()
)

profile_26 = (
    cq.Sketch()
    # loop_26_1
    .segment((-4.572, 5.293), (-3.998, 4.474), 'line_26_1_1')
    .arc((-3.857, 4.596), (-3.711, 4.714), 'arc_26_1_2')
    .segment((-4.419, 5.421), 'line_26_1_3')
    .segment((-4.495, 5.357), 'line_26_1_4')
    .segment((-4.572, 5.293), 'line_26_1_5')
    .assemble()
)

profile_27 = (
    cq.Sketch()
    # loop_27_1
    .segment((-5.016, 4.874), (-4.373, 4.108), 'line_27_1_1')
    .arc((-4.243, 4.243), (-4.108, 4.373), 'arc_27_1_2')
    .segment((-4.874, 5.016), 'line_27_1_3')
    .segment((-4.945, 4.945), 'line_27_1_4')
    .segment((-5.016, 4.874), 'line_27_1_5')
    .assemble()
)

profile_28 = (
    cq.Sketch()
    # loop_28_1
    .segment((-5.421, 4.419), (-4.714, 3.711), 'line_28_1_1')
    .arc((-4.596, 3.857), (-4.474, 3.998), 'arc_28_1_2')
    .segment((-5.293, 4.572), 'line_28_1_3')
    .segment((-5.357, 4.495), 'line_28_1_4')
    .segment((-5.421, 4.419), 'line_28_1_5')
    .assemble()
)

profile_29 = (
    cq.Sketch()
    # loop_29_1
    .segment((-5.786, 3.929), (-5.02, 3.286), 'line_29_1_1')
    .arc((-4.915, 3.441), (-4.805, 3.593), 'arc_29_1_2')
    .segment((-5.671, 4.093), 'line_29_1_3')
    .segment((-5.729, 4.011), 'line_29_1_4')
    .segment((-5.786, 3.929), 'line_29_1_5')
    .assemble()
)

profile_30 = (
    cq.Sketch()
    # loop_30_1
    .segment((-6.106, 3.41), (-5.287, 2.836), 'line_30_1_1')
    .arc((-5.196, 3.0), (-5.1, 3.161), 'arc_30_1_2')
    .segment((-6.006, 3.583), 'line_30_1_3')
    .segment((-6.056, 3.497), 'line_30_1_4')
    .segment((-6.106, 3.41), 'line_30_1_5')
    .assemble()
)

profile_31 = (
    cq.Sketch()
    # loop_31_1
    .segment((-6.38, 2.865), (-5.514, 2.365), 'line_31_1_1')
    .arc((-5.438, 2.536), (-5.356, 2.704), 'arc_31_1_2')
    .segment((-6.296, 3.046), 'line_31_1_3')
    .segment((-6.338, 2.955), 'line_31_1_4')
    .segment((-6.38, 2.865), 'line_31_1_5')
    .assemble()
)

profile_32 = (
    cq.Sketch()
    # loop_32_1
    .segment((-6.606, 2.298), (-5.699, 1.875), 'line_32_1_1')
    .arc((-5.638, 2.052), (-5.571, 2.227), 'arc_32_1_2')
    .segment((-6.537, 2.486), 'line_32_1_3')
    .segment((-6.572, 2.392), 'line_32_1_4')
    .segment((-6.606, 2.298), 'line_32_1_5')
    .assemble()
)

profile_33 = (
    cq.Sketch()
    # loop_33_1
    .segment((-6.781, 1.713), (-5.841, 1.371), 'line_33_1_1')
    .arc((-5.796, 1.553), (-5.744, 1.733), 'arc_33_1_2')
    .segment((-6.729, 1.907), 'line_33_1_3')
    .segment((-6.755, 1.81), 'line_33_1_4')
    .segment((-6.781, 1.713), 'line_33_1_5')
    .assemble()
)

profile_34 = (
    cq.Sketch()
    # loop_34_1
    .segment((-6.904, 1.116), (-5.938, 0.857), 'line_34_1_1')
    .arc((-5.909, 1.042), (-5.873, 1.226), 'arc_34_1_2')
    .segment((-6.87, 1.313), 'line_34_1_3')
    .segment((-6.887, 1.214), 'line_34_1_4')
    .segment((-6.904, 1.116), 'line_34_1_5')
    .assemble()
)

profile_35 = (
    cq.Sketch()
    # loop_35_1
    .segment((-6.975, 0.51), (-5.991, 0.336), 'line_35_1_1')
    .arc((-5.977, 0.523), (-5.958, 0.709), 'arc_35_1_2')
    .segment((-6.958, 0.709), 'line_35_1_3')
    .segment((-6.967, 0.61), 'line_35_1_4')
    .segment((-6.975, 0.51), 'line_35_1_5')
    .assemble()
)

profile_36 = (
    cq.Sketch()
    # loop_36_1
    .segment((-6.993, -0.1), (-5.997, -0.187), 'line_36_1_1')
    .arc((-6.0, 0.0), (-5.997, 0.187), 'arc_36_1_2')
    .segment((-6.993, 0.1), 'line_36_1_3')
    .segment((-6.993, 0.0), 'line_36_1_4')
    .segment((-6.993, -0.1), 'line_36_1_5')
    .assemble()
)

profile_37 = (
    cq.Sketch()
    # loop_37_1
    .segment((-6.975, -0.51), (-6.967, -0.61), 'line_37_1_1')
    .segment((-6.958, -0.709), 'line_37_1_2')
    .segment((-5.958, -0.709), 'line_37_1_3')
    .arc((-5.977, -0.523), (-5.991, -0.336), 'arc_37_1_4')
    .segment((-6.975, -0.51), 'line_37_1_5')
    .assemble()
)

profile_38 = (
    cq.Sketch()
    # loop_38_1
    .segment((-6.904, -1.116), (-6.887, -1.214), 'line_38_1_1')
    .segment((-6.87, -1.313), 'line_38_1_2')
    .segment((-5.873, -1.226), 'line_38_1_3')
    .arc((-5.909, -1.042), (-5.938, -0.857), 'arc_38_1_4')
    .segment((-6.904, -1.116), 'line_38_1_5')
    .assemble()
)

profile_39 = (
    cq.Sketch()
    # loop_39_1
    .segment((-6.781, -1.713), (-6.755, -1.81), 'line_39_1_1')
    .segment((-6.729, -1.907), 'line_39_1_2')
    .segment((-5.744, -1.733), 'line_39_1_3')
    .arc((-5.796, -1.553), (-5.841, -1.371), 'arc_39_1_4')
    .segment((-6.781, -1.713), 'line_39_1_5')
    .assemble()
)

profile_40 = (
    cq.Sketch()
    # loop_40_1
    .segment((-6.606, -2.298), (-6.572, -2.392), 'line_40_1_1')
    .segment((-6.537, -2.486), 'line_40_1_2')
    .segment((-5.571, -2.227), 'line_40_1_3')
    .arc((-5.638, -2.052), (-5.699, -1.875), 'arc_40_1_4')
    .segment((-6.606, -2.298), 'line_40_1_5')
    .assemble()
)

profile_41 = (
    cq.Sketch()
    # loop_41_1
    .segment((-6.38, -2.865), (-6.338, -2.955), 'line_41_1_1')
    .segment((-6.296, -3.046), 'line_41_1_2')
    .segment((-5.356, -2.704), 'line_41_1_3')
    .arc((-5.438, -2.536), (-5.514, -2.365), 'arc_41_1_4')
    .segment((-6.38, -2.865), 'line_41_1_5')
    .assemble()
)

profile_42 = (
    cq.Sketch()
    # loop_42_1
    .segment((-6.106, -3.41), (-6.056, -3.497), 'line_42_1_1')
    .segment((-6.006, -3.583), 'line_42_1_2')
    .segment((-5.1, -3.161), 'line_42_1_3')
    .arc((-5.196, -3.0), (-5.287, -2.836), 'arc_42_1_4')
    .segment((-6.106, -3.41), 'line_42_1_5')
    .assemble()
)

profile_43 = (
    cq.Sketch()
    # loop_43_1
    .segment((-5.786, -3.929), (-5.729, -4.011), 'line_43_1_1')
    .segment((-5.671, -4.093), 'line_43_1_2')
    .segment((-4.805, -3.593), 'line_43_1_3')
    .arc((-4.915, -3.441), (-5.02, -3.286), 'arc_43_1_4')
    .segment((-5.786, -3.929), 'line_43_1_5')
    .assemble()
)

profile_44 = (
    cq.Sketch()
    # loop_44_1
    .segment((-5.421, -4.419), (-5.357, -4.495), 'line_44_1_1')
    .segment((-5.293, -4.572), 'line_44_1_2')
    .segment((-4.474, -3.998), 'line_44_1_3')
    .arc((-4.596, -3.857), (-4.714, -3.711), 'arc_44_1_4')
    .segment((-5.421, -4.419), 'line_44_1_5')
    .assemble()
)

profile_45 = (
    cq.Sketch()
    # loop_45_1
    .segment((-5.016, -4.874), (-4.945, -4.945), 'line_45_1_1')
    .segment((-4.874, -5.016), 'line_45_1_2')
    .segment((-4.108, -4.373), 'line_45_1_3')
    .arc((-4.243, -4.243), (-4.373, -4.108), 'arc_45_1_4')
    .segment((-5.016, -4.874), 'line_45_1_5')
    .assemble()
)

profile_46 = (
    cq.Sketch()
    # loop_46_1
    .segment((-4.572, -5.293), (-4.495, -5.357), 'line_46_1_1')
    .segment((-4.419, -5.421), 'line_46_1_2')
    .segment((-3.711, -4.714), 'line_46_1_3')
    .arc((-3.857, -4.596), (-3.998, -4.474), 'arc_46_1_4')
    .segment((-4.572, -5.293), 'line_46_1_5')
    .assemble()
)

profile_47 = (
    cq.Sketch()
    # loop_47_1
    .segment((-4.093, -5.671), (-4.011, -5.729), 'line_47_1_1')
    .segment((-3.929, -5.786), 'line_47_1_2')
    .segment((-3.286, -5.02), 'line_47_1_3')
    .arc((-3.441, -4.915), (-3.593, -4.805), 'arc_47_1_4')
    .segment((-4.093, -5.671), 'line_47_1_5')
    .assemble()
)

profile_48 = (
    cq.Sketch()
    # loop_48_1
    .segment((-3.583, -6.006), (-3.497, -6.056), 'line_48_1_1')
    .segment((-3.41, -6.106), 'line_48_1_2')
    .segment((-2.836, -5.287), 'line_48_1_3')
    .arc((-3.0, -5.196), (-3.161, -5.1), 'arc_48_1_4')
    .segment((-3.583, -6.006), 'line_48_1_5')
    .assemble()
)

profile_49 = (
    cq.Sketch()
    # loop_49_1
    .segment((-3.046, -6.296), (-2.955, -6.338), 'line_49_1_1')
    .segment((-2.865, -6.38), 'line_49_1_2')
    .segment((-2.365, -5.514), 'line_49_1_3')
    .arc((-2.536, -5.438), (-2.704, -5.356), 'arc_49_1_4')
    .segment((-3.046, -6.296), 'line_49_1_5')
    .assemble()
)

profile_50 = (
    cq.Sketch()
    # loop_50_1
    .segment((-2.486, -6.537), (-2.392, -6.572), 'line_50_1_1')
    .segment((-2.298, -6.606), 'line_50_1_2')
    .segment((-1.875, -5.699), 'line_50_1_3')
    .arc((-2.052, -5.638), (-2.227, -5.571), 'arc_50_1_4')
    .segment((-2.486, -6.537), 'line_50_1_5')
    .assemble()
)

profile_51 = (
    cq.Sketch()
    # loop_51_1
    .segment((-1.907, -6.729), (-1.81, -6.755), 'line_51_1_1')
    .segment((-1.713, -6.781), 'line_51_1_2')
    .segment((-1.371, -5.841), 'line_51_1_3')
    .arc((-1.553, -5.796), (-1.733, -5.744), 'arc_51_1_4')
    .segment((-1.907, -6.729), 'line_51_1_5')
    .assemble()
)

profile_52 = (
    cq.Sketch()
    # loop_52_1
    .segment((-1.313, -6.87), (-1.214, -6.887), 'line_52_1_1')
    .segment((-1.116, -6.904), 'line_52_1_2')
    .segment((-0.857, -5.938), 'line_52_1_3')
    .arc((-1.042, -5.909), (-1.226, -5.873), 'arc_52_1_4')
    .segment((-1.313, -6.87), 'line_52_1_5')
    .assemble()
)

profile_53 = (
    cq.Sketch()
    # loop_53_1
    .segment((-0.709, -6.958), (-0.61, -6.967), 'line_53_1_1')
    .segment((-0.51, -6.975), 'line_53_1_2')
    .segment((-0.336, -5.991), 'line_53_1_3')
    .arc((-0.523, -5.977), (-0.709, -5.958), 'arc_53_1_4')
    .segment((-0.709, -6.958), 'line_53_1_5')
    .assemble()
)

profile_54 = (
    cq.Sketch()
    # loop_54_1
    .segment((-0.187, -5.997), (-0.1, -6.993), 'line_54_1_1')
    .segment((0.0, -6.993), 'line_54_1_2')
    .segment((0.1, -6.993), 'line_54_1_3')
    .segment((0.187, -5.997), 'line_54_1_4')
    .arc((0.0, -6.0), (-0.187, -5.997), 'arc_54_1_5')
    .assemble()
)

profile_55 = (
    cq.Sketch()
    # loop_55_1
    .segment((0.336, -5.991), (0.51, -6.975), 'line_55_1_1')
    .segment((0.61, -6.967), 'line_55_1_2')
    .segment((0.709, -6.958), 'line_55_1_3')
    .segment((0.709, -5.958), 'line_55_1_4')
    .arc((0.523, -5.977), (0.336, -5.991), 'arc_55_1_5')
    .assemble()
)

profile_56 = (
    cq.Sketch()
    # loop_56_1
    .segment((0.857, -5.938), (1.116, -6.904), 'line_56_1_1')
    .segment((1.214, -6.887), 'line_56_1_2')
    .segment((1.313, -6.87), 'line_56_1_3')
    .segment((1.226, -5.873), 'line_56_1_4')
    .arc((1.042, -5.909), (0.857, -5.938), 'arc_56_1_5')
    .assemble()
)

profile_57 = (
    cq.Sketch()
    # loop_57_1
    .segment((1.371, -5.841), (1.713, -6.781), 'line_57_1_1')
    .segment((1.81, -6.755), 'line_57_1_2')
    .segment((1.907, -6.729), 'line_57_1_3')
    .segment((1.733, -5.744), 'line_57_1_4')
    .arc((1.553, -5.796), (1.371, -5.841), 'arc_57_1_5')
    .assemble()
)

profile_58 = (
    cq.Sketch()
    # loop_58_1
    .segment((1.875, -5.699), (2.298, -6.606), 'line_58_1_1')
    .segment((2.392, -6.572), 'line_58_1_2')
    .segment((2.486, -6.537), 'line_58_1_3')
    .segment((2.227, -5.571), 'line_58_1_4')
    .arc((2.052, -5.638), (1.875, -5.699), 'arc_58_1_5')
    .assemble()
)

profile_59 = (
    cq.Sketch()
    # loop_59_1
    .segment((2.365, -5.514), (2.865, -6.38), 'line_59_1_1')
    .segment((2.955, -6.338), 'line_59_1_2')
    .segment((3.046, -6.296), 'line_59_1_3')
    .segment((2.704, -5.356), 'line_59_1_4')
    .arc((2.536, -5.438), (2.365, -5.514), 'arc_59_1_5')
    .assemble()
)

profile_60 = (
    cq.Sketch()
    # loop_60_1
    .segment((2.836, -5.287), (3.41, -6.106), 'line_60_1_1')
    .segment((3.497, -6.056), 'line_60_1_2')
    .segment((3.583, -6.006), 'line_60_1_3')
    .segment((3.161, -5.1), 'line_60_1_4')
    .arc((3.0, -5.196), (2.836, -5.287), 'arc_60_1_5')
    .assemble()
)

profile_61 = (
    cq.Sketch()
    # loop_61_1
    .segment((3.286, -5.02), (3.929, -5.786), 'line_61_1_1')
    .segment((4.011, -5.729), 'line_61_1_2')
    .segment((4.093, -5.671), 'line_61_1_3')
    .segment((3.593, -4.805), 'line_61_1_4')
    .arc((3.441, -4.915), (3.286, -5.02), 'arc_61_1_5')
    .assemble()
)

profile_62 = (
    cq.Sketch()
    # loop_62_1
    .segment((3.711, -4.714), (4.419, -5.421), 'line_62_1_1')
    .segment((4.495, -5.357), 'line_62_1_2')
    .segment((4.572, -5.293), 'line_62_1_3')
    .segment((3.998, -4.474), 'line_62_1_4')
    .arc((3.857, -4.596), (3.711, -4.714), 'arc_62_1_5')
    .assemble()
)

profile_63 = (
    cq.Sketch()
    # loop_63_1
    .segment((4.108, -4.373), (4.874, -5.016), 'line_63_1_1')
    .segment((4.945, -4.945), 'line_63_1_2')
    .segment((5.016, -4.874), 'line_63_1_3')
    .segment((4.373, -4.108), 'line_63_1_4')
    .arc((4.243, -4.243), (4.108, -4.373), 'arc_63_1_5')
    .assemble()
)

profile_64 = (
    cq.Sketch()
    # loop_64_1
    .segment((4.474, -3.998), (5.293, -4.572), 'line_64_1_1')
    .segment((5.357, -4.495), 'line_64_1_2')
    .segment((5.421, -4.419), 'line_64_1_3')
    .segment((4.714, -3.711), 'line_64_1_4')
    .arc((4.596, -3.857), (4.474, -3.998), 'arc_64_1_5')
    .assemble()
)

profile_65 = (
    cq.Sketch()
    # loop_65_1
    .segment((4.805, -3.593), (5.671, -4.093), 'line_65_1_1')
    .segment((5.729, -4.011), 'line_65_1_2')
    .segment((5.786, -3.929), 'line_65_1_3')
    .segment((5.02, -3.286), 'line_65_1_4')
    .arc((4.915, -3.441), (4.805, -3.593), 'arc_65_1_5')
    .assemble()
)

profile_66 = (
    cq.Sketch()
    # loop_66_1
    .segment((5.1, -3.161), (6.006, -3.583), 'line_66_1_1')
    .segment((6.056, -3.497), 'line_66_1_2')
    .segment((6.106, -3.41), 'line_66_1_3')
    .segment((5.287, -2.836), 'line_66_1_4')
    .arc((5.196, -3.0), (5.1, -3.161), 'arc_66_1_5')
    .assemble()
)

profile_67 = (
    cq.Sketch()
    # loop_67_1
    .segment((5.356, -2.704), (6.296, -3.046), 'line_67_1_1')
    .segment((6.338, -2.955), 'line_67_1_2')
    .segment((6.38, -2.865), 'line_67_1_3')
    .segment((5.514, -2.365), 'line_67_1_4')
    .arc((5.438, -2.536), (5.356, -2.704), 'arc_67_1_5')
    .assemble()
)

profile_68 = (
    cq.Sketch()
    # loop_68_1
    .segment((5.571, -2.227), (6.537, -2.486), 'line_68_1_1')
    .segment((6.572, -2.392), 'line_68_1_2')
    .segment((6.606, -2.298), 'line_68_1_3')
    .segment((5.699, -1.875), 'line_68_1_4')
    .arc((5.638, -2.052), (5.571, -2.227), 'arc_68_1_5')
    .assemble()
)

profile_69 = (
    cq.Sketch()
    # loop_69_1
    .segment((5.744, -1.733), (6.729, -1.907), 'line_69_1_1')
    .segment((6.755, -1.81), 'line_69_1_2')
    .segment((6.781, -1.713), 'line_69_1_3')
    .segment((5.841, -1.371), 'line_69_1_4')
    .arc((5.796, -1.553), (5.744, -1.733), 'arc_69_1_5')
    .assemble()
)

profile_70 = (
    cq.Sketch()
    # loop_70_1
    .segment((5.873, -1.226), (6.87, -1.313), 'line_70_1_1')
    .segment((6.887, -1.214), 'line_70_1_2')
    .segment((6.904, -1.116), 'line_70_1_3')
    .segment((5.938, -0.857), 'line_70_1_4')
    .arc((5.909, -1.042), (5.873, -1.226), 'arc_70_1_5')
    .assemble()
)

profile_71 = (
    cq.Sketch()
    # loop_71_1
    .segment((5.958, -0.709), (6.958, -0.709), 'line_71_1_1')
    .segment((6.967, -0.61), 'line_71_1_2')
    .segment((6.975, -0.51), 'line_71_1_3')
    .segment((5.991, -0.336), 'line_71_1_4')
    .arc((5.977, -0.523), (5.958, -0.709), 'arc_71_1_5')
    .assemble()
)

profile_72 = (
    cq.Sketch()
    # loop_72_1
    .segment((5.997, -0.187), (6.993, -0.1), 'line_72_1_1')
    .segment((6.993, 0.0), 'line_72_1_2')
    .segment((6.993, 0.1), 'line_72_1_3')
    .segment((5.997, 0.187), 'line_72_1_4')
    .arc((6.0, 0.0), (5.997, -0.187), 'arc_72_1_5')
    .assemble()
)

profile_73 = (
    cq.Sketch()
    # loop_73_1
    .arc((0.0, 0.0), 6.0, 0.0, 360.0, 'circle_73_1_1')
    .assemble()
)

sketch_1 = profile_1
sketch_1 = sketch_1.face(profile_2, mode='a')
sketch_1 = sketch_1.face(profile_3, mode='a')
sketch_1 = sketch_1.face(profile_4, mode='a')
sketch_1 = sketch_1.face(profile_5, mode='a')
sketch_1 = sketch_1.face(profile_6, mode='a')
sketch_1 = sketch_1.face(profile_7, mode='a')
sketch_1 = sketch_1.face(profile_8, mode='a')
sketch_1 = sketch_1.face(profile_9, mode='a')
sketch_1 = sketch_1.face(profile_10, mode='a')
sketch_1 = sketch_1.face(profile_11, mode='a')
sketch_1 = sketch_1.face(profile_12, mode='a')
sketch_1 = sketch_1.face(profile_13, mode='a')
sketch_1 = sketch_1.face(profile_14, mode='a')
sketch_1 = sketch_1.face(profile_15, mode='a')
sketch_1 = sketch_1.face(profile_16, mode='a')
sketch_1 = sketch_1.face(profile_17, mode='a')
sketch_1 = sketch_1.face(profile_18, mode='a')
sketch_1 = sketch_1.face(profile_19, mode='a')
sketch_1 = sketch_1.face(profile_20, mode='a')
sketch_1 = sketch_1.face(profile_21, mode='a')
sketch_1 = sketch_1.face(profile_22, mode='a')
sketch_1 = sketch_1.face(profile_23, mode='a')
sketch_1 = sketch_1.face(profile_24, mode='a')
sketch_1 = sketch_1.face(profile_25, mode='a')
sketch_1 = sketch_1.face(profile_26, mode='a')
sketch_1 = sketch_1.face(profile_27, mode='a')
sketch_1 = sketch_1.face(profile_28, mode='a')
sketch_1 = sketch_1.face(profile_29, mode='a')
sketch_1 = sketch_1.face(profile_30, mode='a')
sketch_1 = sketch_1.face(profile_31, mode='a')
sketch_1 = sketch_1.face(profile_32, mode='a')
sketch_1 = sketch_1.face(profile_33, mode='a')
sketch_1 = sketch_1.face(profile_34, mode='a')
sketch_1 = sketch_1.face(profile_35, mode='a')
sketch_1 = sketch_1.face(profile_36, mode='a')
sketch_1 = sketch_1.face(profile_37, mode='a')
sketch_1 = sketch_1.face(profile_38, mode='a')
sketch_1 = sketch_1.face(profile_39, mode='a')
sketch_1 = sketch_1.face(profile_40, mode='a')
sketch_1 = sketch_1.face(profile_41, mode='a')
sketch_1 = sketch_1.face(profile_42, mode='a')
sketch_1 = sketch_1.face(profile_43, mode='a')
sketch_1 = sketch_1.face(profile_44, mode='a')
sketch_1 = sketch_1.face(profile_45, mode='a')
sketch_1 = sketch_1.face(profile_46, mode='a')
sketch_1 = sketch_1.face(profile_47, mode='a')
sketch_1 = sketch_1.face(profile_48, mode='a')
sketch_1 = sketch_1.face(profile_49, mode='a')
sketch_1 = sketch_1.face(profile_50, mode='a')
sketch_1 = sketch_1.face(profile_51, mode='a')
sketch_1 = sketch_1.face(profile_52, mode='a')
sketch_1 = sketch_1.face(profile_53, mode='a')
sketch_1 = sketch_1.face(profile_54, mode='a')
sketch_1 = sketch_1.face(profile_55, mode='a')
sketch_1 = sketch_1.face(profile_56, mode='a')
sketch_1 = sketch_1.face(profile_57, mode='a')
sketch_1 = sketch_1.face(profile_58, mode='a')
sketch_1 = sketch_1.face(profile_59, mode='a')
sketch_1 = sketch_1.face(profile_60, mode='a')
sketch_1 = sketch_1.face(profile_61, mode='a')
sketch_1 = sketch_1.face(profile_62, mode='a')
sketch_1 = sketch_1.face(profile_63, mode='a')
sketch_1 = sketch_1.face(profile_64, mode='a')
sketch_1 = sketch_1.face(profile_65, mode='a')
sketch_1 = sketch_1.face(profile_66, mode='a')
sketch_1 = sketch_1.face(profile_67, mode='a')
sketch_1 = sketch_1.face(profile_68, mode='a')
sketch_1 = sketch_1.face(profile_69, mode='a')
sketch_1 = sketch_1.face(profile_70, mode='a')
sketch_1 = sketch_1.face(profile_71, mode='a')
sketch_1 = sketch_1.face(profile_72, mode='a')
sketch_1 = sketch_1.face(profile_73, mode='a')

extrude_1 = cq.Workplane('XY').placeSketch(sketch_1).extrude(1.0, both=False)
result = extrude_1
profile_1 = (
    cq.Sketch()
    # loop_1_1
    .arc((0.0, 0.0), 5.0, 0.0, 360.0, 'circle_1_1_1')
    .assemble()
)

sketch_2 = profile_1

extrude_2 = cq.Workplane('bottom').placeSketch(sketch_2).extrude(4.0, both=False)
result = result.union(extrude_2)
profile_1 = (
    cq.Sketch()
    # loop_1_1
    .arc((0.0, 0.0), 0.75, 0.0, 360.0, 'circle_1_1_1')
    .assemble()
)

sketch_3 = profile_1

extrude_3 = cq.Workplane().copyWorkplane(extrude_1.faces(DirectionSelector(cq.Vector(0.0, 0.0, 1.0))).workplane()).placeSketch(sketch_3).extrude(-25.0, both=False)
result = result.cut(extrude_3)
show_object(result)