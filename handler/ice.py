from flask import jsonify
from dao.ice import IceDAO
    #ICE ATTTRIBUTES iid, size,unit_size,description,price,location,quantity


class IceHandler:
    def build_Ice_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['ice_id'] = row[1]
        result['unit_size'] = row[2]
        result['name'] = row[3]
        result['price'] = row[4]
        result['location'] = row[5]
        result['quantity']=row[6]
        result['description']=7

        return result


    def getAllResourceByKeyword(self , keyword):
        dao = IceDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)


    def getAllIce(self):

        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def getIceById(self, id):
        dao = IceDAO()
        ice_list = dao.getIceById(id)
        result_list = []
        for row in ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    # def getIceBySize(self,size):
    #     dao = IceDAO()
    #     ice_list = dao.getAllIce()
    #     result_list = []
    #     for row in ice_list:
    #         result = self.build_Ice_dict(row)
    #         result_list.append(result)
    #     return jsonify(Ice=result_list)
    #
    # def getIceByPrice(self,price):
    #     dao = IceDAO()
    #     ice_list = dao.getAllIce()
    #     result_list = []
    #     for row in ice_list:
    #         result = self.build_Ice_dict(row)
    #         result_list.append(result)
    #     return jsonify(Ice=result_list)

    def getIceByLocation(self,location):
        dao = IceDAO()
        ice_list = dao.getIceByLocation(location)
        result_list = []
        for row in ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def insert(self,item):
        return jsonify(Ice= item) ,200

    def delete(self,item):
        return jsonify(Ice= item) ,200


    def update(self,item):
        return jsonify(Ice= item) ,200
