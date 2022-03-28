import bpy
from bpy.types import Operator
import random
import math

class Generate(Operator):
    bl_idname = "object.generate"       # Associe l'opération à un bouton du panneau
    bl_label = "Generate"
    bl_description = "La description affichée au survol"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        activeObj = context.view_layer.objects.active   
        self.generateVariants(activeObj)
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

    def generateVariants(self, objToDerive):
        scene = bpy.context.scene
        # print("lancement de generateIdenticalObj")

        for i in range(scene.quantity_SP):
            # Duplication de l'objet sélectionné, puis je le retrouve puis le renomme direct pour le modifier plus tard
            bpy.ops.object.add_named(name=objToDerive.name)
            generatedObj = bpy.context.scene.objects[objToDerive.name + ".001"]
            generatedObj.name = "Generated" + objToDerive.name
            
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

            # Application des variations de scale
            generatedObj.scale[0] = objToDerive.scale[0] - scene.XScaleVar_SP + random.random()*(scene.XScaleVar_SP*2)
            generatedObj.scale[1] = objToDerive.scale[1] - scene.YScaleVar_SP + random.random()*(scene.YScaleVar_SP*2)
            generatedObj.scale[2] = objToDerive.scale[2] - scene.ZScaleVar_SP + random.random()*(scene.ZScaleVar_SP*2)

            # Application des variations de rotation
            generatedObj.rotation_euler[0] = objToDerive.rotation_euler[0] - math.radians(scene.XRotationVar_SP) + math.radians(random.random()*(scene.XRotationVar_SP*2))
            generatedObj.rotation_euler[1] = objToDerive.rotation_euler[1] - math.radians(scene.YRotationVar_SP) + math.radians(random.random()*(scene.YRotationVar_SP*2))
            generatedObj.rotation_euler[2] = objToDerive.rotation_euler[2] - math.radians(scene.ZRotationVar_SP) + math.radians(random.random()*(scene.ZRotationVar_SP*2))
            # tester avec un seul math.radians par ligne ?

            # for i in range(9):
            #     print(f"ce que j'ajoute : {random.random()*(scene.YRotationVar_SP*2)}")

            print(f"Resultat rot Y : {generatedObj.rotation_euler[1]}")
            