from flask import jsonify
from dao.admin import AdminDAO

class AdminHandler:

    def build_admin_dict(self , row ):
        result = {}

        result['person_id']  = row[0]
        result['person_firstname'] = row[1]
        result['person_lastname'] = row[2]
        result['person_dob'] = row[3]
        result['person_address'] = row[4]
        result['person_phone'] = row[5]
        result['person_email'] = row[6]
        result['admin_id'] = row[7]

        return result

    def getAllAdmins(self):
        dao = AdminDAO()
        users = []
        items = dao.getAllAdmins()

        for i in items:
            result = self.build_admin_dict(i)
            users.append(result)

        return jsonify(User = users)


    def getAdminByID(self , person_id ):
        dao = AdminDAO()
        users = []
        items = dao.getAdminByID(person_id)

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
        return jsonify(Admin= item) ,200
