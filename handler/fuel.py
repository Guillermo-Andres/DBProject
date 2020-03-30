from flask import jsonify
from dao.fuel import FuelDAO

    #Fuel ATTTRIBUTES fid, type,unit_size,description

class FuelHandler:
    def build_Fuel_dict(self, row):
        result = {}
        result['food_id'] = row[0]
        result['type'] = row[1]
        result['unit_size'] = row[2]
        result['description'] = row[3]

        return result



    def getAllFuel(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)
