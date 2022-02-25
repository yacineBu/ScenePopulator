import bpy
from bpy.types import Panel

class Panel_PT_(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Population settings"
    bl_category = "Scene populator"

    def draw(self, context):
        layout = self.layout

        # Une seule colonne avec un bouton
        row = layout.row()
        col = row.column()
        col.operator("object.generate", text="Generate")
