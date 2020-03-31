from flask import jsonify
from dao.ice import IceDAO
    #ICE ATTTRIBUTES iid, size,unit_size,description,price,location,quantity


class IceHandler:
    def build_Ice_dict(self, row):
        result = {}
        result['ice_id'] = row[0]
        result['size'] = row[1]
        result['unit_size'] = row[2]
        result['description'] = row[3]

        return result

    def getAllIce(self):

        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def getIceByUnitSize(self, id):
        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def getIceBySize(self,size):
        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def getIceByPrice(self,price):
        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def getIceByLocation(self,location):
        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)
