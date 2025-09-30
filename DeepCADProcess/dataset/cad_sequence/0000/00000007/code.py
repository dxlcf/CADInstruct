import cadquery as cq
from cadquery.selectors import DirectionSelector, NearestToPointSelector

profile_1 = (
    cq.Sketch()
    # loop_1_1
    .arc((0.0, 0.0), 91.049, 0.0, 360.0, 'circle_1_1_1')
    .assemble()
)

sketch_1 = profile_1

extrude_1 = cq.Workplane('XY').placeSketch(sketch_1).extrude(25.4, both=False)
result = extrude_1
show_object(result)