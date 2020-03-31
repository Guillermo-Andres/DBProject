from flask import jsonify
from dao.heavyequipment import HeavyEquipmentDAO
#HeavyEquipment ATTTRIBUTES heavy_id, description


class HeavyEquipmentHandler:
    def build_heavyE_dict(self, row):
        result = {}
        result['heavy_id'] = row[0]
        result['description'] = row[1]
        result['price'] = row[2]
        result['location'] = row[3]
        result['quantity'] = row[4]


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
        HE_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)


    def getHeavyEquipmentByPrice(self, price):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def getHeavyEquipmentByLocation(self, location):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def insert(self, sname, scity, sphone):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def update(self):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def delete(self):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)
