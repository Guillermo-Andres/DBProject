from config.dbconfig import pg_config
import psycopg2
class CompanyDAO:

    def getAllCompanies(self):
        return [[2 ,  "PNP" , "corrupteo 101" ]]
    

    def getCompanyByID(self , cid):
        for Company in self.getAllCompanies():
            if(Company[0] == cid):
                return Company
        return None

    def getCompanyByDes(self , des):
        for Company in self.getAllCompanies():
            if(Company[2] == des):
                return Company
        return None

    def getCompanyByName(self , name):
        for Company in self.getAllCompanies():
            if(Company[1] == name):
                return Company
        return None