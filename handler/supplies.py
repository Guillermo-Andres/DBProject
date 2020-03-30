from flask import jsonify
from dao.supplies import SuppliesDAO

class suppliesHandler:

    def build_supplies_dict(self , row ):
        result = {}

        result['supid']  = row[0]
        result['sid'] = row[1]
        result['rid'] = row[2]
        

        return result
    
    def getAllSupplies(self):
        dao = SuppliesDAO()
        supplies = []
        items = dao.getAllSupplies()

        for i in items:
            result = self.build_supplies_dict(i)
            supplies.append(result)
        
        return jsonify(supplies = supplies)
