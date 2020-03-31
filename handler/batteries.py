from flask import jsonify
from dao.batteries import BatteryDAO


class BatteryHandler:
    def build_battery_dict(self, row):
        result = {}
        result['battery_id'] = row[0]
        result['type'] = row[1]
        result['unit_size'] = row[2]
        result['price'] = row[3]
        result['location'] = row[4]
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
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)


    def getBatteryByType(self, type):
        dao = BatteryDAO()
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)


    def getBatteryByPrice(self,prince):
        dao = BatteryDAO()
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)


    def getBatteryByLocaion(self,location):
        dao = BatteryDAO()
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)

    def insert(self, pname, pcolor, pmaterial, pprice):
        dao = BatteryDAO()
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)


    def delete(self, pid):
        dao = BatteryDAO()
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        dao = BatteryDAO()
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)        
