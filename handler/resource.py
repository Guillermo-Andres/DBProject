from dao.request import RequestDAO
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
        result['resource_description'] = row[5]

        return result

    def build_resource_attributes(self, resource_id, resource_price, resource_location, resource_quantity):
        result = {'resource_id': resource_id,
                  'resource_price': resource_price,
                  'resource_location': resource_location,
                  'resource_quantity': resource_quantity}
        return result

    def build_resource_stats_per_date_dict(self, row):
        result = {
            'resource_name': row[0],
            'quantity': row[1],
            'date': row[2]
        }
        return result

    def build_reqs_stats_per_region_dict(self, row):
        result = {
            'resource_name': row[0],
            'available': row[1],
            'region': row[2]
        }
        return result

    def getAllByType(self , type):
        print(type)
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
        elif(type == 'tools'):
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

    def getAll(self):
        items = ResourceDAO().getAllResource()
        result = []
        for i in items:
            toAdd = self.build_resource_dict(i)
            result.append(toAdd)

        return jsonify(Resources = result)

    def getAllResources(self):
        dao = ResourceDAO()
        resources_list = dao.getAllResource()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, resource_id):
        dao = ResourceDAO()
        row = dao.getResourceById(resource_id)
        if not row:
            return jsonify(Error='Resource not found'), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    def getResourcesInStock(self):
        dao = ResourceDAO()
        resources_list = dao.getResourcesInStock()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceInRequest(self, request_id):
        dao = RequestDAO()
        row = dao.getResourceInRequest(request_id)
        if not row:
            return jsonify(Error='Resource not found'), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    def getAllResourceByKeyword(self , keyword):
        dao = ResourceDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceAvailablePerDay(self):
        dao = ResourceDAO()
        resource_list = dao.getResourceAvailablePerDay()
        result_list = []
        for row in resource_list:
            result = self.build_resource_stats_per_date_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def getResourceAvailablePerWeek(self):
        dao = ResourceDAO()
        resource_list = dao.getResourceAvailablePerWeek()
        result_list = []
        for row in resource_list:
            result = self.build_resource_stats_per_date_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

    def getResourceAvailablePerRegion(self):
        dao = ResourceDAO()
        resource_list = dao.getResourceAvailablePerRegion()
        result_list = []
        for row in resource_list:
            result = self.build_reqs_stats_per_region_dict(row)
            result_list.append(result)
        return jsonify(Resource=result_list)

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