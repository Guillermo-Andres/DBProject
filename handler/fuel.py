from flask import jsonify
from dao.fuel import FuelDAO

    #Fuel ATTTRIBUTES fid, type,unit_size,description

class FuelHandler:
    def build_Fuel_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['fuel_id'] = row[1]
        result['type'] = row[2]
        result['name'] = row[3]
        result['price'] = row[4]
        result['location'] = row[5]
        result['quantity'] = row[6]
        result['descrition']= row[7]


        return result

    def getAllResourceByKeyword(self , keyword):
        dao = FuelDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllFuel(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def getFuelById(self, id):
        dao = FuelDAO()
        fuel_list = dao.getFuelById(id)
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    # def getFuelByType(self, type):
    #      dao = FuelDAO()
    #      fuel_list = dao.getAllFuel()
    #      result_list = []
    #      for row in fuel_list:
    #          result = self.build_Fuel_dict(row)
    #          result_list.append(result)
    #      return jsonify(Fuel=result_list)
    #
    # def getFuelBySize(self, size):
    #     dao = FuelDAO()
    #     fuel_list = dao.getAllFuel()
    #     result_list = []
    #     for row in fuel_list:
    #         result = self.build_Fuel_dict(row)
    #         result_list.append(result)
    #     return jsonify(Fuel=result_list)
    #
    # def getFuelByPrice(self, price):
    #     dao = FuelDAO()
    #     fuel_list = dao.getAllFuel()
    #     result_list = []
    #     for row in fuel_list:
    #         result = self.build_Fuel_dict(row)
    #         result_list.append(result)
    #     return jsonify(Fuel=result_list)

    def getFuelByLocation(self, location):
        dao = FuelDAO()
        fuel_list = dao.getFuelByLocation(location)
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def insert(self, item):
        return jsonify(Fuel= item) ,200

    def delete(self, pid):
        return jsonify(Fuel= item) ,200


    def update(self, pid):
        return jsonify(Fuel= item) ,200
