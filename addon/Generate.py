import bpy
from bpy.types import Operator
import random

class Generate(Operator):
    bl_idname = "object.generate"       # Associe l'opération à un bouton du panneau
    bl_label = "Generate"
    bl_description = "La description affichée au survol"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        activeObj = context.view_layer.objects.active   
        self.generateIdenticalObj(activeObj)
        return {'FINISHED'}
    
    # A partir d'ici, BIEN DIFFERENCIER 2 CHOSES :
    #   1) La liste de SOMMETS, contenant des objets de type "bpy.types.MeshVertex" (un type où je peux accéder aux coordonnées du sommet, mais pas que)
    #   2) La liste de COORDONNEES, contenant des LISTES de 3 nombres

    # Trié et réduit au minimum, à l'avenir
    def getTerrainVerticesCo(self, terrainObjName):
        allTerrainVerts = bpy.context.scene.objects[terrainObjName].data.vertices

        terrainVertsCo = list()

        for i in range(0, len(allTerrainVerts)):
            terrainVertsCo.append(allTerrainVerts[i].co)

        return terrainVertsCo

    def XYdist(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    
    def generateIdenticalObj(self, objToDerive):
        scene = bpy.context.scene
        # print("lancement de generateIdenticalObj")

        for i in range(scene.quantity_SP):
            # Duplication de l'objet sélectionné, puis je le retrouve puis le renomme direct pour le modifier plus tard
            bpy.ops.object.add_named(name=objToDerive.name)
            bpy.context.scene.objects[objToDerive.name + ".001"].name = objToDerive.name + str(i+2)
            generatedObj = bpy.context.scene.objects[objToDerive.name + str(i+2)]
            
            x = scene.xCenter_SP - scene.sideLength_SP/2 + random.random()*scene.sideLength_SP
            y = scene.yCenter_SP - scene.sideLength_SP/2 + random.random()*scene.sideLength_SP

            # Recherche du sommet correspondant le plus possible aux coordonnées x y trouvées juste avant
            terrainVertsCoords = self.getTerrainVerticesCo(scene.terrainObjName_SP)
            terrainVertsCoordsLen = len(terrainVertsCoords)
            bestMatchingVertCo = terrainVertsCoords[0]
            for currentVertCoIndex in range(1, terrainVertsCoordsLen):
                if self.XYdist(terrainVertsCoords[currentVertCoIndex], [x, y]) < self.XYdist(bestMatchingVertCo, [x, y]):
                    bestMatchingVertCo = terrainVertsCoords[currentVertCoIndex]

            z = bestMatchingVertCo[2]

            generatedObj.location = (x,y,z)

            # bpy.context.view_layer.active_layer_collection.collection.objects.link(generatedObj)

    def generateVariants(self, objToDerive):
        pass