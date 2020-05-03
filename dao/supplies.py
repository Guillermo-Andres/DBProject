from config.dbconfig import pg_config
import psycopg2
class SuppliesDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    #supid , sid , rid
    def getAllSupplies(self):
        cursor = self.conn.cursor()
        query = "select * from supplies;"
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(row)
        return result

    
    

    def getSuppliesByID(self , supid):
        cursor = self.conn.cursor()
        query = "select * from supplies where supplies_id = %s;"
        cursor.execute(query , (supid))
        result = []
        result.append

    def getSuppliesBySupplierID(self , sid):
        cursor = self.conn.cursor()
        query = "select * from supplies where supplier_id = %s;"
        cursor.execute(query, (sid,))
        result = []

        for row in cursor:
            result.append(row)
        return result

    def getSuppliesByResourceID(self , rid):
        cursor = self.conn.cursor()
        query = "select * from supplies where rid = %s;"
        cursor.execute(query , (supid))
        result = []
        result.append(row)

        for row in cursor:
            result.append(row)
        return result

    def insert(self , supplies_id , supplier_id , resource_id):
        cursor = self.conn.cursor()


