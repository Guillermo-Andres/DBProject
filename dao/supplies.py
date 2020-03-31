from config.dbconfig import pg_config
import psycopg2
class SuppliesDAO:


    #supid , sid , rid
    def getAllSupplies(self):
        return [[1,1,1] , [1,2,3]]
    

    def getSuppliesByID(self , supid):
        for contains in self.getAllSupplies():
            if(contains[0] == supid):
                return contains
        return None

    def getSuppliesBySupplierID(self , sid):
        return [[1,1,1] , [1,2,3]]

    def getSuppliesByResourceID(self , rid):
        return [[1,1,1] , [1,2,3]]
