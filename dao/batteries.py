from config.dbconfig import pg_config
import psycopg2
class BatteryDAO:
    #Baterries ATTTRIBUTES battery_id, type, quantity per unit, price location quantity
    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllBatteries(self):
        result = [[1,'AA',12,3.99,'bayamon'1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def getBatteryById(self, id):
        result = [[1,'AA',12,3.99,'bayamon'1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def getBatteryByType(self, type):
        result = [[1,'AA',12,3.99,'bayamon'1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def getBatteryByPrice(self,prince):
        result = [[1,'AA',12,3.99,'bayamon'1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def getBatteryByLocaion(self,location):
        result = [[1,'AA',12,3.99,'bayamon'1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'AA',12,3.99,'bayamon'1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def delete(self, pid):
        result = [[1,'AA',12,3.99,'bayamon'1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'AA',12,3.99,'bayamon'1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result
