from flask import jsonify
from dao.powertools import ToolsDAO

    #powertools ATTTRIBUTES tool id, type, description

class PowerToolsHandler:
    def build_Tools_dict(self, row):
        result = {}
        result['tool_id'] = row[0]
        result['type'] = row[1]
        result['description'] = row[2]
        result['price'] = row[3]
        result['location'] = row[4]
        result['quantity'] = row[5]

        return result



    def getAllTools(self):
        dao = ToolsDAO()
        tools_list = dao.getAllTools()
        result_list = []
        for row in tools_list:
            result = self.build_Tools_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)

    def getToolById(self, pid):
        dao = ToolsDAO()
        tools_list = dao.getAllTools()
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

    def getToolByPrice(self, color):
        dao = ToolsDAO()
        tools_list = dao.getAllTools()
        result_list = []
        for row in tools_list:
            result = self.build_Tools_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)

    def getToolByLocation(self, color):
        dao = ToolsDAO()
        tools_list = dao.getAllTools()
        result_list = []
        for row in tools_list:
            result = self.build_Tools_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)

    def insert(self,item):
        return jsonify(Tools= item) ,200

    def delete(self,item):
        return jsonify(Tools= item) ,200


    def update(self,item):
        return jsonify(Tools= item) ,200
