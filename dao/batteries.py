from config.dbconfig import pg_config
import psycopg2
class BatteryDAO:
    # Baterries ATTTRIBUTES battery_id, type, quantity per unit, price location quantity
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "select * from batteries natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryById(self, id):
        cursor = self.conn.cursor()
        query = "select * from batteries natural inner join resource where batteries_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getBatteryByType(self, type):
    #     result = [[1,'AA',12,3.99,'bayamon',1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
    #     return result
    #
    # def getBatteryByPrice(self,prince):
    #     result = [[1,'AA',12,3.99,'bayamon',1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
    #     return result

    def getBatteryByLocaion(self,location):
        cursor = self.conn.cursor()
        query = "select * from batteries natural inner join resource where rlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'AA',12,3.99,'bayamon',1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def delete(self, pid):
        result = [[1,'AA',12,3.99,'bayamon',1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'AA',12,3.99,'bayamon',1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result
