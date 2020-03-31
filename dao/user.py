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


    def getUserByName(self  , name):
        for user in self.getAllUsers():
            if(user[1] == name):
                return user
        
        return None

    def getUserByDOB(self  , DOB):
        for user in self.getAllUsers():
            if(user[2] == DOB):
                    return user
        
        return None

    
    def getUserByLocation(self  , location):
        for user in self.getAllUsers():
            if(user[3] == location):
                    return user
        
        return None

    def getUserByPhone(self  , phone):
        for user in self.getAllUsers():
            if(user[4] == phone):
                    return user
        
        return None

    def getUserByEmail(self  , email):
        for user in self.getAllUsers():
            if(user[4] == email):
                    return user
        
        return None

    def insert(self , item):
        return 1
    def delete(self , id):
        return 1
    def update(self , item):
        return 1