import cadquery as cq
from cadquery.selectors import DirectionSelector, NearestToPointSelector

profile_1 = (
    cq.Sketch()
    # loop_1_1
    .arc((0.641, 0.536), (0.724, 0.418), (0.785, 0.287), 'arc_1_1_1')
    .segment((1.195, 0.574), 'line_1_1_2')
    .segment((1.145, 0.661), 'line_1_1_3')
    .segment((1.095, 0.747), 'line_1_1_4')
    .segment((0.641, 0.536), 'line_1_1_5')
    .assemble()
)

profile_2 = (
    cq.Sketch()
    # loop_2_1
    .arc((0.287, 0.785), (0.418, 0.724), (0.536, 0.641), 'arc_2_1_1')
    .segment((0.747, 1.095), 'line_2_1_2')
    .segment((0.661, 1.145), 'line_2_1_3')
    .segment((0.574, 1.195), 'line_2_1_4')
    .segment((0.287, 0.785), 'line_2_1_5')
    .assemble()
)

profile_3 = (
    cq.Sketch()
    # loop_3_1
    .arc((-0.144, 0.824), (0.0, 0.836), (0.144, 0.824), 'arc_3_1_1')
    .segment((0.1, 1.322), 'line_3_1_2')
    .segment((0.0, 1.322), 'line_3_1_3')
    .segment((-0.1, 1.322), 'line_3_1_4')
    .segment((-0.144, 0.824), 'line_3_1_5')
    .assemble()
)

profile_4 = (
    cq.Sketch()
    # loop_4_1
    .segment((-0.747, 1.095), (-0.536, 0.641), 'line_4_1_1')
    .arc((-0.418, 0.724), (-0.287, 0.785), 'arc_4_1_2')
    .segment((-0.574, 1.195), 'line_4_1_3')
    .segment((-0.661, 1.145), 'line_4_1_4')
    .segment((-0.747, 1.095), 'line_4_1_5')
    .assemble()
)

profile_5 = (
    cq.Sketch()
    # loop_5_1
    .segment((-1.195, 0.574), (-0.785, 0.287), 'line_5_1_1')
    .arc((-0.724, 0.418), (-0.641, 0.536), 'arc_5_1_2')
    .segment((-1.095, 0.747), 'line_5_1_3')
    .segment((-1.145, 0.661), 'line_5_1_4')
    .segment((-1.195, 0.574), 'line_5_1_5')
    .assemble()
)

profile_6 = (
    cq.Sketch()
    # loop_6_1
    .segment((-1.322, -0.1), (-0.824, -0.144), 'line_6_1_1')
    .arc((-0.836, 0.0), (-0.824, 0.144), 'arc_6_1_2')
    .segment((-1.322, 0.1), 'line_6_1_3')
    .segment((-1.322, 0.0), 'line_6_1_4')
    .segment((-1.322, -0.1), 'line_6_1_5')
    .assemble()
)

profile_7 = (
    cq.Sketch()
    # loop_7_1
    .segment((-1.195, -0.574), (-1.145, -0.661), 'line_7_1_1')
    .segment((-1.095, -0.747), 'line_7_1_2')
    .segment((-0.641, -0.536), 'line_7_1_3')
    .arc((-0.724, -0.418), (-0.785, -0.287), 'arc_7_1_4')
    .segment((-1.195, -0.574), 'line_7_1_5')
    .assemble()
)

profile_8 = (
    cq.Sketch()
    # loop_8_1
    .segment((-0.747, -1.095), (-0.661, -1.145), 'line_8_1_1')
    .segment((-0.574, -1.195), 'line_8_1_2')
    .segment((-0.287, -0.785), 'line_8_1_3')
    .arc((-0.418, -0.724), (-0.536, -0.641), 'arc_8_1_4')
    .segment((-0.747, -1.095), 'line_8_1_5')
    .assemble()
)

profile_9 = (
    cq.Sketch()
    # loop_9_1
    .segment((-0.144, -0.824), (-0.1, -1.322), 'line_9_1_1')
    .segment((0.0, -1.322), 'line_9_1_2')
    .segment((0.1, -1.322), 'line_9_1_3')
    .segment((0.144, -0.824), 'line_9_1_4')
    .arc((0.0, -0.836), (-0.144, -0.824), 'arc_9_1_5')
    .assemble()
)

profile_10 = (
    cq.Sketch()
    # loop_10_1
    .segment((0.287, -0.785), (0.574, -1.195), 'line_10_1_1')
    .segment((0.661, -1.145), 'line_10_1_2')
    .segment((0.747, -1.095), 'line_10_1_3')
    .segment((0.536, -0.641), 'line_10_1_4')
    .arc((0.418, -0.724), (0.287, -0.785), 'arc_10_1_5')
    .assemble()
)

profile_11 = (
    cq.Sketch()
    # loop_11_1
    .segment((0.641, -0.536), (1.095, -0.747), 'line_11_1_1')
    .segment((1.145, -0.661), 'line_11_1_2')
    .segment((1.195, -0.574), 'line_11_1_3')
    .segment((0.785, -0.287), 'line_11_1_4')
    .arc((0.724, -0.418), (0.641, -0.536), 'arc_11_1_5')
    .assemble()
)

profile_12 = (
    cq.Sketch()
    # loop_12_1
    .segment((0.824, -0.144), (1.322, -0.1), 'line_12_1_1')
    .segment((1.322, 0.0), 'line_12_1_2')
    .segment((1.322, 0.1), 'line_12_1_3')
    .segment((0.824, 0.144), 'line_12_1_4')
    .arc((0.836, 0.0), (0.824, -0.144), 'arc_12_1_5')
    .assemble()
)

profile_13 = (
    cq.Sketch()
    # loop_13_1
    .arc((0.0, 0.0), 0.836, 0.0, 360.0, 'circle_13_1_1')
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

extrude_1 = cq.Workplane('XY').placeSketch(sketch_1).extrude(2.0, both=False)
result = extrude_1
profile_1 = (
    cq.Sketch()
    # loop_1_1
    .arc((0.0, 0.0), 0.25, 0.0, 360.0, 'circle_1_1_1')
    .assemble()
)

sketch_2 = profile_1

extrude_2 = cq.Workplane().copyWorkplane(extrude_1.faces(DirectionSelector(cq.Vector(0.0, 0.0, 1.0))).workplane()).placeSketch(sketch_2).extrude(-25.0, both=False)
result = result.cut(extrude_2)
show_object(result)