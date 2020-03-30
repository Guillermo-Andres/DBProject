from config.dbconfig import pg_config
import psycopg2
class SuppliesDAO:


    #supid , sid , id
    def getAllSupplies(self):
        return [[1,1,1] , [1,2,3]]
    

    def getSuppliesByID(self , supid):
        for contains in self.getAllSupplies():
            if(contains[0] == supid):
                return contains
        return None
