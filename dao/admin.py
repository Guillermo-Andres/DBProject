from config.dbconfig import pg_config
import psycopg2
class AdminDAO:

    def getAllAdmins(self):
        return [[666 , "Pablito El Admin" , "6\6\6" , "Infierno" ,  "787-666-0420" , "pablito666@hell.edu" ]]
    

    def getAdminByID(self , aid):
        for user in self.getAllAdmins():
            if(user[0] == aid):
                return user
        return None


    def getAdminByName(self  , name):
        for user in self.getAllAdmins():
            if(user[1] == name):
                return user
        
        return None

    def getAdminByDOB(self  , DOB):
        for user in self.getAllAdmins():
            if(user[2] == DOB):
                    return user
        
        return None

    
    def getAdminByLocation(self  , location):
        for user in self.getAllAdmins():
            if(user[3] == location):
                    return user
        
        return None

    def getAdminByPhone(self  , phone):
        for user in self.getAllAdmins():
            if(user[4] == phone):
                    return user
        
        return None

    def getAdminByEmail(self  , email):
        for user in self.getAllAdmins():
            if(user[4] == email):
                    return user
        
        return None


    def insert(self , item):
        return 1
    def delete(self , id):
        return 1
    def update(self , item):
        return 1

