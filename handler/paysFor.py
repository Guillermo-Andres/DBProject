from flask import jsonify
from dao.paysFor import PaysForDAO

class PaysForHandler:

    def build_PaysFor_dict(self , row ):
        result = {}

        result['pfid']  = row[0]
        result['pid'] = row[1]
        result['oid'] = row[2]
        

        return result
    
    def getAllPaysFor(self):
        dao = PaysForDAO()
        PaysFor = []
        items = dao.getAllPaysFor()

        for i in items:
            result = self.build_PaysFor_dict(i)
            PaysFor.append(result)
        
        return jsonify(PaysFor = PaysFor)


    def getPaysForByID(self , id):
        dao = PaysForDAO()
        PaysFor = []
        items = dao.getPaysForByID(id)

        for i in items:
            result = self.build_PaysFor_dict(i)
            PaysFor.append(result)
        
        return jsonify(PaysFor = PaysFor)

    def getPaysForByPaymentMethod(self , id):
        dao = PaysForDAO()
        PaysFor = []
        items = dao.getPaysForByPaymentID(id)

        for i in items:
            result = self.build_PaysFor_dict(i)
            PaysFor.append(result)
        
        return jsonify(PaysFor = PaysFor)

    def getPaysForByOrder(self , id):
        dao = PaysForDAO()
        PaysFor = []
        items = dao.getPaysForByOrderID(id)

        for i in items:
            result = self.build_PaysFor_dict(i)
            PaysFor.append(result)
        
        return jsonify(PaysFor = PaysFor)

    def insert(self , item):
        return jsonify(PaysFor= item) ,200
    def delete(self , id):
        return jsonify(PaysFor= id) ,200
    def update(self , item):
        return jsonify(PaysFor= item) ,200