import bpy

class Props:

    props = bpy.props
    addonProps = (
        ("quantity_SP", props.IntProperty(name="quantity")),
        ("xCenter_SP", props.IntProperty(name="X Center")),
        ("yCenter_SP", props.IntProperty(name="Y Center")),
        ("radius_SP", props.FloatProperty(name="radius"))
    )

    # def __getattribute__(self, __name: addonProps):
    #     pass