from flask import jsonify
from dao.user import UserDAO

class UserHandler:

    def build_user_dict(self , row ):
        result = {}

        result['uid']  = row[0]
        result['uname'] = row[1]
        result['uAddress'] = row[2]
        result['uPhone'] = row[3]
        result['uEmail'] = row[4]

        return result

    def getAllUsers(self):
        dao = UserDAO()
        users = []
        items = dao.getAllUsers()

        for i in items:
            result = self.build_user_dict(i)
            users.append(result)

        return jsonify(User = users)

    def getUserByID(self , aid ):
        dao = UserDAO()
        users = []
        items = dao.getUserByID(aid)

        for i in items:
            result = self.build_user_dict(i)
            users.append(result)

        return jsonify(User = users)


    def getUserByName(self , name ):
        dao = UserDAO()
        users = []
        items = dao.getUserByName(name)

        for i in items:
            result = self.build_user_dict(i)
            users.append(result)

        return jsonify(User = users)

    def getUserByAddress(self ,  location):
        dao = UserDAO()
        users = []
        items = dao.getUserByLocation(location)

        for i in items:
            result = self.build_user_dict(i)
            users.append(result)

        return jsonify(User = users)

    def getUserByPhone(self , phone ):
        dao = UserDAO()
        users = []
        items = dao.getUserByPhone(phone)

        for i in items:
            result = self.build_user_dict(i)
            users.append(result)

        return jsonify(User = users)

    def getUserByEmail(self , email):
        dao = UserDAO()
        users = []
        items = dao.getUserByEmail(email)

        for i in items:
            result = self.build_user_dict(i)
            users.append(result)

        return jsonify(User = users)


    def insert(self , item):
        return 1
    def delete(self , id):
        return 1
    def update(self , item):
        return 1
