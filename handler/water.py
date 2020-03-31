from config.dbconfig import pg_config
from dao.water import WaterDAO
from flask import jsonify
import psycopg2
class WaterHandler:
    #ICE ATTTRIBUTES wiid, size,brand,type,unit_size, price,location,quantity

    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)


    def build_water_dict(self , row):
        waterdict = {}

        waterdict['id'] = row[0]
        waterdict['size'] = row[1]
        waterdict['brand'] = row[2]
        waterdict['type'] = row[3]
        waterdict['unit_size'] = row[4]
        waterdict['price'] = row[5]
        waterdict['location'] = row[6]
        waterdict['quantity'] = row[7]

        return waterdict


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
        water = dao.getAllWater()
        result_list = []
        for row in water:
            result = self.build_water_dict(row)
            result_list.append(result)

        return jsonify(Water=result_list)


    def getWaterBySize(self, size):
        dao = WaterDAO()
        water = dao.getAllWater()
        result_list = []
        for row in water:
            result = self.build_water_dict(row)
            result_list.append(result)

        return jsonify(Water=result_list)


    def getWaterByPrice(self,price):
        dao = WaterDAO()
        water = dao.getAllWater()
        result_list = []
        for row in water:
            result = self.build_water_dict(row)
            result_list.append(result)

        return jsonify(Water=result_list)


    def getWaterByLocation(self,location):
        dao = WaterDAO()
        water = dao.getAllWater()
        result_list = []
        for row in water:
            result = self.build_water_dict(row)
            result_list.append(result)

        return jsonify(Water=result_list)


    def getWaterByType(self,location):
        dao = WaterDAO()
        water = dao.getAllWater()
        result_list = []
        for row in water:
            result = self.build_water_dict(row)
            result_list.append(result)

        return jsonify(Water=result_list)


    def insert(self,item):
        return jsonify(Water= item) ,200

    def delete(self,item):
        return jsonify(Water= item) ,200


    def update(self,item):
        return jsonify(Water= item) ,200
