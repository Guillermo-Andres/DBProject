from flask import jsonify
from dao.fuel import FuelDAO


# Fuel ATTTRIBUTES fid, type,unit_size,description

class FuelHandler:
    def build_Fuel_dict(self, row):
        result = {'resource_id': row[0], 'fuel_id': row[1], 'type': row[2], 'name': row[3], 'price': row[4],
                  'location': row[5], 'quantity': row[6], 'descrition': row[7]}
        return result

    def build_fuel_attrs(self, fuel_type, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date):
        result = {
            'fuel_type': fuel_type,
            'resource_name': resource_name,
            'resource_price': resource_price,
            'resource_city': resource_city,
            'resource_quantity': resource_quantity,
            'resource_description': resource_description,
            'resource_date': resource_date
        }
        return result

    def getAllResourceByKeyword(self, keyword):
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

    def getFuelByLocation(self, location):
        dao = FuelDAO()
        fuel_list = dao.getFuelByLocation(location)
        result_list = []
        for row in fuel_list:
            result = self.build_Fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def insert(self, item):
        fuel_type = item['fuel_type']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if fuel_type and resource_name and resource_price and resource_city and resource_quantity and resource_description and resource_date:
            dao = FuelDAO()
            rid = dao.insert(fuel_type, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date)
            return jsonify(Fuel=self.build_fuel_attrs(fuel_type, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date))
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400

    def delete(self, pid):
        return jsonify(Fuel=item), 200

    def update(self, pid):
        return jsonify(Fuel=item), 200
