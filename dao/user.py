from config.dbconfig import pg_config
import psycopg2
class UserDAO:

    def getAllUsers(self):
        return [[2 , "Pablito El Dios" , "6\6\6" , "Infierno" ,  "787-666-0420" , "pablito666@hell.edu" ]]
    

    def getUserByID(self , uid):
        for user in self.getAllUsers():
            if(user[0] == uid):
                return user
        return None
