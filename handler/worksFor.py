from flask import jsonify
from dao.worksFor import WorksForDAO

class WorksForHandler:

    def build_WorksFor_dict(self , row ):
        result = {}

        result['wfid']  = row[0]
        result['cid'] = row[1]
        result['sid'] = row[2]
        

        return result
    
    def getAllWorksFor(self):
        dao = WorksForDAO()
        WorksFor = []
        items = dao.getAllWorksFor()

        for i in items:
            result = self.build_WorksFor_dict(i)
            WorksFor.append(result)
        
        return jsonify(WorksFor = WorksFor)

    def insert(self , item):
        return jsonify(WorksFor= item) ,200
    def delete(self , id):
        return jsonify(WorksFor= id) ,200
    def update(self , item):
        return jsonify(WorksFor= item) ,200