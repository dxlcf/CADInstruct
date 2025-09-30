from DeepCADProcess.cadlib.instruction_base import * 

# part_1
sketch_1 = Sketch()
profile_1 = Profile([
    Loop([
        Line((0.0, -254.0), (254.0, -254.0), name="line_1_1_1"),
        Line((254.0, 0.0), name="line_1_1_2"),
        Line((25.4, 0.0), name="line_1_1_3"),
        Arc((17.961, -17.961), (0.0, -25.4), name="arc_1_1_4"),
        Line((0.0, -254.0), name="line_1_1_5"),
    ]),
])
sketch_1.add_profile([profile_1])
sketch_1.add_constraint([
    Constraint(['line_1_1_1'], 'Horizontal', None),
    Constraint(['line_1_1_1.end_point', 'line_1_1_2.start_point'], 'Coincident', None),
    Constraint(['line_1_1_1'], 'Length', 254.0),
    Constraint(['line_1_1_2'], 'Length', 254.0),
])
workplane_1 = WorkplanePre('XY')
extrude_1 = Extrude(workplane_1, sketch_1, 'newbody', 12.7, 0.0, False)


