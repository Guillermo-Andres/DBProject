from config.dbconfig import pg_config
import psycopg2
class AdminDAO:

    def getAllAdmins(self):
        return [[2 , "Pablito El Admin" , "6\6\6" , "Infierno" ,  "787-666-0420" , "pablito666@hell.edu" ]]
    

    def getAdminByID(self , aid):
        for user in self.getAllAdmins():
            if(user[0] == aid):
                return user
        return None
