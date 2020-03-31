from flask import jsonify
from dao.fuel import FuelDAO

    #Fuel ATTTRIBUTES fid, type,unit_size,description

class FuelHandler:
    def build_Fuel_dict(self, row):
        result = {}
        result['fuel_id'] = row[0]
        result['type'] = row[1]
        result['unit_size'] = row[2]
        result['description'] = row[3]
        result['price'] = row[4]
        result['location'] = row[5]
        result['quantity'] = row[6]

        return result



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
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

     def getFuelByType(self, type):
         dao = FuelDAO()
         fuel_list = dao.getAllFuel()
         result_list = []
         for row in fuel_list:
             result = self.build_Fuel_dict(row)
             result_list.append(result)
         return jsonify(Fuel=result_list)

    def getFuelBySize(self, size):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def getFuelByPrice(self, price):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def getFuelByLocation(self, location):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def insert(self, pname, pcolor, pmaterial, pprice):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def delete(self, pid):
         dao = FuelDAO()
         fuel_list = dao.getAllFuel()
         result_list = []
         for row in fuel_list:
             result = self.build_Fuel_dict(row)
             result_list.append(result)
         return jsonify(Fuel=result_list)

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)
