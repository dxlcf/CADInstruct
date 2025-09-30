from DeepCADProcess.cadlib.instruction_base import * 

# part_1
sketch_1 = Sketch()
profile_1 = Profile([
    Loop([
        Arc((0.641, 0.536), (0.724, 0.418), (0.785, 0.287), name="arc_1_1_1"),
        Line((1.195, 0.574), name="line_1_1_2"),
        Line((1.145, 0.661), name="line_1_1_3"),
        Line((1.095, 0.747), name="line_1_1_4"),
        Line((0.641, 0.536), name="line_1_1_5"),
    ]),
])
profile_2 = Profile([
    Loop([
        Arc((0.287, 0.785), (0.418, 0.724), (0.536, 0.641), name="arc_2_1_1"),
        Line((0.747, 1.095), name="line_2_1_2"),
        Line((0.661, 1.145), name="line_2_1_3"),
        Line((0.574, 1.195), name="line_2_1_4"),
        Line((0.287, 0.785), name="line_2_1_5"),
    ]),
])
profile_3 = Profile([
    Loop([
        Arc((-0.144, 0.824), (0.0, 0.836), (0.144, 0.824), name="arc_3_1_1"),
        Line((0.1, 1.322), name="line_3_1_2"),
        Line((0.0, 1.322), name="line_3_1_3"),
        Line((-0.1, 1.322), name="line_3_1_4"),
        Line((-0.144, 0.824), name="line_3_1_5"),
    ]),
])
profile_4 = Profile([
    Loop([
        Line((-0.747, 1.095), (-0.536, 0.641), name="line_4_1_1"),
        Arc((-0.418, 0.724), (-0.287, 0.785), name="arc_4_1_2"),
        Line((-0.574, 1.195), name="line_4_1_3"),
        Line((-0.661, 1.145), name="line_4_1_4"),
        Line((-0.747, 1.095), name="line_4_1_5"),
    ]),
])
profile_5 = Profile([
    Loop([
        Line((-1.195, 0.574), (-0.785, 0.287), name="line_5_1_1"),
        Arc((-0.724, 0.418), (-0.641, 0.536), name="arc_5_1_2"),
        Line((-1.095, 0.747), name="line_5_1_3"),
        Line((-1.145, 0.661), name="line_5_1_4"),
        Line((-1.195, 0.574), name="line_5_1_5"),
    ]),
])
profile_6 = Profile([
    Loop([
        Line((-1.322, -0.1), (-0.824, -0.144), name="line_6_1_1"),
        Arc((-0.836, 0.0), (-0.824, 0.144), name="arc_6_1_2"),
        Line((-1.322, 0.1), name="line_6_1_3"),
        Line((-1.322, 0.0), name="line_6_1_4"),
        Line((-1.322, -0.1), name="line_6_1_5"),
    ]),
])
profile_7 = Profile([
    Loop([
        Line((-1.195, -0.574), (-1.145, -0.661), name="line_7_1_1"),
        Line((-1.095, -0.747), name="line_7_1_2"),
        Line((-0.641, -0.536), name="line_7_1_3"),
        Arc((-0.724, -0.418), (-0.785, -0.287), name="arc_7_1_4"),
        Line((-1.195, -0.574), name="line_7_1_5"),
    ]),
])
profile_8 = Profile([
    Loop([
        Line((-0.747, -1.095), (-0.661, -1.145), name="line_8_1_1"),
        Line((-0.574, -1.195), name="line_8_1_2"),
        Line((-0.287, -0.785), name="line_8_1_3"),
        Arc((-0.418, -0.724), (-0.536, -0.641), name="arc_8_1_4"),
        Line((-0.747, -1.095), name="line_8_1_5"),
    ]),
])
profile_9 = Profile([
    Loop([
        Line((-0.144, -0.824), (-0.1, -1.322), name="line_9_1_1"),
        Line((0.0, -1.322), name="line_9_1_2"),
        Line((0.1, -1.322), name="line_9_1_3"),
        Line((0.144, -0.824), name="line_9_1_4"),
        Arc((0.0, -0.836), (-0.144, -0.824), name="arc_9_1_5"),
    ]),
])
profile_10 = Profile([
    Loop([
        Line((0.287, -0.785), (0.574, -1.195), name="line_10_1_1"),
        Line((0.661, -1.145), name="line_10_1_2"),
        Line((0.747, -1.095), name="line_10_1_3"),
        Line((0.536, -0.641), name="line_10_1_4"),
        Arc((0.418, -0.724), (0.287, -0.785), name="arc_10_1_5"),
    ]),
])
profile_11 = Profile([
    Loop([
        Line((0.641, -0.536), (1.095, -0.747), name="line_11_1_1"),
        Line((1.145, -0.661), name="line_11_1_2"),
        Line((1.195, -0.574), name="line_11_1_3"),
        Line((0.785, -0.287), name="line_11_1_4"),
        Arc((0.724, -0.418), (0.641, -0.536), name="arc_11_1_5"),
    ]),
])
profile_12 = Profile([
    Loop([
        Line((0.824, -0.144), (1.322, -0.1), name="line_12_1_1"),
        Line((1.322, 0.0), name="line_12_1_2"),
        Line((1.322, 0.1), name="line_12_1_3"),
        Line((0.824, 0.144), name="line_12_1_4"),
        Arc((0.836, 0.0), (0.824, -0.144), name="arc_12_1_5"),
    ]),
])
profile_13 = Profile([
    Loop([
        Circle((0.0, 0.0), 0.836, name="circle_13_1_1"),
    ]),
])
sketch_1.add_profile([profile_1, profile_2, profile_3, profile_4, profile_5, profile_6, profile_7, profile_8, profile_9, profile_10, profile_11, profile_12, profile_13])
sketch_1.add_constraint([
    Constraint(['circle_13_1_1.center_point', 'origin'], 'Coincident', None),
    Constraint(['circle_13_1_1'], 'Diameter', 1.672),
    Constraint(['line_3_1_5.end_point', 'circle_13_1_1'], 'Coincident', None),
    Constraint(['line_3_1_4.end_point', 'line_3_1_5.start_point'], 'Coincident', None),
    Constraint(['line_3_1_4'], 'Horizontal', None),
    Constraint(['line_3_1_4.start_point', 'line_3_1_3.end_point'], 'Coincident', None),
    Constraint(['circle_13_1_1', 'line_3_1_2.start_point'], 'Coincident', None),
    Constraint(['line_3_1_3.start_point', 'line_3_1_2.end_point'], 'Coincident', None),
    Constraint(['line_3_1_4.end_point', 'line_3_1_3.start_point'], 'Distance', 0.2),
    Constraint(['line_3_1_5'], 'Length', 0.5),
    Constraint(['line_3_1_4', 'line_3_1_5'], 'Angle', 95.0),
    Constraint(['line_4_1_5.end_point', 'line_4_1_1.start_point'], 'Coincident', None),
    Constraint(['line_4_1_5.start_point', 'line_4_1_4.end_point'], 'Coincident', None),
    Constraint(['line_4_1_4.start_point', 'line_4_1_3.end_point'], 'Coincident', None),
    Constraint(['line_5_1_5.end_point', 'line_5_1_1.start_point'], 'Coincident', None),
    Constraint(['line_5_1_5.start_point', 'line_5_1_4.end_point'], 'Coincident', None),
    Constraint(['line_5_1_4.start_point', 'line_5_1_3.end_point'], 'Coincident', None),
    Constraint(['line_6_1_5.end_point', 'line_6_1_1.start_point'], 'Coincident', None),
    Constraint(['line_6_1_5.start_point', 'line_6_1_4.end_point'], 'Coincident', None),
    Constraint(['line_6_1_4.start_point', 'line_6_1_3.end_point'], 'Coincident', None),
    Constraint(['line_7_1_2.end_point', 'line_7_1_3.start_point'], 'Coincident', None),
    Constraint(['line_7_1_2.start_point', 'line_7_1_1.end_point'], 'Coincident', None),
    Constraint(['line_7_1_1.start_point', 'line_7_1_5.end_point'], 'Coincident', None),
    Constraint(['line_8_1_2.end_point', 'line_8_1_3.start_point'], 'Coincident', None),
    Constraint(['line_8_1_2.start_point', 'line_8_1_1.end_point'], 'Coincident', None),
    Constraint(['line_8_1_1.start_point', 'line_8_1_5.end_point'], 'Coincident', None),
    Constraint(['line_9_1_3.end_point', 'line_9_1_4.start_point'], 'Coincident', None),
    Constraint(['line_9_1_3.start_point', 'line_9_1_2.end_point'], 'Coincident', None),
    Constraint(['line_9_1_2.start_point', 'line_9_1_1.end_point'], 'Coincident', None),
    Constraint(['line_10_1_3.end_point', 'line_10_1_4.start_point'], 'Coincident', None),
    Constraint(['line_10_1_3.start_point', 'line_10_1_2.end_point'], 'Coincident', None),
    Constraint(['line_10_1_2.start_point', 'line_10_1_1.end_point'], 'Coincident', None),
    Constraint(['line_11_1_3.end_point', 'line_11_1_4.start_point'], 'Coincident', None),
    Constraint(['line_11_1_3.start_point', 'line_11_1_2.end_point'], 'Coincident', None),
    Constraint(['line_11_1_2.start_point', 'line_11_1_1.end_point'], 'Coincident', None),
    Constraint(['line_12_1_3.end_point', 'line_12_1_4.start_point'], 'Coincident', None),
    Constraint(['line_12_1_3.start_point', 'line_12_1_2.end_point'], 'Coincident', None),
    Constraint(['line_12_1_2.start_point', 'line_12_1_1.end_point'], 'Coincident', None),
    Constraint(['line_1_1_4.end_point', 'line_1_1_5.start_point'], 'Coincident', None),
    Constraint(['line_1_1_4.start_point', 'line_1_1_3.end_point'], 'Coincident', None),
    Constraint(['line_1_1_3.start_point', 'line_1_1_2.end_point'], 'Coincident', None),
    Constraint(['line_2_1_4.end_point', 'line_2_1_5.start_point'], 'Coincident', None),
    Constraint(['line_2_1_4.start_point', 'line_2_1_3.end_point'], 'Coincident', None),
    Constraint(['line_2_1_3.start_point', 'line_2_1_2.end_point'], 'Coincident', None),
])
workplane_1 = WorkplanePre('XY')
extrude_1 = Extrude(workplane_1, sketch_1, 'newbody', 2.0, 0.0, False)


# part_2
sketch_2 = Sketch()
profile_14 = Profile([
    Loop([
        Circle((0.0, 0.0), 0.25, name="circle_1_1_1"),
    ]),
])
sketch_2.add_profile([profile_14])
sketch_2.add_constraint([
    Constraint(['circle_1_1_1.center_point', 'origin'], 'Coincident', None),
    Constraint(['circle_1_1_1'], 'Diameter', 0.5),
])
workplane_2 = WorkplaneRef('extrude_1', (0.0, 0.0, 1.0), None)
extrude_2 = Extrude(workplane_2, sketch_2, 'cut', -25.0, 0.0, False)


