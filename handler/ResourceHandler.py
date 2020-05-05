from handler.babyFood import babyFoodHandler
from handler.cannedFood import cannedFoodHandler
from handler.dryFood import dryFoodHandler
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
        if(type == 'babyfood'):
            return babyFoodHandler().getAllbabyFood()
        elif(type == 'dryfood'):
            return dryFoodHandler().getAlldryFood()
        elif(type == 'cannedfood'):
            return cannedFoodHandler().getAllcannedFood()
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
        elif(type == 'medicaldevices'):
            return MedicalDevicesHandler().getAllMedicalDevices()
        elif(type == 'powergenerator'):
            return PowerGeneratorHandler().getAllPowerGenerator()
        elif(type == 'hygiene'):
            return HygieneHandler().getAllHygiene()
        elif(type == 'water'):
            return WaterHandler().getAllWater()

        else:
            return MedicationHandler().getAllMedication()

    def getHandler(self , type):
        if(type == 'babyfood'):
            return babyFoodHandler()
        elif(type == 'dryfood'):
            return dryFoodHandler()
        elif(type == 'cannedfood'):
            return cannedFoodHandler()
        elif(type == 'medication'):
            return MedicationHandler()
        elif(type == 'batteries'):
            return BatteryHandler()
        elif(type == 'clothing'):
            return ClothingHandler()
        elif(type == 'heavyequipment'):
            return HeavyEquipmentHandler()
        elif(type == 'ice'):
            return IceHandler()
        elif(type == 'powertools'):
            return PowerToolsHandler()
        elif(type == 'fuel'):
            return FuelHandler()
        elif(type == 'medicaldevices'):
            return MedicalDevicesHandler()
        elif(type == 'powergenerator'):
            return PowerGeneratorHandler()
        elif(type == 'hygiene'):
            return HygieneHandler()
        elif(type == 'water'):
            return WaterHandler()

        else:
            return MedicationHandler()

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
