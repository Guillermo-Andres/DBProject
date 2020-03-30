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
