import bpy
from . Generator import Generator       # faire ca à la place, "import generator" ne marche pas
from bpy.types import Operator

class Operator_OT_(Operator):
    bl_idname = "object.generate"       # Associe l'opération à un bouton du panneau
    bl_label = "Generate"
    bl_description = "La description affichée au survol"

    # 
    # Enable or disable Operator depending yes or no an object is selected
    #
    # @classmethod
    # def poll(cls, context):
    #     obj = context.object

    #     if obj is not None:
    #         if obj.mode == "OBJECT":
    #             return True
        
    #     return False

    def execute(self, context):
        activeObj = context.view_layer.objects.active
        scene = context.scene
        
        myGenerator = Generator()
        myGenerator.generateIdenticalObj(activeObj, scene.quantity, scene.radius, scene.xCenter, scene.yCenter)
        return {'FINISHED'}