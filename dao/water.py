from config.dbconfig import pg_config
import psycopg2
class WaterDAO:
    #ICE ATTTRIBUTES wiid, size,brand,type,unit_size, price,location,quantity

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host= 127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)





    def getAllWater(self):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getWaterById(self, id):
        cursor = self.conn.cursor()
        query = "select * from water natural inner join resource where water_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getWaterBySize(self, size):
    #     result = [[1,'8 Oz','Dasani', 'Bottled',12,6.99,'Guayanilla',1],[2,'16 Oz','Evian', 'Bottled',24,90.95,'Guaynabo',48]]
    #     return result

    # def getWaterByPrice(self,price):
    #     result = [[1,'8 Oz','Dasani', 'Bottled',12,6.99,'Guayanilla',1],[2,'16 Oz','Evian', 'Bottled',24,90.95,'Guaynabo',48]]
    #     return result
    #
    # def getWaterByLocation(self,location):
    #     result = [[1,'8 Oz','Dasani', 'Bottled',12,6.99,'Guayanilla',1],[2,'16 Oz','Evian', 'Bottled',24,90.95,'Guaynabo',48]]
    #     return result
    #
    # def getWaterByType(self,location):
    #     result = [[1,'8 Oz','Dasani', 'Bottled',12,6.99,'Guayanilla',1],[2,'16 Oz','Evian', 'Bottled',24,90.95,'Guaynabo',48]]
    #     return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'8 Oz','Dasani', 'Bottled',12,6.99,'Guayanilla',1],[2,'16 Oz','Evian', 'Bottled',24,90.95,'Guaynabo',48]]
        return result

    def delete(self, pid):
        result = [[1,'8 Oz','Dasani', 'Bottled',12,6.99,'Guayanilla',1],[2,'16 Oz','Evian', 'Bottled',24,90.95,'Guaynabo',48]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'8 Oz','Dasani', 'Bottled',12,6.99,'Guayanilla',1],[2,'16 Oz','Evian', 'Bottled',24,90.95,'Guaynabo',48]]
        return result
