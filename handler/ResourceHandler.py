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


class ResourceHandler:

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
        return {
            'hygiene':HygieneHandler().getAllHygiene().get_json(),
            'food':FoodHandler().getAllFood().get_json(),
            'batteries':BatteryHandler().getAllbattery().get_json(),
            'clothing':ClothingHandler().getAllClothes().get_json(),
            'heavyEquipment':HeavyEquipmentHandler().getAllHeavyEquipment().get_json(),
            'ice':IceHandler().getAllIce().get_json(),
            'powertools':PowerToolsHandler().getAllTools().get_json(),
            'fuel':FuelHandler().getAllFuel().get_json(),
            'medicalDevices':MedicalDevicesHandler().getAllMedicalDevices().get_json(),
            'powerGenerator':PowerGeneratorHandler().getAllPowerGenerator().get_json(),
            'hygiene':HygieneHandler().getAllHygiene().get_json(),
            'water':WaterHandler().getAllWater().get_json()
        }
