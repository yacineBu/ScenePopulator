import bpy
from bpy.types import Panel
from . Props import Props

class MainPanel(Panel):
    bl_idname = "VIEW3D_PT_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Population settings"
    bl_category = "Scene populator"

    areaParamProps = ("quantity_SP", "xCenter_SP", "yCenter_SP", "sideLength_SP")

    def draw(self, context):
        row = self.layout.row()
        row.label(text="area parameters")
        for (propName) in self.areaParamProps:
            newRow = self.layout.row()
            newRow.prop(context.scene, propName)
       
        row = self.layout.row()
        row.operator("object.generate", text="Generate")
