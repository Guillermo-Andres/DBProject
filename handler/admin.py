from flask import jsonify
from dao.admin import AdminDAO

class AdminHandler:

    def build_admin_dict(self , row ):
        result = {}

        result['aid']  = row[0]
        result['aname'] = row[1]
        result['aAddress'] = row[2]
        result['aPhone'] = row[3]
        result['aEmail'] = row[4]

        return result
    
    def getAllAdmins(self):
        dao = AdminDAO()
        users = []
        items = dao.getAllAdmins()

        for i in items:
            result = self.build_admin_dict(i)
            users.append(result)
        
        return jsonify(User = users)
