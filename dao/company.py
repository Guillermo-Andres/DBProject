from config.dbconfig import pg_config
import psycopg2
class CompanyDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllCompanies(self):
        cursor = self.conn.cursor()
        query = "select * from company;"
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    

    def getCompanyByID(self , cid):
        cursor = self.conn.cursor()
        query = "select * " \
                "from company " \
                "where company_id = %s;"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        return result

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

    def insert(self , item):
        return 1
    def delete(self , id):
        return 1
    def update(self , item):
        return 1