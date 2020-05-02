from config.dbconfig import pg_config
import psycopg2
class FuelDAO:
    #Fuel ATTTRIBUTES fid, type,unit_size,description,price,location,quantity
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select * from fuel;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelById(self, id):
        cursor = self.conn.cursor()
        query = "select * from fuel where fuel_id = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result

    def getFuelByType(self, type):
        cursor = self.conn.cursor()
        query = "select * from fuel where fuel_type = %s;"
        cursor.execute(query, (type,))
        result = cursor.fetchone()
        return result

    def getFuelBySize(self, size):
        cursor = self.conn.cursor()
        query = "select * from fuel where size = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getFuelByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from fuel where price = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result
    def getFuelByLocation(self, location):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def delete(self, pid):
         result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
         return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result
