from config.dbconfig import pg_config
import psycopg2
class ContainsDAO:

    def getAllContains(self):
        return [[1,1,1] , [1,2,3]]
    

    def getContainsByID(self , cid):
        for contains in self.getAllContains():
            if(contains[0] == cid):
                return contains
        return None
