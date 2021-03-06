from flask import jsonify
from dao.contains import ContainsDAO

class ContainsHandler:

    def build_contains_dict(self , row ):
        result = {}

        result['cid']  = row[0]
        result['oid'] = row[1]
        result['rid'] = row[2]
        

        return result
    
    def getAllContains(self):
        dao = ContainsDAO()
        contains = []
        items = dao.getAllContains()

        for i in items:
            result = self.build_contains_dict(i)
            contains.append(result)
        
        return jsonify(contain = contains)
  
    def insert(self , item):
        return jsonify(Contains= item) ,200
    def delete(self , id):
        return jsonify(Contains= id) ,200
    def update(self , item):
        return jsonify(Contains= item) ,200