from flask import jsonify
from dao.batteries import BatteryDAO


class BatteryHandler:
    def build_battery_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['battery_id'] = row[1]
        result['type'] = row[2]
        result['unit_size'] = row[3]
        result['price'] = row[4]
        result['location'] = row[5]
        result['quantity'] = row[5]

        return result



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


    # def getBatteryByType(self, type):
    #     dao = BatteryDAO()
    #     battery_list = dao.getAllBatteries()
    #     result_list = []
    #     for row in battery_list:
    #         result = self.build_battery_dict(row)
    #         result_list.append(result)
    #     return jsonify(battery=result_list)
    #
    #
    # def getBatteryByPrice(self,prince):
    #     dao = BatteryDAO()
    #     battery_list = dao.getAllBatteries()
    #     result_list = []
    #     for row in battery_list:
    #         result = self.build_battery_dict(row)
    #         result_list.append(result)
    #     return jsonify(battery=result_list)


    def getBatteryByLocaion(self,location):
        dao = BatteryDAO()
        battery_list = dao.getBatteryByLocaion(location)
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)

    def insert(self, item):
        return jsonify(Batteries= item) ,200


    def delete(self, item):
        return jsonify(Batteries= item) ,200

    def update(self, item):
        return jsonify(Batteries= item) ,200
