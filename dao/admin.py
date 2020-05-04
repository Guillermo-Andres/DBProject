from config.dbconfig import pg_config
import psycopg2
class AdminDAO:


    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)



    def getAllAdmins(self):
        cursor = self.conn.cursor()
        query = "select * from person natural join admin;"
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(row)
        return result

    def getAdminByID(self , person_id):
        cursor = self.conn.cursor()
        query = "select * from person natural join admin where person_id = %s;"
        cursor.execute(query , (person_id,))
        result = []
        
        for row in cursor:
            result.append(row)
        return result



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

