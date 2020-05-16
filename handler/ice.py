from flask import jsonify
from dao.ice import IceDAO
    #ICE ATTTRIBUTES iid, size,unit_size,description,price,location,quantity


class IceHandler:
    def build_Ice_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['ice_id'] = row[1]
        result['ice_size'] = row[2]
        result['name'] = row[3]
        result['price'] = row[4]
        result['location'] = row[5]
        result['quantity']=row[6]
        result['description']=row[7]
        result['date']=row[8]


        return result

    def build_ice_attributes(self, unit_size):
        result = {   'ice_size': unit_size   }
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


    def getIceByLocation(self,location):
        dao = IceDAO()
        ice_list = dao.getIceByLocation(location)
        result_list = []
        for row in ice_list:
            result = self.build_Ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def insert(self, item,supplier_id):
        size = item['ice_size']
        rname = item['resource_name']
        rprice = item['resource_price']
        resource_location = item['resource_location']
        resource_quantity = item['resource_quantity']
        resource_date = item['resource_date']
        resource_description = item['resource_description']
        if size and rname and rprice and resource_location and resource_quantity and resource_date and resource_description:
            dao = IceDAO()
            rid = dao.insert(size, rname, rprice,resource_location,resource_quantity,resource_description,resource_date,supplier_id)
            return jsonify(Ice=self.build_ice_attributes(size)), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
