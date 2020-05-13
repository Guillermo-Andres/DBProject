from config.dbconfig import pg_config
from dao.water import WaterDAO
from flask import jsonify
import psycopg2
class WaterHandler:

    def build_water_dict(self , row):
        waterdict = {}

        waterdict['resource_id'] = row[0]
        waterdict['water_id'] = row[0]
        waterdict['size'] = row[1]
        waterdict['brand'] = row[2]
        waterdict['type'] = row[3]
        waterdict['unit_size'] = row[4]
        waterdict['name'] = row[5]
        waterdict['price'] = row[6]
        waterdict['location'] = row[7]
        waterdict['quantity'] = row[8]
        waterdict['description'] = row[9]

        return waterdict

    def getAllResourceByKeyword(self , keyword):
        dao = WaterDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)


    def getAllWater(self):
        dao = WaterDAO()
        water = dao.getAllWater()
        result_list = []
        for row in water:
            result = self.build_water_dict(row)
            result_list.append(result)

        return jsonify(Water=result_list)


    def getWaterById(self, id):
        dao = WaterDAO()
        water = dao.getWaterById(id)
        result_list = []
        for row in water:
            result = self.build_water_dict(row)
            result_list.append(result)

        return jsonify(Water=result_list)


    # def getWaterBySize(self, size):
    #     dao = WaterDAO()
    #     water = dao.getAllWater()
    #     result_list = []
    #     for row in water:
    #         result = self.build_water_dict(row)
    #         result_list.append(result)
    #
    #     return jsonify(Water=result_list)
    #
    #
    # def getWaterByPrice(self,price):
    #     dao = WaterDAO()
    #     water = dao.getAllWater()
    #     result_list = []
    #     for row in water:
    #         result = self.build_water_dict(row)
    #         result_list.append(result)
    #
    #     return jsonify(Water=result_list)
    #
    #
    # def getWaterByLocation(self,location):
    #     dao = WaterDAO()
    #     water = dao.getAllWater()
    #     result_list = []
    #     for row in water:
    #         result = self.build_water_dict(row)
    #         result_list.append(result)
    #
    #     return jsonify(Water=result_list)
    #
    #
    # def getWaterByType(self,location):
    #     dao = WaterDAO()
    #     water = dao.getAllWater()
    #     result_list = []
    #     for row in water:
    #         result = self.build_water_dict(row)
    #         result_list.append(result)
    #
    #     return jsonify(Water=result_list)


    def insert(self,item):
        return jsonify(Water= item) ,200

    def delete(self,item):
        return jsonify(Water= item) ,200


    def update(self,item):
        return jsonify(Water= item) ,200
