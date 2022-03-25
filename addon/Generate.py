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
        
        self.generateIdenticalObj(activeObj, scene.quantity_SP, scene.sideLength_SP, scene.xCenter_SP, scene.yCenter_SP, "")
        return {'FINISHED'}
    
    # A partir d'ici, BIEN DIFFERENCIER 2 CHOSES :
    #   1) La liste de SOMMETS, contenant des objets de type "bpy.types.MeshVertex"
    #   2) La liste de COORDONNEES, contenant des LISTES de 3 nombres

    # Trié et réduit au minimum, à l'avenir
    def getTerrainVerticesCo(self, terrainObj):
        allTerrainVerts = bpy.context.blend_data.objects['Plane'].data.vertices     # temporaire
        terrainVertsCo = list()

        for i in range(0, len(allTerrainVerts)):
            terrainVertsCo.append(allTerrainVerts[i].co)

        return terrainVertsCo

    def XYdist(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    
    def generateIdenticalObj(self, activeObj, quantity, sideLength, xCenter, yCenter, terrain):
        for i in range(quantity):
            generatedObj = bpy.data.objects.new("Obj", activeObj.data)
            # Ici, essayer d'utiliser plutôt l'opération de duplication, peut etre ca crashera plus
            
            x = xCenter - sideLength/2 + random.random()*sideLength
            y = yCenter - sideLength/2 + random.random()*sideLength

            # Recherche du sommet correspondant le plus possible aux coordonnées x y trouvées juste avant
            terrainVertsCoords = self.getTerrainVerticesCo(terrain)
            terrainVertsCoordsLen = len(terrainVertsCoords)
            bestMatchingVertCo = terrainVertsCoords[0]
            for currentVertCoIndex in range(1, terrainVertsCoordsLen):
                if self.XYdist(terrainVertsCoords[currentVertCoIndex], [x, y]) < self.XYdist(bestMatchingVertCo, [x, y]):
                    bestMatchingVertCo = terrainVertsCoords[currentVertCoIndex]

            z = bestMatchingVertCo[2]

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