from config.dbconfig import pg_config
import psycopg2

class HeavyEquipmentDAO:
#HeavyEquipment ATTTRIBUTES heavy_id, description

    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllHeavyEquipment(self):
        # cursor = self.conn.cursor()
        # query = "select * from supplier;"
        # cursor.execute(query)
        result = [[1,'15-ft Camping Tents'],[2,'20-ft Tents']]

        return result

    def getHeavyEquimentById(self, sid):
            cursor = self.conn.cursor()
            query = "select * from supplier where sid = %s;"
            cursor.execute(query, (sid,))
            result = cursor.fetchone()
            return result

    def getHeavyEquipmentByType(self, sid):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join supplier natural inner join supplies where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, sname, scity, sphone):
        cursor = self.conn.cursor()
        query = "insert into supplier(sname, scity, sphone) values (%s, %s, %s) returning sid;"
        cursor.execute(query, (sname, scity, sphone))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid
