from DeepCADProcess.cadlib.instruction_base import * 

# part_1
sketch_1 = Sketch()
profile_1 = Profile([
    Loop([
        Arc((5.958, 0.709), (5.977, 0.523), (5.991, 0.336), name="arc_1_1_1"),
        Line((6.975, 0.51), name="line_1_1_2"),
        Line((6.967, 0.61), name="line_1_1_3"),
        Line((6.958, 0.709), name="line_1_1_4"),
        Line((5.958, 0.709), name="line_1_1_5"),
    ]),
])
profile_2 = Profile([
    Loop([
        Arc((5.873, 1.226), (5.909, 1.042), (5.938, 0.857), name="arc_2_1_1"),
        Line((6.904, 1.116), name="line_2_1_2"),
        Line((6.887, 1.214), name="line_2_1_3"),
        Line((6.87, 1.313), name="line_2_1_4"),
        Line((5.873, 1.226), name="line_2_1_5"),
    ]),
])
profile_3 = Profile([
    Loop([
        Arc((5.744, 1.733), (5.796, 1.553), (5.841, 1.371), name="arc_3_1_1"),
        Line((6.781, 1.713), name="line_3_1_2"),
        Line((6.755, 1.81), name="line_3_1_3"),
        Line((6.729, 1.907), name="line_3_1_4"),
        Line((5.744, 1.733), name="line_3_1_5"),
    ]),
])
profile_4 = Profile([
    Loop([
        Arc((5.571, 2.227), (5.638, 2.052), (5.699, 1.875), name="arc_4_1_1"),
        Line((6.606, 2.298), name="line_4_1_2"),
        Line((6.572, 2.392), name="line_4_1_3"),
        Line((6.537, 2.486), name="line_4_1_4"),
        Line((5.571, 2.227), name="line_4_1_5"),
    ]),
])
profile_5 = Profile([
    Loop([
        Arc((5.356, 2.704), (5.438, 2.536), (5.514, 2.365), name="arc_5_1_1"),
        Line((6.38, 2.865), name="line_5_1_2"),
        Line((6.338, 2.955), name="line_5_1_3"),
        Line((6.296, 3.046), name="line_5_1_4"),
        Line((5.356, 2.704), name="line_5_1_5"),
    ]),
])
profile_6 = Profile([
    Loop([
        Arc((5.1, 3.161), (5.196, 3.0), (5.287, 2.836), name="arc_6_1_1"),
        Line((6.106, 3.41), name="line_6_1_2"),
        Line((6.056, 3.497), name="line_6_1_3"),
        Line((6.006, 3.583), name="line_6_1_4"),
        Line((5.1, 3.161), name="line_6_1_5"),
    ]),
])
profile_7 = Profile([
    Loop([
        Arc((4.805, 3.593), (4.915, 3.441), (5.02, 3.286), name="arc_7_1_1"),
        Line((5.786, 3.929), name="line_7_1_2"),
        Line((5.729, 4.011), name="line_7_1_3"),
        Line((5.671, 4.093), name="line_7_1_4"),
        Line((4.805, 3.593), name="line_7_1_5"),
    ]),
])
profile_8 = Profile([
    Loop([
        Arc((4.474, 3.998), (4.596, 3.857), (4.714, 3.711), name="arc_8_1_1"),
        Line((5.421, 4.419), name="line_8_1_2"),
        Line((5.357, 4.495), name="line_8_1_3"),
        Line((5.293, 4.572), name="line_8_1_4"),
        Line((4.474, 3.998), name="line_8_1_5"),
    ]),
])
profile_9 = Profile([
    Loop([
        Arc((4.108, 4.373), (4.243, 4.243), (4.373, 4.108), name="arc_9_1_1"),
        Line((5.016, 4.874), name="line_9_1_2"),
        Line((4.945, 4.945), name="line_9_1_3"),
        Line((4.874, 5.016), name="line_9_1_4"),
        Line((4.108, 4.373), name="line_9_1_5"),
    ]),
])
profile_10 = Profile([
    Loop([
        Arc((3.711, 4.714), (3.857, 4.596), (3.998, 4.474), name="arc_10_1_1"),
        Line((4.572, 5.293), name="line_10_1_2"),
        Line((4.495, 5.357), name="line_10_1_3"),
        Line((4.419, 5.421), name="line_10_1_4"),
        Line((3.711, 4.714), name="line_10_1_5"),
    ]),
])
profile_11 = Profile([
    Loop([
        Arc((3.286, 5.02), (3.441, 4.915), (3.593, 4.805), name="arc_11_1_1"),
        Line((4.093, 5.671), name="line_11_1_2"),
        Line((4.011, 5.729), name="line_11_1_3"),
        Line((3.929, 5.786), name="line_11_1_4"),
        Line((3.286, 5.02), name="line_11_1_5"),
    ]),
])
profile_12 = Profile([
    Loop([
        Arc((2.836, 5.287), (3.0, 5.196), (3.161, 5.1), name="arc_12_1_1"),
        Line((3.583, 6.006), name="line_12_1_2"),
        Line((3.497, 6.056), name="line_12_1_3"),
        Line((3.41, 6.106), name="line_12_1_4"),
        Line((2.836, 5.287), name="line_12_1_5"),
    ]),
])
profile_13 = Profile([
    Loop([
        Arc((2.365, 5.514), (2.536, 5.438), (2.704, 5.356), name="arc_13_1_1"),
        Line((3.046, 6.296), name="line_13_1_2"),
        Line((2.955, 6.338), name="line_13_1_3"),
        Line((2.865, 6.38), name="line_13_1_4"),
        Line((2.365, 5.514), name="line_13_1_5"),
    ]),
])
profile_14 = Profile([
    Loop([
        Arc((1.875, 5.699), (2.052, 5.638), (2.227, 5.571), name="arc_14_1_1"),
        Line((2.486, 6.537), name="line_14_1_2"),
        Line((2.392, 6.572), name="line_14_1_3"),
        Line((2.298, 6.606), name="line_14_1_4"),
        Line((1.875, 5.699), name="line_14_1_5"),
    ]),
])
profile_15 = Profile([
    Loop([
        Arc((1.371, 5.841), (1.553, 5.796), (1.733, 5.744), name="arc_15_1_1"),
        Line((1.907, 6.729), name="line_15_1_2"),
        Line((1.81, 6.755), name="line_15_1_3"),
        Line((1.713, 6.781), name="line_15_1_4"),
        Line((1.371, 5.841), name="line_15_1_5"),
    ]),
])
profile_16 = Profile([
    Loop([
        Arc((0.857, 5.938), (1.042, 5.909), (1.226, 5.873), name="arc_16_1_1"),
        Line((1.313, 6.87), name="line_16_1_2"),
        Line((1.214, 6.887), name="line_16_1_3"),
        Line((1.116, 6.904), name="line_16_1_4"),
        Line((0.857, 5.938), name="line_16_1_5"),
    ]),
])
profile_17 = Profile([
    Loop([
        Arc((0.336, 5.991), (0.523, 5.977), (0.709, 5.958), name="arc_17_1_1"),
        Line((0.709, 6.958), name="line_17_1_2"),
        Line((0.61, 6.967), name="line_17_1_3"),
        Line((0.51, 6.975), name="line_17_1_4"),
        Line((0.336, 5.991), name="line_17_1_5"),
    ]),
])
profile_18 = Profile([
    Loop([
        Arc((-0.187, 5.997), (0.0, 6.0), (0.187, 5.997), name="arc_18_1_1"),
        Line((0.1, 6.993), name="line_18_1_2"),
        Line((0.0, 6.993), name="line_18_1_3"),
        Line((-0.1, 6.993), name="line_18_1_4"),
        Line((-0.187, 5.997), name="line_18_1_5"),
    ]),
])
profile_19 = Profile([
    Loop([
        Arc((-0.709, 5.958), (-0.523, 5.977), (-0.336, 5.991), name="arc_19_1_1"),
        Line((-0.51, 6.975), name="line_19_1_2"),
        Line((-0.61, 6.967), name="line_19_1_3"),
        Line((-0.709, 6.958), name="line_19_1_4"),
        Line((-0.709, 5.958), name="line_19_1_5"),
    ]),
])
profile_20 = Profile([
    Loop([
        Line((-1.313, 6.87), (-1.226, 5.873), name="line_20_1_1"),
        Arc((-1.042, 5.909), (-0.857, 5.938), name="arc_20_1_2"),
        Line((-1.116, 6.904), name="line_20_1_3"),
        Line((-1.214, 6.887), name="line_20_1_4"),
        Line((-1.313, 6.87), name="line_20_1_5"),
    ]),
])
profile_21 = Profile([
    Loop([
        Line((-1.907, 6.729), (-1.733, 5.744), name="line_21_1_1"),
        Arc((-1.553, 5.796), (-1.371, 5.841), name="arc_21_1_2"),
        Line((-1.713, 6.781), name="line_21_1_3"),
        Line((-1.81, 6.755), name="line_21_1_4"),
        Line((-1.907, 6.729), name="line_21_1_5"),
    ]),
])
profile_22 = Profile([
    Loop([
        Line((-2.486, 6.537), (-2.227, 5.571), name="line_22_1_1"),
        Arc((-2.052, 5.638), (-1.875, 5.699), name="arc_22_1_2"),
        Line((-2.298, 6.606), name="line_22_1_3"),
        Line((-2.392, 6.572), name="line_22_1_4"),
        Line((-2.486, 6.537), name="line_22_1_5"),
    ]),
])
profile_23 = Profile([
    Loop([
        Line((-3.046, 6.296), (-2.704, 5.356), name="line_23_1_1"),
        Arc((-2.536, 5.438), (-2.365, 5.514), name="arc_23_1_2"),
        Line((-2.865, 6.38), name="line_23_1_3"),
        Line((-2.955, 6.338), name="line_23_1_4"),
        Line((-3.046, 6.296), name="line_23_1_5"),
    ]),
])
profile_24 = Profile([
    Loop([
        Line((-3.583, 6.006), (-3.161, 5.1), name="line_24_1_1"),
        Arc((-3.0, 5.196), (-2.836, 5.287), name="arc_24_1_2"),
        Line((-3.41, 6.106), name="line_24_1_3"),
        Line((-3.497, 6.056), name="line_24_1_4"),
        Line((-3.583, 6.006), name="line_24_1_5"),
    ]),
])
profile_25 = Profile([
    Loop([
        Line((-4.093, 5.671), (-3.593, 4.805), name="line_25_1_1"),
        Arc((-3.441, 4.915), (-3.286, 5.02), name="arc_25_1_2"),
        Line((-3.929, 5.786), name="line_25_1_3"),
        Line((-4.011, 5.729), name="line_25_1_4"),
        Line((-4.093, 5.671), name="line_25_1_5"),
    ]),
])
profile_26 = Profile([
    Loop([
        Line((-4.572, 5.293), (-3.998, 4.474), name="line_26_1_1"),
        Arc((-3.857, 4.596), (-3.711, 4.714), name="arc_26_1_2"),
        Line((-4.419, 5.421), name="line_26_1_3"),
        Line((-4.495, 5.357), name="line_26_1_4"),
        Line((-4.572, 5.293), name="line_26_1_5"),
    ]),
])
profile_27 = Profile([
    Loop([
        Line((-5.016, 4.874), (-4.373, 4.108), name="line_27_1_1"),
        Arc((-4.243, 4.243), (-4.108, 4.373), name="arc_27_1_2"),
        Line((-4.874, 5.016), name="line_27_1_3"),
        Line((-4.945, 4.945), name="line_27_1_4"),
        Line((-5.016, 4.874), name="line_27_1_5"),
    ]),
])
profile_28 = Profile([
    Loop([
        Line((-5.421, 4.419), (-4.714, 3.711), name="line_28_1_1"),
        Arc((-4.596, 3.857), (-4.474, 3.998), name="arc_28_1_2"),
        Line((-5.293, 4.572), name="line_28_1_3"),
        Line((-5.357, 4.495), name="line_28_1_4"),
        Line((-5.421, 4.419), name="line_28_1_5"),
    ]),
])
profile_29 = Profile([
    Loop([
        Line((-5.786, 3.929), (-5.02, 3.286), name="line_29_1_1"),
        Arc((-4.915, 3.441), (-4.805, 3.593), name="arc_29_1_2"),
        Line((-5.671, 4.093), name="line_29_1_3"),
        Line((-5.729, 4.011), name="line_29_1_4"),
        Line((-5.786, 3.929), name="line_29_1_5"),
    ]),
])
profile_30 = Profile([
    Loop([
        Line((-6.106, 3.41), (-5.287, 2.836), name="line_30_1_1"),
        Arc((-5.196, 3.0), (-5.1, 3.161), name="arc_30_1_2"),
        Line((-6.006, 3.583), name="line_30_1_3"),
        Line((-6.056, 3.497), name="line_30_1_4"),
        Line((-6.106, 3.41), name="line_30_1_5"),
    ]),
])
profile_31 = Profile([
    Loop([
        Line((-6.38, 2.865), (-5.514, 2.365), name="line_31_1_1"),
        Arc((-5.438, 2.536), (-5.356, 2.704), name="arc_31_1_2"),
        Line((-6.296, 3.046), name="line_31_1_3"),
        Line((-6.338, 2.955), name="line_31_1_4"),
        Line((-6.38, 2.865), name="line_31_1_5"),
    ]),
])
profile_32 = Profile([
    Loop([
        Line((-6.606, 2.298), (-5.699, 1.875), name="line_32_1_1"),
        Arc((-5.638, 2.052), (-5.571, 2.227), name="arc_32_1_2"),
        Line((-6.537, 2.486), name="line_32_1_3"),
        Line((-6.572, 2.392), name="line_32_1_4"),
        Line((-6.606, 2.298), name="line_32_1_5"),
    ]),
])
profile_33 = Profile([
    Loop([
        Line((-6.781, 1.713), (-5.841, 1.371), name="line_33_1_1"),
        Arc((-5.796, 1.553), (-5.744, 1.733), name="arc_33_1_2"),
        Line((-6.729, 1.907), name="line_33_1_3"),
        Line((-6.755, 1.81), name="line_33_1_4"),
        Line((-6.781, 1.713), name="line_33_1_5"),
    ]),
])
profile_34 = Profile([
    Loop([
        Line((-6.904, 1.116), (-5.938, 0.857), name="line_34_1_1"),
        Arc((-5.909, 1.042), (-5.873, 1.226), name="arc_34_1_2"),
        Line((-6.87, 1.313), name="line_34_1_3"),
        Line((-6.887, 1.214), name="line_34_1_4"),
        Line((-6.904, 1.116), name="line_34_1_5"),
    ]),
])
profile_35 = Profile([
    Loop([
        Line((-6.975, 0.51), (-5.991, 0.336), name="line_35_1_1"),
        Arc((-5.977, 0.523), (-5.958, 0.709), name="arc_35_1_2"),
        Line((-6.958, 0.709), name="line_35_1_3"),
        Line((-6.967, 0.61), name="line_35_1_4"),
        Line((-6.975, 0.51), name="line_35_1_5"),
    ]),
])
profile_36 = Profile([
    Loop([
        Line((-6.993, -0.1), (-5.997, -0.187), name="line_36_1_1"),
        Arc((-6.0, 0.0), (-5.997, 0.187), name="arc_36_1_2"),
        Line((-6.993, 0.1), name="line_36_1_3"),
        Line((-6.993, 0.0), name="line_36_1_4"),
        Line((-6.993, -0.1), name="line_36_1_5"),
    ]),
])
profile_37 = Profile([
    Loop([
        Line((-6.975, -0.51), (-6.967, -0.61), name="line_37_1_1"),
        Line((-6.958, -0.709), name="line_37_1_2"),
        Line((-5.958, -0.709), name="line_37_1_3"),
        Arc((-5.977, -0.523), (-5.991, -0.336), name="arc_37_1_4"),
        Line((-6.975, -0.51), name="line_37_1_5"),
    ]),
])
profile_38 = Profile([
    Loop([
        Line((-6.904, -1.116), (-6.887, -1.214), name="line_38_1_1"),
        Line((-6.87, -1.313), name="line_38_1_2"),
        Line((-5.873, -1.226), name="line_38_1_3"),
        Arc((-5.909, -1.042), (-5.938, -0.857), name="arc_38_1_4"),
        Line((-6.904, -1.116), name="line_38_1_5"),
    ]),
])
profile_39 = Profile([
    Loop([
        Line((-6.781, -1.713), (-6.755, -1.81), name="line_39_1_1"),
        Line((-6.729, -1.907), name="line_39_1_2"),
        Line((-5.744, -1.733), name="line_39_1_3"),
        Arc((-5.796, -1.553), (-5.841, -1.371), name="arc_39_1_4"),
        Line((-6.781, -1.713), name="line_39_1_5"),
    ]),
])
profile_40 = Profile([
    Loop([
        Line((-6.606, -2.298), (-6.572, -2.392), name="line_40_1_1"),
        Line((-6.537, -2.486), name="line_40_1_2"),
        Line((-5.571, -2.227), name="line_40_1_3"),
        Arc((-5.638, -2.052), (-5.699, -1.875), name="arc_40_1_4"),
        Line((-6.606, -2.298), name="line_40_1_5"),
    ]),
])
profile_41 = Profile([
    Loop([
        Line((-6.38, -2.865), (-6.338, -2.955), name="line_41_1_1"),
        Line((-6.296, -3.046), name="line_41_1_2"),
        Line((-5.356, -2.704), name="line_41_1_3"),
        Arc((-5.438, -2.536), (-5.514, -2.365), name="arc_41_1_4"),
        Line((-6.38, -2.865), name="line_41_1_5"),
    ]),
])
profile_42 = Profile([
    Loop([
        Line((-6.106, -3.41), (-6.056, -3.497), name="line_42_1_1"),
        Line((-6.006, -3.583), name="line_42_1_2"),
        Line((-5.1, -3.161), name="line_42_1_3"),
        Arc((-5.196, -3.0), (-5.287, -2.836), name="arc_42_1_4"),
        Line((-6.106, -3.41), name="line_42_1_5"),
    ]),
])
profile_43 = Profile([
    Loop([
        Line((-5.786, -3.929), (-5.729, -4.011), name="line_43_1_1"),
        Line((-5.671, -4.093), name="line_43_1_2"),
        Line((-4.805, -3.593), name="line_43_1_3"),
        Arc((-4.915, -3.441), (-5.02, -3.286), name="arc_43_1_4"),
        Line((-5.786, -3.929), name="line_43_1_5"),
    ]),
])
profile_44 = Profile([
    Loop([
        Line((-5.421, -4.419), (-5.357, -4.495), name="line_44_1_1"),
        Line((-5.293, -4.572), name="line_44_1_2"),
        Line((-4.474, -3.998), name="line_44_1_3"),
        Arc((-4.596, -3.857), (-4.714, -3.711), name="arc_44_1_4"),
        Line((-5.421, -4.419), name="line_44_1_5"),
    ]),
])
profile_45 = Profile([
    Loop([
        Line((-5.016, -4.874), (-4.945, -4.945), name="line_45_1_1"),
        Line((-4.874, -5.016), name="line_45_1_2"),
        Line((-4.108, -4.373), name="line_45_1_3"),
        Arc((-4.243, -4.243), (-4.373, -4.108), name="arc_45_1_4"),
        Line((-5.016, -4.874), name="line_45_1_5"),
    ]),
])
profile_46 = Profile([
    Loop([
        Line((-4.572, -5.293), (-4.495, -5.357), name="line_46_1_1"),
        Line((-4.419, -5.421), name="line_46_1_2"),
        Line((-3.711, -4.714), name="line_46_1_3"),
        Arc((-3.857, -4.596), (-3.998, -4.474), name="arc_46_1_4"),
        Line((-4.572, -5.293), name="line_46_1_5"),
    ]),
])
profile_47 = Profile([
    Loop([
        Line((-4.093, -5.671), (-4.011, -5.729), name="line_47_1_1"),
        Line((-3.929, -5.786), name="line_47_1_2"),
        Line((-3.286, -5.02), name="line_47_1_3"),
        Arc((-3.441, -4.915), (-3.593, -4.805), name="arc_47_1_4"),
        Line((-4.093, -5.671), name="line_47_1_5"),
    ]),
])
profile_48 = Profile([
    Loop([
        Line((-3.583, -6.006), (-3.497, -6.056), name="line_48_1_1"),
        Line((-3.41, -6.106), name="line_48_1_2"),
        Line((-2.836, -5.287), name="line_48_1_3"),
        Arc((-3.0, -5.196), (-3.161, -5.1), name="arc_48_1_4"),
        Line((-3.583, -6.006), name="line_48_1_5"),
    ]),
])
profile_49 = Profile([
    Loop([
        Line((-3.046, -6.296), (-2.955, -6.338), name="line_49_1_1"),
        Line((-2.865, -6.38), name="line_49_1_2"),
        Line((-2.365, -5.514), name="line_49_1_3"),
        Arc((-2.536, -5.438), (-2.704, -5.356), name="arc_49_1_4"),
        Line((-3.046, -6.296), name="line_49_1_5"),
    ]),
])
profile_50 = Profile([
    Loop([
        Line((-2.486, -6.537), (-2.392, -6.572), name="line_50_1_1"),
        Line((-2.298, -6.606), name="line_50_1_2"),
        Line((-1.875, -5.699), name="line_50_1_3"),
        Arc((-2.052, -5.638), (-2.227, -5.571), name="arc_50_1_4"),
        Line((-2.486, -6.537), name="line_50_1_5"),
    ]),
])
profile_51 = Profile([
    Loop([
        Line((-1.907, -6.729), (-1.81, -6.755), name="line_51_1_1"),
        Line((-1.713, -6.781), name="line_51_1_2"),
        Line((-1.371, -5.841), name="line_51_1_3"),
        Arc((-1.553, -5.796), (-1.733, -5.744), name="arc_51_1_4"),
        Line((-1.907, -6.729), name="line_51_1_5"),
    ]),
])
profile_52 = Profile([
    Loop([
        Line((-1.313, -6.87), (-1.214, -6.887), name="line_52_1_1"),
        Line((-1.116, -6.904), name="line_52_1_2"),
        Line((-0.857, -5.938), name="line_52_1_3"),
        Arc((-1.042, -5.909), (-1.226, -5.873), name="arc_52_1_4"),
        Line((-1.313, -6.87), name="line_52_1_5"),
    ]),
])
profile_53 = Profile([
    Loop([
        Line((-0.709, -6.958), (-0.61, -6.967), name="line_53_1_1"),
        Line((-0.51, -6.975), name="line_53_1_2"),
        Line((-0.336, -5.991), name="line_53_1_3"),
        Arc((-0.523, -5.977), (-0.709, -5.958), name="arc_53_1_4"),
        Line((-0.709, -6.958), name="line_53_1_5"),
    ]),
])
profile_54 = Profile([
    Loop([
        Line((-0.187, -5.997), (-0.1, -6.993), name="line_54_1_1"),
        Line((0.0, -6.993), name="line_54_1_2"),
        Line((0.1, -6.993), name="line_54_1_3"),
        Line((0.187, -5.997), name="line_54_1_4"),
        Arc((0.0, -6.0), (-0.187, -5.997), name="arc_54_1_5"),
    ]),
])
profile_55 = Profile([
    Loop([
        Line((0.336, -5.991), (0.51, -6.975), name="line_55_1_1"),
        Line((0.61, -6.967), name="line_55_1_2"),
        Line((0.709, -6.958), name="line_55_1_3"),
        Line((0.709, -5.958), name="line_55_1_4"),
        Arc((0.523, -5.977), (0.336, -5.991), name="arc_55_1_5"),
    ]),
])
profile_56 = Profile([
    Loop([
        Line((0.857, -5.938), (1.116, -6.904), name="line_56_1_1"),
        Line((1.214, -6.887), name="line_56_1_2"),
        Line((1.313, -6.87), name="line_56_1_3"),
        Line((1.226, -5.873), name="line_56_1_4"),
        Arc((1.042, -5.909), (0.857, -5.938), name="arc_56_1_5"),
    ]),
])
profile_57 = Profile([
    Loop([
        Line((1.371, -5.841), (1.713, -6.781), name="line_57_1_1"),
        Line((1.81, -6.755), name="line_57_1_2"),
        Line((1.907, -6.729), name="line_57_1_3"),
        Line((1.733, -5.744), name="line_57_1_4"),
        Arc((1.553, -5.796), (1.371, -5.841), name="arc_57_1_5"),
    ]),
])
profile_58 = Profile([
    Loop([
        Line((1.875, -5.699), (2.298, -6.606), name="line_58_1_1"),
        Line((2.392, -6.572), name="line_58_1_2"),
        Line((2.486, -6.537), name="line_58_1_3"),
        Line((2.227, -5.571), name="line_58_1_4"),
        Arc((2.052, -5.638), (1.875, -5.699), name="arc_58_1_5"),
    ]),
])
profile_59 = Profile([
    Loop([
        Line((2.365, -5.514), (2.865, -6.38), name="line_59_1_1"),
        Line((2.955, -6.338), name="line_59_1_2"),
        Line((3.046, -6.296), name="line_59_1_3"),
        Line((2.704, -5.356), name="line_59_1_4"),
        Arc((2.536, -5.438), (2.365, -5.514), name="arc_59_1_5"),
    ]),
])
profile_60 = Profile([
    Loop([
        Line((2.836, -5.287), (3.41, -6.106), name="line_60_1_1"),
        Line((3.497, -6.056), name="line_60_1_2"),
        Line((3.583, -6.006), name="line_60_1_3"),
        Line((3.161, -5.1), name="line_60_1_4"),
        Arc((3.0, -5.196), (2.836, -5.287), name="arc_60_1_5"),
    ]),
])
profile_61 = Profile([
    Loop([
        Line((3.286, -5.02), (3.929, -5.786), name="line_61_1_1"),
        Line((4.011, -5.729), name="line_61_1_2"),
        Line((4.093, -5.671), name="line_61_1_3"),
        Line((3.593, -4.805), name="line_61_1_4"),
        Arc((3.441, -4.915), (3.286, -5.02), name="arc_61_1_5"),
    ]),
])
profile_62 = Profile([
    Loop([
        Line((3.711, -4.714), (4.419, -5.421), name="line_62_1_1"),
        Line((4.495, -5.357), name="line_62_1_2"),
        Line((4.572, -5.293), name="line_62_1_3"),
        Line((3.998, -4.474), name="line_62_1_4"),
        Arc((3.857, -4.596), (3.711, -4.714), name="arc_62_1_5"),
    ]),
])
profile_63 = Profile([
    Loop([
        Line((4.108, -4.373), (4.874, -5.016), name="line_63_1_1"),
        Line((4.945, -4.945), name="line_63_1_2"),
        Line((5.016, -4.874), name="line_63_1_3"),
        Line((4.373, -4.108), name="line_63_1_4"),
        Arc((4.243, -4.243), (4.108, -4.373), name="arc_63_1_5"),
    ]),
])
profile_64 = Profile([
    Loop([
        Line((4.474, -3.998), (5.293, -4.572), name="line_64_1_1"),
        Line((5.357, -4.495), name="line_64_1_2"),
        Line((5.421, -4.419), name="line_64_1_3"),
        Line((4.714, -3.711), name="line_64_1_4"),
        Arc((4.596, -3.857), (4.474, -3.998), name="arc_64_1_5"),
    ]),
])
profile_65 = Profile([
    Loop([
        Line((4.805, -3.593), (5.671, -4.093), name="line_65_1_1"),
        Line((5.729, -4.011), name="line_65_1_2"),
        Line((5.786, -3.929), name="line_65_1_3"),
        Line((5.02, -3.286), name="line_65_1_4"),
        Arc((4.915, -3.441), (4.805, -3.593), name="arc_65_1_5"),
    ]),
])
profile_66 = Profile([
    Loop([
        Line((5.1, -3.161), (6.006, -3.583), name="line_66_1_1"),
        Line((6.056, -3.497), name="line_66_1_2"),
        Line((6.106, -3.41), name="line_66_1_3"),
        Line((5.287, -2.836), name="line_66_1_4"),
        Arc((5.196, -3.0), (5.1, -3.161), name="arc_66_1_5"),
    ]),
])
profile_67 = Profile([
    Loop([
        Line((5.356, -2.704), (6.296, -3.046), name="line_67_1_1"),
        Line((6.338, -2.955), name="line_67_1_2"),
        Line((6.38, -2.865), name="line_67_1_3"),
        Line((5.514, -2.365), name="line_67_1_4"),
        Arc((5.438, -2.536), (5.356, -2.704), name="arc_67_1_5"),
    ]),
])
profile_68 = Profile([
    Loop([
        Line((5.571, -2.227), (6.537, -2.486), name="line_68_1_1"),
        Line((6.572, -2.392), name="line_68_1_2"),
        Line((6.606, -2.298), name="line_68_1_3"),
        Line((5.699, -1.875), name="line_68_1_4"),
        Arc((5.638, -2.052), (5.571, -2.227), name="arc_68_1_5"),
    ]),
])
profile_69 = Profile([
    Loop([
        Line((5.744, -1.733), (6.729, -1.907), name="line_69_1_1"),
        Line((6.755, -1.81), name="line_69_1_2"),
        Line((6.781, -1.713), name="line_69_1_3"),
        Line((5.841, -1.371), name="line_69_1_4"),
        Arc((5.796, -1.553), (5.744, -1.733), name="arc_69_1_5"),
    ]),
])
profile_70 = Profile([
    Loop([
        Line((5.873, -1.226), (6.87, -1.313), name="line_70_1_1"),
        Line((6.887, -1.214), name="line_70_1_2"),
        Line((6.904, -1.116), name="line_70_1_3"),
        Line((5.938, -0.857), name="line_70_1_4"),
        Arc((5.909, -1.042), (5.873, -1.226), name="arc_70_1_5"),
    ]),
])
profile_71 = Profile([
    Loop([
        Line((5.958, -0.709), (6.958, -0.709), name="line_71_1_1"),
        Line((6.967, -0.61), name="line_71_1_2"),
        Line((6.975, -0.51), name="line_71_1_3"),
        Line((5.991, -0.336), name="line_71_1_4"),
        Arc((5.977, -0.523), (5.958, -0.709), name="arc_71_1_5"),
    ]),
])
profile_72 = Profile([
    Loop([
        Line((5.997, -0.187), (6.993, -0.1), name="line_72_1_1"),
        Line((6.993, 0.0), name="line_72_1_2"),
        Line((6.993, 0.1), name="line_72_1_3"),
        Line((5.997, 0.187), name="line_72_1_4"),
        Arc((6.0, 0.0), (5.997, -0.187), name="arc_72_1_5"),
    ]),
])
profile_73 = Profile([
    Loop([
        Circle((0.0, 0.0), 6.0, name="circle_73_1_1"),
    ]),
])
sketch_1.add_profile([profile_1, profile_2, profile_3, profile_4, profile_5, profile_6, profile_7, profile_8, profile_9, profile_10, profile_11, profile_12, profile_13, profile_14, profile_15, profile_16, profile_17, profile_18, profile_19, profile_20, profile_21, profile_22, profile_23, profile_24, profile_25, profile_26, profile_27, profile_28, profile_29, profile_30, profile_31, profile_32, profile_33, profile_34, profile_35, profile_36, profile_37, profile_38, profile_39, profile_40, profile_41, profile_42, profile_43, profile_44, profile_45, profile_46, profile_47, profile_48, profile_49, profile_50, profile_51, profile_52, profile_53, profile_54, profile_55, profile_56, profile_57, profile_58, profile_59, profile_60, profile_61, profile_62, profile_63, profile_64, profile_65, profile_66, profile_67, profile_68, profile_69, profile_70, profile_71, profile_72, profile_73])
sketch_1.add_constraint([
    Constraint(['circle_73_1_1.center_point', 'origin'], 'Coincident', None),
    Constraint(['circle_73_1_1'], 'Diameter', 12.0),
    Constraint(['line_18_1_5.end_point', 'circle_73_1_1'], 'Coincident', None),
    Constraint(['line_18_1_4.end_point', 'line_18_1_5.start_point'], 'Coincident', None),
    Constraint(['line_18_1_4'], 'Horizontal', None),
    Constraint(['line_18_1_4.start_point', 'line_18_1_3.end_point'], 'Coincident', None),
    Constraint(['circle_73_1_1', 'line_18_1_2.start_point'], 'Coincident', None),
    Constraint(['line_18_1_3.start_point', 'line_18_1_2.end_point'], 'Coincident', None),
    Constraint(['line_18_1_4.end_point', 'line_18_1_3.start_point'], 'Distance', 0.2),
    Constraint(['line_18_1_5'], 'Length', 1.0),
    Constraint(['line_18_1_4', 'line_18_1_5'], 'Angle', 95.0),
    Constraint(['line_19_1_4.end_point', 'line_19_1_5.start_point'], 'Coincident', None),
    Constraint(['line_19_1_4.start_point', 'line_19_1_3.end_point'], 'Coincident', None),
    Constraint(['line_19_1_3.start_point', 'line_19_1_2.end_point'], 'Coincident', None),
    Constraint(['line_20_1_5.end_point', 'line_20_1_1.start_point'], 'Coincident', None),
    Constraint(['line_20_1_5.start_point', 'line_20_1_4.end_point'], 'Coincident', None),
    Constraint(['line_20_1_4.start_point', 'line_20_1_3.end_point'], 'Coincident', None),
    Constraint(['line_21_1_5.end_point', 'line_21_1_1.start_point'], 'Coincident', None),
    Constraint(['line_21_1_5.start_point', 'line_21_1_4.end_point'], 'Coincident', None),
    Constraint(['line_21_1_4.start_point', 'line_21_1_3.end_point'], 'Coincident', None),
    Constraint(['line_22_1_5.end_point', 'line_22_1_1.start_point'], 'Coincident', None),
    Constraint(['line_22_1_5.start_point', 'line_22_1_4.end_point'], 'Coincident', None),
    Constraint(['line_22_1_4.start_point', 'line_22_1_3.end_point'], 'Coincident', None),
    Constraint(['line_23_1_5.end_point', 'line_23_1_1.start_point'], 'Coincident', None),
    Constraint(['line_23_1_5.start_point', 'line_23_1_4.end_point'], 'Coincident', None),
    Constraint(['line_23_1_4.start_point', 'line_23_1_3.end_point'], 'Coincident', None),
    Constraint(['line_24_1_5.end_point', 'line_24_1_1.start_point'], 'Coincident', None),
    Constraint(['line_24_1_5.start_point', 'line_24_1_4.end_point'], 'Coincident', None),
    Constraint(['line_24_1_4.start_point', 'line_24_1_3.end_point'], 'Coincident', None),
    Constraint(['line_25_1_5.end_point', 'line_25_1_1.start_point'], 'Coincident', None),
    Constraint(['line_25_1_5.start_point', 'line_25_1_4.end_point'], 'Coincident', None),
    Constraint(['line_25_1_4.start_point', 'line_25_1_3.end_point'], 'Coincident', None),
    Constraint(['line_26_1_5.end_point', 'line_26_1_1.start_point'], 'Coincident', None),
    Constraint(['line_26_1_5.start_point', 'line_26_1_4.end_point'], 'Coincident', None),
    Constraint(['line_26_1_4.start_point', 'line_26_1_3.end_point'], 'Coincident', None),
    Constraint(['line_27_1_5.end_point', 'line_27_1_1.start_point'], 'Coincident', None),
    Constraint(['line_27_1_5.start_point', 'line_27_1_4.end_point'], 'Coincident', None),
    Constraint(['line_27_1_4.start_point', 'line_27_1_3.end_point'], 'Coincident', None),
    Constraint(['line_28_1_5.end_point', 'line_28_1_1.start_point'], 'Coincident', None),
    Constraint(['line_28_1_5.start_point', 'line_28_1_4.end_point'], 'Coincident', None),
    Constraint(['line_28_1_4.start_point', 'line_28_1_3.end_point'], 'Coincident', None),
    Constraint(['line_29_1_5.end_point', 'line_29_1_1.start_point'], 'Coincident', None),
    Constraint(['line_29_1_5.start_point', 'line_29_1_4.end_point'], 'Coincident', None),
    Constraint(['line_29_1_4.start_point', 'line_29_1_3.end_point'], 'Coincident', None),
    Constraint(['line_30_1_5.end_point', 'line_30_1_1.start_point'], 'Coincident', None),
    Constraint(['line_30_1_5.start_point', 'line_30_1_4.end_point'], 'Coincident', None),
    Constraint(['line_30_1_4.start_point', 'line_30_1_3.end_point'], 'Coincident', None),
    Constraint(['line_31_1_5.end_point', 'line_31_1_1.start_point'], 'Coincident', None),
    Constraint(['line_31_1_5.start_point', 'line_31_1_4.end_point'], 'Coincident', None),
    Constraint(['line_31_1_4.start_point', 'line_31_1_3.end_point'], 'Coincident', None),
    Constraint(['line_32_1_5.end_point', 'line_32_1_1.start_point'], 'Coincident', None),
    Constraint(['line_32_1_5.start_point', 'line_32_1_4.end_point'], 'Coincident', None),
    Constraint(['line_32_1_4.start_point', 'line_32_1_3.end_point'], 'Coincident', None),
    Constraint(['line_33_1_5.end_point', 'line_33_1_1.start_point'], 'Coincident', None),
    Constraint(['line_33_1_5.start_point', 'line_33_1_4.end_point'], 'Coincident', None),
    Constraint(['line_33_1_4.start_point', 'line_33_1_3.end_point'], 'Coincident', None),
    Constraint(['line_34_1_5.end_point', 'line_34_1_1.start_point'], 'Coincident', None),
    Constraint(['line_34_1_5.start_point', 'line_34_1_4.end_point'], 'Coincident', None),
    Constraint(['line_34_1_4.start_point', 'line_34_1_3.end_point'], 'Coincident', None),
    Constraint(['line_35_1_5.end_point', 'line_35_1_1.start_point'], 'Coincident', None),
    Constraint(['line_35_1_5.start_point', 'line_35_1_4.end_point'], 'Coincident', None),
    Constraint(['line_35_1_4.start_point', 'line_35_1_3.end_point'], 'Coincident', None),
    Constraint(['line_36_1_5.end_point', 'line_36_1_1.start_point'], 'Coincident', None),
    Constraint(['line_36_1_5.start_point', 'line_36_1_4.end_point'], 'Coincident', None),
    Constraint(['line_36_1_4.start_point', 'line_36_1_3.end_point'], 'Coincident', None),
    Constraint(['line_37_1_2.end_point', 'line_37_1_3.start_point'], 'Coincident', None),
    Constraint(['line_37_1_2.start_point', 'line_37_1_1.end_point'], 'Coincident', None),
    Constraint(['line_37_1_1.start_point', 'line_37_1_5.end_point'], 'Coincident', None),
    Constraint(['line_38_1_2.end_point', 'line_38_1_3.start_point'], 'Coincident', None),
    Constraint(['line_38_1_2.start_point', 'line_38_1_1.end_point'], 'Coincident', None),
    Constraint(['line_38_1_1.start_point', 'line_38_1_5.end_point'], 'Coincident', None),
    Constraint(['line_39_1_2.end_point', 'line_39_1_3.start_point'], 'Coincident', None),
    Constraint(['line_39_1_2.start_point', 'line_39_1_1.end_point'], 'Coincident', None),
    Constraint(['line_39_1_1.start_point', 'line_39_1_5.end_point'], 'Coincident', None),
    Constraint(['line_40_1_2.end_point', 'line_40_1_3.start_point'], 'Coincident', None),
    Constraint(['line_40_1_2.start_point', 'line_40_1_1.end_point'], 'Coincident', None),
    Constraint(['line_40_1_1.start_point', 'line_40_1_5.end_point'], 'Coincident', None),
    Constraint(['line_41_1_2.end_point', 'line_41_1_3.start_point'], 'Coincident', None),
    Constraint(['line_41_1_2.start_point', 'line_41_1_1.end_point'], 'Coincident', None),
    Constraint(['line_41_1_1.start_point', 'line_41_1_5.end_point'], 'Coincident', None),
    Constraint(['line_42_1_2.end_point', 'line_42_1_3.start_point'], 'Coincident', None),
    Constraint(['line_42_1_2.start_point', 'line_42_1_1.end_point'], 'Coincident', None),
    Constraint(['line_42_1_1.start_point', 'line_42_1_5.end_point'], 'Coincident', None),
    Constraint(['line_43_1_2.end_point', 'line_43_1_3.start_point'], 'Coincident', None),
    Constraint(['line_43_1_2.start_point', 'line_43_1_1.end_point'], 'Coincident', None),
    Constraint(['line_43_1_1.start_point', 'line_43_1_5.end_point'], 'Coincident', None),
    Constraint(['line_44_1_2.end_point', 'line_44_1_3.start_point'], 'Coincident', None),
    Constraint(['line_44_1_2.start_point', 'line_44_1_1.end_point'], 'Coincident', None),
    Constraint(['line_44_1_1.start_point', 'line_44_1_5.end_point'], 'Coincident', None),
    Constraint(['line_45_1_2.end_point', 'line_45_1_3.start_point'], 'Coincident', None),
    Constraint(['line_45_1_2.start_point', 'line_45_1_1.end_point'], 'Coincident', None),
    Constraint(['line_45_1_1.start_point', 'line_45_1_5.end_point'], 'Coincident', None),
    Constraint(['line_46_1_2.end_point', 'line_46_1_3.start_point'], 'Coincident', None),
    Constraint(['line_46_1_2.start_point', 'line_46_1_1.end_point'], 'Coincident', None),
    Constraint(['line_46_1_1.start_point', 'line_46_1_5.end_point'], 'Coincident', None),
    Constraint(['line_47_1_2.end_point', 'line_47_1_3.start_point'], 'Coincident', None),
    Constraint(['line_47_1_2.start_point', 'line_47_1_1.end_point'], 'Coincident', None),
    Constraint(['line_47_1_1.start_point', 'line_47_1_5.end_point'], 'Coincident', None),
    Constraint(['line_48_1_2.end_point', 'line_48_1_3.start_point'], 'Coincident', None),
    Constraint(['line_48_1_2.start_point', 'line_48_1_1.end_point'], 'Coincident', None),
    Constraint(['line_48_1_1.start_point', 'line_48_1_5.end_point'], 'Coincident', None),
    Constraint(['line_49_1_2.end_point', 'line_49_1_3.start_point'], 'Coincident', None),
    Constraint(['line_49_1_2.start_point', 'line_49_1_1.end_point'], 'Coincident', None),
    Constraint(['line_49_1_1.start_point', 'line_49_1_5.end_point'], 'Coincident', None),
    Constraint(['line_50_1_2.end_point', 'line_50_1_3.start_point'], 'Coincident', None),
    Constraint(['line_50_1_2.start_point', 'line_50_1_1.end_point'], 'Coincident', None),
    Constraint(['line_50_1_1.start_point', 'line_50_1_5.end_point'], 'Coincident', None),
    Constraint(['line_51_1_2.end_point', 'line_51_1_3.start_point'], 'Coincident', None),
    Constraint(['line_51_1_2.start_point', 'line_51_1_1.end_point'], 'Coincident', None),
    Constraint(['line_51_1_1.start_point', 'line_51_1_5.end_point'], 'Coincident', None),
    Constraint(['line_52_1_2.end_point', 'line_52_1_3.start_point'], 'Coincident', None),
    Constraint(['line_52_1_2.start_point', 'line_52_1_1.end_point'], 'Coincident', None),
    Constraint(['line_52_1_1.start_point', 'line_52_1_5.end_point'], 'Coincident', None),
    Constraint(['line_53_1_2.end_point', 'line_53_1_3.start_point'], 'Coincident', None),
    Constraint(['line_53_1_2.start_point', 'line_53_1_1.end_point'], 'Coincident', None),
    Constraint(['line_53_1_1.start_point', 'line_53_1_5.end_point'], 'Coincident', None),
    Constraint(['line_54_1_3.end_point', 'line_54_1_4.start_point'], 'Coincident', None),
    Constraint(['line_54_1_3.start_point', 'line_54_1_2.end_point'], 'Coincident', None),
    Constraint(['line_54_1_2.start_point', 'line_54_1_1.end_point'], 'Coincident', None),
    Constraint(['line_55_1_3.end_point', 'line_55_1_4.start_point'], 'Coincident', None),
    Constraint(['line_55_1_3.start_point', 'line_55_1_2.end_point'], 'Coincident', None),
    Constraint(['line_55_1_2.start_point', 'line_55_1_1.end_point'], 'Coincident', None),
    Constraint(['line_56_1_3.end_point', 'line_56_1_4.start_point'], 'Coincident', None),
    Constraint(['line_56_1_3.start_point', 'line_56_1_2.end_point'], 'Coincident', None),
    Constraint(['line_56_1_2.start_point', 'line_56_1_1.end_point'], 'Coincident', None),
    Constraint(['line_57_1_3.end_point', 'line_57_1_4.start_point'], 'Coincident', None),
    Constraint(['line_57_1_3.start_point', 'line_57_1_2.end_point'], 'Coincident', None),
    Constraint(['line_57_1_2.start_point', 'line_57_1_1.end_point'], 'Coincident', None),
    Constraint(['line_58_1_3.end_point', 'line_58_1_4.start_point'], 'Coincident', None),
    Constraint(['line_58_1_3.start_point', 'line_58_1_2.end_point'], 'Coincident', None),
    Constraint(['line_58_1_2.start_point', 'line_58_1_1.end_point'], 'Coincident', None),
    Constraint(['line_59_1_3.end_point', 'line_59_1_4.start_point'], 'Coincident', None),
    Constraint(['line_59_1_3.start_point', 'line_59_1_2.end_point'], 'Coincident', None),
    Constraint(['line_59_1_2.start_point', 'line_59_1_1.end_point'], 'Coincident', None),
    Constraint(['line_60_1_3.end_point', 'line_60_1_4.start_point'], 'Coincident', None),
    Constraint(['line_60_1_3.start_point', 'line_60_1_2.end_point'], 'Coincident', None),
    Constraint(['line_60_1_2.start_point', 'line_60_1_1.end_point'], 'Coincident', None),
    Constraint(['line_61_1_3.end_point', 'line_61_1_4.start_point'], 'Coincident', None),
    Constraint(['line_61_1_3.start_point', 'line_61_1_2.end_point'], 'Coincident', None),
    Constraint(['line_61_1_2.start_point', 'line_61_1_1.end_point'], 'Coincident', None),
    Constraint(['line_62_1_3.end_point', 'line_62_1_4.start_point'], 'Coincident', None),
    Constraint(['line_62_1_3.start_point', 'line_62_1_2.end_point'], 'Coincident', None),
    Constraint(['line_62_1_2.start_point', 'line_62_1_1.end_point'], 'Coincident', None),
    Constraint(['line_63_1_3.end_point', 'line_63_1_4.start_point'], 'Coincident', None),
    Constraint(['line_63_1_3.start_point', 'line_63_1_2.end_point'], 'Coincident', None),
    Constraint(['line_63_1_2.start_point', 'line_63_1_1.end_point'], 'Coincident', None),
    Constraint(['line_64_1_3.end_point', 'line_64_1_4.start_point'], 'Coincident', None),
    Constraint(['line_64_1_3.start_point', 'line_64_1_2.end_point'], 'Coincident', None),
    Constraint(['line_64_1_2.start_point', 'line_64_1_1.end_point'], 'Coincident', None),
    Constraint(['line_65_1_3.end_point', 'line_65_1_4.start_point'], 'Coincident', None),
    Constraint(['line_65_1_3.start_point', 'line_65_1_2.end_point'], 'Coincident', None),
    Constraint(['line_65_1_2.start_point', 'line_65_1_1.end_point'], 'Coincident', None),
    Constraint(['line_66_1_3.end_point', 'line_66_1_4.start_point'], 'Coincident', None),
    Constraint(['line_66_1_3.start_point', 'line_66_1_2.end_point'], 'Coincident', None),
    Constraint(['line_66_1_2.start_point', 'line_66_1_1.end_point'], 'Coincident', None),
    Constraint(['line_67_1_3.end_point', 'line_67_1_4.start_point'], 'Coincident', None),
    Constraint(['line_67_1_3.start_point', 'line_67_1_2.end_point'], 'Coincident', None),
    Constraint(['line_67_1_2.start_point', 'line_67_1_1.end_point'], 'Coincident', None),
    Constraint(['line_68_1_3.end_point', 'line_68_1_4.start_point'], 'Coincident', None),
    Constraint(['line_68_1_3.start_point', 'line_68_1_2.end_point'], 'Coincident', None),
    Constraint(['line_68_1_2.start_point', 'line_68_1_1.end_point'], 'Coincident', None),
    Constraint(['line_69_1_3.end_point', 'line_69_1_4.start_point'], 'Coincident', None),
    Constraint(['line_69_1_3.start_point', 'line_69_1_2.end_point'], 'Coincident', None),
    Constraint(['line_69_1_2.start_point', 'line_69_1_1.end_point'], 'Coincident', None),
    Constraint(['line_70_1_3.end_point', 'line_70_1_4.start_point'], 'Coincident', None),
    Constraint(['line_70_1_3.start_point', 'line_70_1_2.end_point'], 'Coincident', None),
    Constraint(['line_70_1_2.start_point', 'line_70_1_1.end_point'], 'Coincident', None),
    Constraint(['line_71_1_3.end_point', 'line_71_1_4.start_point'], 'Coincident', None),
    Constraint(['line_71_1_3.start_point', 'line_71_1_2.end_point'], 'Coincident', None),
    Constraint(['line_71_1_2.start_point', 'line_71_1_1.end_point'], 'Coincident', None),
    Constraint(['line_72_1_3.end_point', 'line_72_1_4.start_point'], 'Coincident', None),
    Constraint(['line_72_1_3.start_point', 'line_72_1_2.end_point'], 'Coincident', None),
    Constraint(['line_72_1_2.start_point', 'line_72_1_1.end_point'], 'Coincident', None),
    Constraint(['line_1_1_4.end_point', 'line_1_1_5.start_point'], 'Coincident', None),
    Constraint(['line_1_1_4.start_point', 'line_1_1_3.end_point'], 'Coincident', None),
    Constraint(['line_1_1_3.start_point', 'line_1_1_2.end_point'], 'Coincident', None),
    Constraint(['line_2_1_4.end_point', 'line_2_1_5.start_point'], 'Coincident', None),
    Constraint(['line_2_1_4.start_point', 'line_2_1_3.end_point'], 'Coincident', None),
    Constraint(['line_2_1_3.start_point', 'line_2_1_2.end_point'], 'Coincident', None),
    Constraint(['line_3_1_4.end_point', 'line_3_1_5.start_point'], 'Coincident', None),
    Constraint(['line_3_1_4.start_point', 'line_3_1_3.end_point'], 'Coincident', None),
    Constraint(['line_3_1_3.start_point', 'line_3_1_2.end_point'], 'Coincident', None),
    Constraint(['line_4_1_4.end_point', 'line_4_1_5.start_point'], 'Coincident', None),
    Constraint(['line_4_1_4.start_point', 'line_4_1_3.end_point'], 'Coincident', None),
    Constraint(['line_4_1_3.start_point', 'line_4_1_2.end_point'], 'Coincident', None),
    Constraint(['line_5_1_4.end_point', 'line_5_1_5.start_point'], 'Coincident', None),
    Constraint(['line_5_1_4.start_point', 'line_5_1_3.end_point'], 'Coincident', None),
    Constraint(['line_5_1_3.start_point', 'line_5_1_2.end_point'], 'Coincident', None),
    Constraint(['line_6_1_4.end_point', 'line_6_1_5.start_point'], 'Coincident', None),
    Constraint(['line_6_1_4.start_point', 'line_6_1_3.end_point'], 'Coincident', None),
    Constraint(['line_6_1_3.start_point', 'line_6_1_2.end_point'], 'Coincident', None),
    Constraint(['line_7_1_4.end_point', 'line_7_1_5.start_point'], 'Coincident', None),
    Constraint(['line_7_1_4.start_point', 'line_7_1_3.end_point'], 'Coincident', None),
    Constraint(['line_7_1_3.start_point', 'line_7_1_2.end_point'], 'Coincident', None),
    Constraint(['line_8_1_4.end_point', 'line_8_1_5.start_point'], 'Coincident', None),
    Constraint(['line_8_1_4.start_point', 'line_8_1_3.end_point'], 'Coincident', None),
    Constraint(['line_8_1_3.start_point', 'line_8_1_2.end_point'], 'Coincident', None),
    Constraint(['line_9_1_4.end_point', 'line_9_1_5.start_point'], 'Coincident', None),
    Constraint(['line_9_1_4.start_point', 'line_9_1_3.end_point'], 'Coincident', None),
    Constraint(['line_9_1_3.start_point', 'line_9_1_2.end_point'], 'Coincident', None),
    Constraint(['line_10_1_4.end_point', 'line_10_1_5.start_point'], 'Coincident', None),
    Constraint(['line_10_1_4.start_point', 'line_10_1_3.end_point'], 'Coincident', None),
    Constraint(['line_10_1_3.start_point', 'line_10_1_2.end_point'], 'Coincident', None),
    Constraint(['line_11_1_4.end_point', 'line_11_1_5.start_point'], 'Coincident', None),
    Constraint(['line_11_1_4.start_point', 'line_11_1_3.end_point'], 'Coincident', None),
    Constraint(['line_11_1_3.start_point', 'line_11_1_2.end_point'], 'Coincident', None),
    Constraint(['line_12_1_4.end_point', 'line_12_1_5.start_point'], 'Coincident', None),
    Constraint(['line_12_1_4.start_point', 'line_12_1_3.end_point'], 'Coincident', None),
    Constraint(['line_12_1_3.start_point', 'line_12_1_2.end_point'], 'Coincident', None),
    Constraint(['line_13_1_4.end_point', 'line_13_1_5.start_point'], 'Coincident', None),
    Constraint(['line_13_1_4.start_point', 'line_13_1_3.end_point'], 'Coincident', None),
    Constraint(['line_13_1_3.start_point', 'line_13_1_2.end_point'], 'Coincident', None),
    Constraint(['line_14_1_4.end_point', 'line_14_1_5.start_point'], 'Coincident', None),
    Constraint(['line_14_1_4.start_point', 'line_14_1_3.end_point'], 'Coincident', None),
    Constraint(['line_14_1_3.start_point', 'line_14_1_2.end_point'], 'Coincident', None),
    Constraint(['line_15_1_4.end_point', 'line_15_1_5.start_point'], 'Coincident', None),
    Constraint(['line_15_1_4.start_point', 'line_15_1_3.end_point'], 'Coincident', None),
    Constraint(['line_15_1_3.start_point', 'line_15_1_2.end_point'], 'Coincident', None),
    Constraint(['line_16_1_4.end_point', 'line_16_1_5.start_point'], 'Coincident', None),
    Constraint(['line_16_1_4.start_point', 'line_16_1_3.end_point'], 'Coincident', None),
    Constraint(['line_16_1_3.start_point', 'line_16_1_2.end_point'], 'Coincident', None),
    Constraint(['line_17_1_4.end_point', 'line_17_1_5.start_point'], 'Coincident', None),
    Constraint(['line_17_1_4.start_point', 'line_17_1_3.end_point'], 'Coincident', None),
    Constraint(['line_17_1_3.start_point', 'line_17_1_2.end_point'], 'Coincident', None),
])
workplane_1 = WorkplanePre('XY')
extrude_1 = Extrude(workplane_1, sketch_1, 'newbody', 1.0, 0.0, False)


# part_2
sketch_2 = Sketch()
profile_74 = Profile([
    Loop([
        Circle((0.0, 0.0), 5.0, name="circle_1_1_1"),
    ]),
])
sketch_2.add_profile([profile_74])
sketch_2.add_constraint([
    Constraint(['circle_1_1_1.center_point', 'origin'], 'Coincident', None),
    Constraint(['circle_1_1_1'], 'Diameter', 10.0),
])
workplane_2 = WorkplanePre('bottom')
extrude_2 = Extrude(workplane_2, sketch_2, 'join', 4.0, 0.0, False)


# part_3
sketch_3 = Sketch()
profile_75 = Profile([
    Loop([
        Circle((0.0, 0.0), 0.75, name="circle_1_1_1"),
    ]),
])
sketch_3.add_profile([profile_75])
sketch_3.add_constraint([
    Constraint(['circle_1_1_1.center_point', 'origin'], 'Coincident', None),
    Constraint(['circle_1_1_1'], 'Diameter', 1.5),
])
workplane_3 = WorkplaneRef('extrude_1', (0.0, 0.0, 1.0), None)
extrude_3 = Extrude(workplane_3, sketch_3, 'cut', -25.0, 0.0, False)


