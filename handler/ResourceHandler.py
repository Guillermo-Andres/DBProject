from handler.babyFood import babyFoodHandler
from handler.medication import MedicationHandler
from handler.batteries import BatteryHandler
from handler.clothing import ClothingHandler
from handler.heavyequipment import HeavyEquipmentHandler
from handler.ice import IceHandler
from handler.powertools import PowerToolsHandler
from handler.fuel import FuelHandler
from handler.medicalDevices import MedicalDevicesHandler
from handler.powerGenerator import PowerGeneratorHandler
from handler.hygiene import HygieneHandler
from handler.water import WaterHandler
from dao.resource import ResourceDAO
from flask import jsonify


class ResourceHandler:


    def build_resource_dict(self , row):
        result = {} 
        result['resource_i'] = row[0]
        result['resource_name'] = row[1]
        result['resource_price'] = row[2]
        result['resource_location'] = row[3]
        result['resource_quantity'] = row[4]
        result['resource_available'] = row[5]
        result['resource_description'] = row[7]

        return result

    def getAllByType(self , type):
        if(type == 'food'):
            return babyFoodHandler().getAllFood()
        elif(type == 'medication'):
            return MedicationHandler().getAllMedication()
        elif(type == 'batteries'):
            return BatteryHandler().getAllbattery()
        elif(type == 'clothing'):
            return ClothingHandler().getAllClothes()
        elif(type == 'heavyequipment'):
            return HeavyEquipmentHandler().getAllHeavyEquipment()
        elif(type == 'ice'):
            return IceHandler().getAllIce()
        elif(type == 'powertools'):
            return PowerToolsHandler().getAllTools()
        elif(type == 'fuel'):
            return FuelHandler().getAllFuel()
        elif(type == 'diapers'):
            return MedicalDevicesHandler().getAllMedicalDevices()
        elif(type == 'femeninehygiene'):
            return PowerGeneratorHandler().getAllPowerGenerator()
        elif(type == 'hygiene'):
            return HygieneHandler().getAllHygiene()
        elif(type == 'water'):
            return WaterHandler().getAllWater()

        else:
            return MedicationHandler().getAllMedication()

    def getAll(self):
        items = ResourceDAO().getAllResource()
        result = []
        for i in items:
            toAdd = self.build_resource_dict(i)
            result.append(toAdd)

        return jsonify(Resources = result)
