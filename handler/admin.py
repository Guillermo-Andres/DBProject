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


    def getAdminByID(self , aid ):
        dao = AdminDAO()
        users = []
        items = dao.getAdminByID(aid)

        for i in items:
            result = self.build_admin_dict(i)
            users.append(result)
        
        return jsonify(User = users)

    
    def getAdminByName(self , name ):
        dao = AdminDAO()
        users = []
        items = dao.getAdminByName(name)

        for i in items:
            result = self.build_admin_dict(i)
            users.append(result)
        
        return jsonify(User = users)

    def getAdminByAddress(self ,  location):
        dao = AdminDAO()
        users = []
        items = dao.getAdminByLocation(location)

        for i in items:
            result = self.build_admin_dict(i)
            users.append(result)
        
        return jsonify(User = users)

    def getAdminByPhone(self , phone ):
        dao = AdminDAO()
        users = []
        items = dao.getAdminByPhone(phone)

        for i in items:
            result = self.build_admin_dict(i)
            users.append(result)
        
        return jsonify(User = users)

    def getAdminByEmail(self , email):
        dao = AdminDAO()
        users = []
        items = dao.getAdminByEmail(email)

        for i in items:
            result = self.build_admin_dict(i)
            users.append(result)
        
        return jsonify(User = users)

    def insert(self , item):
        return 1
    def delete(self , id):
        return 1
    def update(self , item):
        return 1