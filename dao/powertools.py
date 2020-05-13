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

    def insert(self, resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date,ttype):
        cursor = self.conn.cursor()
        query = "Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id;"
        cursor.execute(query, (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into tools (resource_id,tools_type) values (%s, %s);"
        cursor.execute(query, (rid,ttype,))
        self.conn.commit()
        cursor.close()
        return rid
