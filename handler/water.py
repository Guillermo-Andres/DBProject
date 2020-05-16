from config.dbconfig import pg_config
from dao.water import WaterDAO
from flask import jsonify
import psycopg2
class WaterHandler:

    def build_water_dict(self , row):
        waterdict = {}

        waterdict['resource_id'] = row[0]
        waterdict['water_id'] = row[1]
        waterdict['size'] = row[2]
        waterdict['brand'] = row[3]
        waterdict['type'] = row[4]
        waterdict['unit_size'] = row[5]
        waterdict['name'] = row[6]
        waterdict['price'] = row[7]
        waterdict['location'] = row[8]
        waterdict['quantity'] = row[9]
        waterdict['description'] = row[10]
        waterdict['date'] = row[11]

        return waterdict

    def build_attribute_dict(self,wsize,wbrand,wtype,wunitsz,rname,rprice,resource_location,resource_quantity,resource_date, resource_description):
        item = {}
        item['water_size'] = wsize
        item['water_brand'] = wbrand
        item['water_type'] = wtype
        item['water_unitsize'] = wunitsz
        item['resource_name'] = rname
        item['resource_price'] = rprice
        item['resource_location'] = resource_location
        item['resource_quantity'] = resource_quantity
        item['resource_date'] = resource_date
        item['resource_description'] = resource_description

        return item

    def getAllWater(self):
        dao = WaterDAO()
        water = dao.getAllWater()
        result_list = []
        for row in water:
            print(row)
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


    def insert(self, item,supplier_id):
        wsize = item['water_size']
        wbrand = item['water_brand']
        wtype = item['water_type']
        wunitsz = item['water_unitsize']
        rname = item['resource_name']
        rprice = item['resource_price']
        resource_location = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_date = item['resource_date']
        resource_description = item['resource_description']
        if wsize and wbrand and wtype and wunitsz and rname and rprice and resource_location and resource_quantity and resource_date and resource_description:
            dao = WaterDAO()
            rid = dao.insert(rname, rprice,resource_location,resource_quantity,resource_description,resource_date,wsize,wbrand,wtype,wunitsz,supplier_id)
            return jsonify(water=self.build_attribute_dict(wsize,wbrand,wtype,wunitsz,rname,rprice,resource_location,resource_quantity,resource_date, resource_description)), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


    def getAllResourceByKeyword(self , keyword):
        dao = WaterDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_Water_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)
