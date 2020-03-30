from config.dbconfig import pg_config
import psycopg2
class PaysForDAO:


    #pfid , pid , oid
    def getAllPaysFor(self):
        return [[1,1,1] , [1,2,3]]
    

    def getPaysForByID(self , pfid):
        for contains in self.getAllPaysFor():
            if(contains[0] == pfid):
                return contains
        return None
