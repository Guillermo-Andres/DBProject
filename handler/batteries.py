from flask import jsonify
from dao.batteries import BatteryDAO


class BatteryHandler:
    def build_battery_dict(self, row):
        result = {}
        result['battery_id'] = row[0]
        result['type'] = row[1]
        result['unit_size'] = row[2]
        


        return result



    def getAllbattery(self):
        dao = BatteryDAO()
        battery_list = dao.getAllBatteries()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(battery=result_list)
