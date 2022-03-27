import bpy
from bpy.types import Panel
from . Props import Props

class MainPanel(Panel):
    bl_idname = "VIEW3D_PT_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Population settings"
    bl_category = "Scene populator"

    areaParamProps = ("xCenter_SP", "yCenter_SP", "sideLength_SP")
    scaleVarProps = ("XScaleVar_SP", "YScaleVar_SP", "ZScaleVar_SP")
    rotationVarProps = ("XRotationVar_SP", "YRotationVar_SP", "ZRotationVar_SP")


    def draw(self, context):
        row = self.layout.row()
        row.label(text="Area parameters")
        for (propName) in self.areaParamProps:
            newRow = self.layout.row()
            newRow.prop(context.scene, propName)

        newRow = self.layout.row()
        newRow.prop_search(context.scene, "terrainObjName_SP", context.scene, "objects")
        # prop_search() créer un champs où l'utilisateur pourra sélectionner un object parmi 
        # les objets dans "context.scene.objects". Le nom de cet objet sera ensuite sauvegardé 
        # dans "context.scene.terrainObjName_SP"

        newRow = self.layout.row()
        newRow.label(text="Object generation parameters")

        newRow = self.layout.row()
        newRow.prop(context.scene, "quantity_SP")
        
        newRow = self.layout.row()
        newRow.label(text="Scale variations")

        for (propName) in self.scaleVarProps:
            newRow = self.layout.row()
            newRow.prop(context.scene, propName)

        newRow = self.layout.row()
        newRow.label(text="Rotation variations")

        for (propName) in self.rotationVarProps:
            newRow = self.layout.row()
            newRow.prop(context.scene, propName)

        row = self.layout.row()
        row.operator("object.generate", text="Generate")
