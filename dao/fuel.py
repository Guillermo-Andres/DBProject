from config.dbconfig import pg_config
import psycopg2
class FuelDAO:
    #Fuel ATTTRIBUTES fid, type,unit_size,description
    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        #cursor = self.conn.cursor()
        #query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        #cursor.execute(query)
        result = [[1,'Propane','12 Oz' , '1 Propane gas Tank'],[2,'Gas','24 Galons', '24 Gallons of liquid fuel'],[3,'Disel','5 Galons','5 Galons of Disel']]
    #    for row in cursor:
    #        result.append(row)
        return result

    # def getFuelById(self, pid):
    #     cursor = self.conn.cursor()
    #     query = "select pid, pname, pmaterial, pcolor, pprice from parts where pid = %s;"
    #     cursor.execute(query, (pid,))
    #     result = cursor.fetchone()
    #     return result
    #
    # def getFuelByType(self, color):
    #     cursor = self.conn.cursor()
    #     query = "select * from parts where pcolor = %s;"
    #     cursor.execute(query, (color,))
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result
    #
    # def getFuelBySize(self, color):
    #     cursor = self.conn.cursor()
    #     query = "select * from parts where pcolor = %s;"
    #     cursor.execute(query, (color,))
    #     result = []
    #     for row in cursor:
    #     result.append(row)
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
