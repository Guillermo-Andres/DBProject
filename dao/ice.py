from config.dbconfig import pg_config
import psycopg2
class IceDAO:
    # ICE ATTTRIBUTES iid, size,quantity,description,price,location,

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host = 127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllIce(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from ice natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getIceById(self, id):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join resource where ice_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getIceByLocation(self,location):
        cursor = self.conn.cursor()
        query = "select * from fuel natural inner join resource where rlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getIceBySize(self, size):
    #     result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
    #     return result
    #
    # def getIceByPrice(self,price):
    #     result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
    #     return result
    #

    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result

    def delete(self, pid):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result
