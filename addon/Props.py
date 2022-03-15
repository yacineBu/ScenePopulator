import bpy

class Props:

    props = bpy.props
    addonProps = (
        ("quantity_SP", props.IntProperty(name="Quantity")),
        ("xCenter_SP", props.IntProperty(name="X Center")),
        ("yCenter_SP", props.IntProperty(name="Y Center")),
        ("sideLength_SP", props.FloatProperty(name="Side length"))
    )

    # def __getattribute__(self, __name: addonProps):
    #     pass