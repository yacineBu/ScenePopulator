import bpy
import random

class Generator:

    # Un simple cube défini ici
    # verts = [(0,0,0),(2,0,0),(2,2,0),(0,2,0),(0,0,2),(2,0,2),(2,2,2),(0,2,2)]
    # faces = [(0,1,2,3),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]
    # meshCube = bpy.data.meshes.new("Cube")
    # objCube = bpy.data.objects.new("Cube", meshCube)

    def generateIdenticalObj(self, activeObj, quantity, radius, xCenter, yCenter):
        for i in range(quantity):
            generatedObj = bpy.data.objects.new("Obj", activeObj.data)
            
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