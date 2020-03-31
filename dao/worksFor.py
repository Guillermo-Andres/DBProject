from config.dbconfig import pg_config
import psycopg2
class WorksForDAO:


    #wfid , cid , sid
    def getAllWorksFor(self):
        return [[1,1,1] , [1,2,3]]
    

    def getWorksForByID(self , pfid):
        for contains in self.getAllWorksFor():
            if(contains[0] == pfid):
                return contains
        return None

    def getWorksForByCompanyID(self , cid):
        return [[1,1,1] , [1,2,3]]
    
    def getWorksForBySupplierID(self ,sid):
        return [[1,1,1] , [1,2,3]]
