from handler.food import FoodHandler
from handler.medication import MedicationHandler
from handler.batteries import BatteryHandler
from handler.clothing import ClothingHandler
from handler.heavyequipment import HeavyEquipmentHandler
from handler.ice import IceHandler
from handler.powertools import PowerToolsHandler
from handler.fuel import FuelHandler
from handler.diapers import DiapersHandler
from handler.femenine_hygiene import FemenineHygieneHandler
from handler.hygiene import HygieneHandler
from handler.water import WaterHandler


class ResourceHandler:

    def getAllByType(self , type):
        if(type == 'food'):
            return FoodHandler().getAllFood()
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
            return DiapersHandler().getAllDiapers()
        elif(type == 'femeninehygiene'):
            return FemenineHygieneHandler().getAllFemenineHygiene()
        elif(type == 'hygiene'):
            return HygieneHandler().getAllHygiene()
        elif(type == 'water'):
            return WaterHandler().getAllWater()

        else:
            return MedicationHandler().getAllMedication()

        def getAll(self):
            return [HygieneHandler().getAllHygiene() , FoodHandler().getAllFood()]
