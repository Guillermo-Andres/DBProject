from config.dbconfig import pg_config
import psycopg2
class IceDAO:
    #ICE ATTTRIBUTES iid, size,unit_size,description
    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)


    def build_ice_dict(self , row):
        iceDict = {}

        iceDict['iid'] = row[0]
        iceDict['size'] = row[1]
        iceDict['unit_size'] = row[2]
        iceDict['description'] = row[3]

        return iceDict






    def getAllIce(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)
        result = [[1,'8 Oz',1, '8 Oz bag of ice'],[2,'6 Oz',1, '6 Oz bag of ice'],[3,'12 Oz',6, '12 Oz bag of ice']]
    #    for row in cursor:
    #        result.append(row)
        return result


    def getIceByID(self , id):
        return self.getAllIce()
    
    def getIceBySize(self , size):
        return self.getAllIce()
    
    def getIceByUnitSize(self , unit_size):
        return self.getAllIce()

    def getIceByDescription(self , description):
        return self.getAllIce()

    def insert(self , item):
        return 1
    def delete(self , id):
        return 1
    def update(self , item):
        return 1

    
    # def getIceById(self, pid):
    #     cursor = self.conn.cursor()
    #     query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
    #     cursor.execute(query, (pid,))def getSuppliersByCity(self, city):
    #     cursor = self.conn.cursor()
    #     query = "select * from supplier where scity = %s;"
    #     cursor.execute(query, (city,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    #     result = cursor.fetchone()
    #     return result
    #
    #
    # def getIceBySize(self, color):
    #     cursor = self.conn.cursor()
    #     query = "select * from parts where pcolor = %s;"
    #     cursor.execute(query, (color,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    #
    #
    # def insert(self, pname, pcolor, pmaterial, pprice):
    #     cursor = self.conn.cursor()
    #     query = "insert into parts(pname, pcolor, pmaterial, pprice) values (%s, %s, %s, %s) returning pid;"
    #     cursor.execute(query, (pname, pcolor, pmaterial, pprice,))
    #     pid = cursor.fetchone()[0]
    #     self.conn.commit()
    #     return pid
    #
    # def delete(self, pid):
    #     cursor = self.conn.cursor()
    #     query = "delete from parts where pid = %s;"
    #     cursor.execute(query, (pid,))
    #     self.conn.commit()
    #     return pid
    #
    # def update(self, pid, pname, pcolor, pmaterial, pprice):
    #     cursor = self.conn.cursor()
    #     query = "update parts set pname = %s, pcolor = %s, pmaterial = %s, pprice = %s where pid = %s;"
    #     cursor.execute(query, (pname, pcolor, pmaterial, pprice, pid,))
    #     self.conn.commit()
    #     return pid
    #
    # def getCountByFoodId(self):
    #     cursor = self.conn.cursor()
    #     query = "select pid, pname, sum(stock) from parts natural inner join supplies group by pid, pname order by pname;"
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
