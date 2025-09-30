import cadquery as cq
from cadquery.selectors import DirectionSelector, NearestToPointSelector

profile_1 = (
    cq.Sketch()
    # loop_1_1
    .segment((0.0, -254.0), (254.0, -254.0), 'line_1_1_1')
    .segment((254.0, 0.0), 'line_1_1_2')
    .segment((25.4, 0.0), 'line_1_1_3')
    .arc((17.961, -17.961), (0.0, -25.4), 'arc_1_1_4')
    .segment((0.0, -254.0), 'line_1_1_5')
    .assemble()
)

sketch_1 = profile_1

extrude_1 = cq.Workplane('XY').placeSketch(sketch_1).extrude(12.7, both=False)
result = extrude_1
show_object(result)