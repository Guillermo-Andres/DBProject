from flask import jsonify
from dao.batteries import BatteryDAO


class BatteryHandler:
    def build_battery_dict(self, row):
        result = {'resource_id': row[0], 'battery_id': row[1], 'type': row[2], 'unit_size': row[3], 'name': row[4],
                  'price': row[5], 'location': row[6], 'quantity': row[7], 'description': row[8]}
        return result

    def build_battery_attrs(self, batteries_type, batteries_quantityPerUnit, resource_name, resource_price,
                            resource_city, resource_quantity, resource_description, resource_date):
        result = {
            'batteries_type': batteries_type,
            'batteries_quantityPerUnit': batteries_quantityPerUnit,
            'resource_name': resource_name,
            'resource_price': resource_price,
            'resource_city': resource_city,
            'resource_quantity': resource_quantity,
            'resource_description': resource_description,
            'resource_date': resource_date
        }
        return result

    def getAllResourceByKeyword(self, keyword):
        dao = BatteryDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllbattery(self):
        dao = BatteryDAO()
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)

    def getBatteryById(self, id):
        dao = BatteryDAO()
        battery_list = dao.getBatteryById(id)
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)

    def getBatteryByLocation(self, location):
        dao = BatteryDAO()
        battery_list = dao.getBatteryByLocaion(location)
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)

    def insert(self, item):
        batteries_type = item['batteries_type']
        batteries_quantityPerUnit = item['batteries_quantityPerUnit']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if batteries_type and batteries_quantityPerUnit and resource_name and resource_price and resource_city and resource_quantity and resource_description and resource_date:
            dao = BatteryDAO()
            rid = dao.insert(batteries_type, batteries_quantityPerUnit, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date)
            return jsonify(Batteries=self.build_battery_attrs(batteries_type, batteries_quantityPerUnit, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date))
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400

    def delete(self, item):
        return jsonify(Batteries=item), 200

    def update(self, item):
        return jsonify(Batteries=item), 200
