import bpy

class Props:

    props = bpy.props
    addonProps = (
        ("xCenter_SP", props.IntProperty(name="X Center")),
        ("yCenter_SP", props.IntProperty(name="Y Center")),
        ("sideLength_SP", props.FloatProperty(name="Side length")),
        ("terrainObjName_SP", props.StringProperty(name="Terrain")),

        ("quantity_SP", props.IntProperty(name="Quantity")),
        ("XScaleVar_SP", props.FloatProperty(name="X")),
        ("YScaleVar_SP", props.FloatProperty(name="Y")),
        ("ZScaleVar_SP", props.FloatProperty(name="Z")),
        ("XRotationVar_SP", props.FloatProperty(name="X")),
        ("YRotationVar_SP", props.FloatProperty(name="Y")),
        ("ZRotationVar_SP", props.FloatProperty(name="Z"))
    )