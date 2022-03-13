import bpy
from bpy.types import Panel

class Panel_PT_(Panel):     # Panel_PT est sous-classe de Panel
    bl_idname = "VIEW3D_PT_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Population settings"
    bl_category = "Scene populator"

    props = bpy.props
    myProps = (
        ("quantity", props.IntProperty(name="quantity")),
        ("xCenter", props.IntProperty(name="X Center")),
        ("yCenter", props.IntProperty(name="Y Center")),
        ("radius", props.FloatProperty(name="radius"))
    )

    def draw(self, context):
        row = self.layout.row()
        row.label(text="area parameters")
        for (propName, osef) in self.myProps:
            newRow = self.layout.row()
            newRow.prop(context.scene, propName)
       
        row = self.layout.row()
        row.operator("object.generate", text="Generate")
