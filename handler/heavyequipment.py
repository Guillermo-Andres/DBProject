from flask import jsonify
from dao.heavyequipment import HeavyEquipmentDAO
#HeavyEquipment ATTTRIBUTES heavy_id, description


class HeavyEquipmentHandler:
    def build_heavyE_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['heavy_id'] = row[1]
        result['type'] = row[2]
        result['name'] = row[3]
        result['price'] = row[4]
        result['location'] = row[5]
        result['quantity'] = row[6]
        result['description'] = row[7]






        return result

    def getAllHeavyEquipment(self):

        dao = HeavyEquipmentDAO()
        HE_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def getHeavyEquimentById(self, id):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getHeavyEquimentById(id)
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)


    def getHeavyEquipmentByPrice(self, price):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getHeavyEquipmentByPrice(price)
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def getHeavyEquipmentByLocation(self, location):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getHeavyEquipmentByLocation(location)
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def insert(self, item):
        return jsonify(HeavyEquiment= item) ,200


    def update(self,item):
        return jsonify(HeavyEquiment= item) ,200

    def delete(self,item):
        return jsonify(HeavyEquiment= item) ,200
