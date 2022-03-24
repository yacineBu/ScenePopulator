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
        
        self.generateIdenticalObj(activeObj, scene.quantity_SP, scene.sideLength_SP, scene.xCenter_SP, scene.yCenter_SP)
        return {'FINISHED'}
    
    # Trié à l'avenir potentiellement
    def getVerticesOfTerrain(self, terrainObj):
        """
        >>> for i in range(0, 10):
...     bpy.context.blend_data.objects['Plane'].data.vertices[i].co
...     
        Vector((-48.96240997314453, -48.96240997314453, 4.66356897354126))
        Vector((48.96240997314453, -48.96240997314453, -1.244048833847046))
        Vector((-48.96240997314453, 48.96240997314453, 4.527307987213135))
        Vector((48.96240997314453, 48.96240997314453, -4.258199214935303))
        Vector((-50.00000762939453, 0.0, 3.051168203353882))
        Vector((0.0, -50.00000762939453, 2.074270725250244))
        Vector((50.00000762939453, 0.0, -5.987868309020996))
        Vector((0.0, 50.00000762939453, 1.761354684829712))
        Vector((0.0, -4.470348358154297e-08, -0.40681424736976624))
        Vector((-50.00000762939453, -25.000001907348633, 4.601046085357666))
        """
    
    def generateIdenticalObj(self, activeObj, quantity, sideLength, xCenter, yCenter):
        for i in range(quantity):
            generatedObj = bpy.data.objects.new("Obj", activeObj.data)
            # Ici, essayer d'utiliser plutôt l'opération de duplication, peut etre ca crashera plus
            
            x = xCenter - sideLength/2 + random.random()*sideLength
            y = yCenter - sideLength/2 + random.random()*sideLength
            z = 0.0
            # z à l'avenir : sera défini selon la hauteur du terrain relevée à la position x et y
            generatedObj.location = (x,y,z)

            bpy.context.view_layer.active_layer_collection.collection.objects.link(generatedObj)

    def generateCube(self, quantity, sideLength, xCenter, yCenter):
        # Sommets et faces d'un simple cube défini ici
        verts = [(0,0,0),(2,0,0),(2,2,0),(0,2,0),(0,0,2),(2,0,2),(2,2,2),(0,2,2)]
        faces = [(0,1,2,3),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]

        for i in range(quantity):
            meshCube = bpy.data.meshes.new("Cube")
            objCube = bpy.data.objects.new("Cube", meshCube)
            
            x = xCenter + random.random()*sideLength
            y = yCenter + random.random()*sideLength
            z = 0.0
            # z à l'avenir : sera défini selon la hauteur du terrain relevée à la position x et y

            objCube.location = (x,y,z)
            bpy.context.view_layer.active_layer_collection.collection.objects.link(objCube)

            meshCube.from_pydata(verts, [], faces)