import bpy
from bpy.types import Operator
import random

class Generate(Operator):
    bl_idname = "object.generate"       # Associe l'opération à un bouton du panneau
    bl_label = "Generate"
    bl_description = "La description affichée au survol"

    def execute(self, context):
        activeObj = context.view_layer.objects.active
        scene = context.scene
        
        self.generateIdenticalObj(activeObj, scene.quantity_SP, scene.radius_SP, scene.xCenter_SP, scene.yCenter_SP)
        return {'FINISHED'}
    
    def generateIdenticalObj(self, activeObj, quantity, radius, xCenter, yCenter):
        for i in range(quantity):
            generatedObj = bpy.data.objects.new("Obj", activeObj.data)
            # Ici, essayer d'utiliser plutôt l'opération de duplication, peut etre ca crashera plus
            
            x = xCenter + random.random()*radius
            y = yCenter + random.random()*radius
            z = 0.0
            # z à l'avenir : sera défini selon la hauteur du terrain relevée à la position x et y
            generatedObj.location = (x,y,z)

            bpy.context.view_layer.active_layer_collection.collection.objects.link(generatedObj)

    def generateCube(self, quantity, radius, xCenter, yCenter):
        # Sommets et faces d'un simple cube défini ici
        verts = [(0,0,0),(2,0,0),(2,2,0),(0,2,0),(0,0,2),(2,0,2),(2,2,2),(0,2,2)]
        faces = [(0,1,2,3),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]

        for i in range(quantity):
            meshCube = bpy.data.meshes.new("Cube")
            objCube = bpy.data.objects.new("Cube", meshCube)
            
            x = xCenter + random.random()*radius
            y = yCenter + random.random()*radius
            z = 0.0
            # z à l'avenir : sera défini selon la hauteur du terrain relevée à la position x et y

            objCube.location = (x,y,z)
            bpy.context.view_layer.active_layer_collection.collection.objects.link(objCube)

            meshCube.from_pydata(verts, [], faces)