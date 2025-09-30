from DeepCADProcess.cadlib.instruction_base import * 

# part_1
sketch_1 = Sketch()
profile_1 = Profile([
    Loop([
        Circle((0.0, 0.0), 91.049, name="circle_1_1_1"),
    ]),
])
sketch_1.add_profile([profile_1])
sketch_1.add_constraint([
    Constraint(['circle_1_1_1.center_point', 'origin'], 'Coincident', None),
])
workplane_1 = WorkplanePre('XY')
extrude_1 = Extrude(workplane_1, sketch_1, 'newbody', 25.4, 0.0, False)


