from flask import jsonify
from dao.powertools import ToolsDAO

    #powertools ATTTRIBUTES tool id, type, description

class PowerToolsHandler:
    def build_Tools_dict(self, row):
        result = {}
        result['tool_id'] = row[0]
        result['type'] = row[1]
        result['description'] = row[2]





        return result



    def getAllTools(self):
        dao = ToolsDAO()
        tools_list = dao.getAllTools()
        result_list = []
        for row in tools_list:
            result = self.build_Tools_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)
