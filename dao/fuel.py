from config.dbconfig import pg_config
import psycopg2
class FuelDAO:
    #Fuel ATTTRIBUTES fid, type,unit_size,description,price,location,quantity
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host = 127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelById(self, id):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join resource where fuel_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelByType(self, type):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join resource where fuel_type = %s;"
        cursor.execute(query, (type,))
        result = cursor.fetchone()
        return result

    def getFuelBySize(self, size):
        cursor = self.conn.cursor()
        query = "select * from fuel where size = %s;"
        cursor.execute(query, (size,))
        result = cursor.fetchone()
        return result

    def getFuelByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join resource where rprice = %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join resource where rprice = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def delete(self, pid):
         cursor = self.conn.cursor()
         query = "select * from fuel natural inner join resource;"
         cursor.execute(query)
         result = []
         for row in cursor:
             result.append(row)
         return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
