from flask import jsonify
from dao.powertools import ToolsDAO

    #powertools ATTTRIBUTES tool id, type, description

class PowerToolsHandler:
    def build_Tools_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['tool_id'] = row[0]
        result['tools_type'] = row[1]
        result['name']=row[2]
        result['price'] = row[3]
        result['location'] = row[4]
        result['quantity'] = row[5]
        result['description'] = row[6]

        return result

    def build_attribute_dict (self, ttype,rname,rprice,resource_location,resource_quantity,resource_date, resource_description):
        item = {}
        item['tools_type'] = ttype
        item['resource_name'] = rname
        item['resource_price'] = rprice
        item['resource_location'] = resource_location
        item['resource_quantity'] = resource_quantity
        item['resource_date'] = resource_date
        item['resource_description'] = resource_description




    def getAllTools(self):
        dao = ToolsDAO()
        tools_list = dao.getAllTools()
        result_list = []
        for row in tools_list:
            result = self.build_Tools_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)

    def getToolById(self, id):
        dao = ToolsDAO()
        tools_list = dao.getToolById(id)
        result_list = []
        for row in tools_list:
            result = self.build_Tools_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)

    def getToolByType(self, color):
        dao = ToolsDAO()
        tools_list = dao.getAllTools()
        result_list = []
        for row in tools_list:
            result = self.build_Tools_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)


    def insert(self, item):
        ttype = item['tools_type']
        rname = item['resource_name']
        rprice = item['resource_price']
        resource_location = item['resource_location']
        resource_quantity = item['resource_quantity']
        resource_date = item['resource_date']
        resource_description = item['resource_description']
        if ttype and rname and rprice and resource_location and resource_quantity and resource_date and resource_description:
            dao = ToolsDAO()
            rid = dao.insert(rname, rprice,resource_location,resource_quantity,resource_description,resource_date,ttype)
            return jsonify(Tools=self.build_attribute_dict(ttype,rname,rprice,resource_location,resource_quantity,resource_date, resource_description)), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
