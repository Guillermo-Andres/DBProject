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

    
    def getSuppliesByID(self , id):
        dao = SuppliesDAO()
        supplies = []
        items = dao.getSuppliesByID(id)

        for i in items:
            result = self.build_supplies_dict(i)
            supplies.append(result)
        
        return jsonify(supplies = supplies)

    def getSuppliesBySupplierID(self , sid):
        dao = SuppliesDAO()
        supplies = []
        items = dao.getSuppliesBySupplierID(sid)

        for i in items:
            result = self.build_supplies_dict(i)
            supplies.append(result)
        
        return jsonify(supplies = supplies)

    def getSuppliesByResourceID(self , rid):
        dao = SuppliesDAO()
        supplies = []
        items = dao.getSuppliesByResourceID(rid)

        for i in items:
            result = self.build_supplies_dict(i)
            supplies.append(result)
        
        return jsonify(supplies = supplies)


    def insert(self , item):
        return jsonify(Supplies= item) ,200
    def delete(self , id):
        return jsonify(Supplies= id) ,200
    def update(self , item):
        return jsonify(Supplies= item) ,200