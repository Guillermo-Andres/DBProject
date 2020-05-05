from config.dbconfig import pg_config
import psycopg2
class ToolsDAO:
    #powertools ATTTRIBUTES tool id, type, description,price,location,quantity

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host = 127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllTools(self):
        cursor = self.conn.cursor()
        query = "select * from tools natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result




    def getToolById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from tools natural inner join resource where fuel_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getToolByType(self, color):
        result = [[1,'Power Tool','Electric Drill',49.99,'Caguas',1],[2,'Hand Tool','Hammer',49.99,'Caguas',1],[3,'Power Tool','Electric Blower',49.99,'Caguas',1]]
        return result

    def getToolByPrice(self, color):
        result = [[1,'Power Tool','Electric Drill',49.99,'Caguas',1],[2,'Hand Tool','Hammer',49.99,'Caguas',1],[3,'Power Tool','Electric Blower',49.99,'Caguas',1]]
        return result
    def getToolByLocation(self, color):
        result = [[1,'Power Tool','Electric Drill',49.99,'Caguas',1],[2,'Hand Tool','Hammer',49.99,'Caguas',1],[3,'Power Tool','Electric Blower',49.99,'Caguas',1]]
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'Power Tool','Electric Drill',49.99,'Caguas',1],[2,'Hand Tool','Hammer',49.99,'Caguas',1],[3,'Power Tool','Electric Blower',49.99,'Caguas',1]]
        return result
    def delete(self, pid):
        result = [[1,'Power Tool','Electric Drill',49.99,'Caguas',1],[2,'Hand Tool','Hammer',49.99,'Caguas',1],[3,'Power Tool','Electric Blower',49.99,'Caguas',1]]
        return result
    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'Power Tool','Electric Drill',49.99,'Caguas',1],[2,'Hand Tool','Hammer',49.99,'Caguas',1],[3,'Power Tool','Electric Blower',49.99,'Caguas',1]]
        return result
