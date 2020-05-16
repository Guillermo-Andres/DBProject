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

    def getResourceByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from batteries natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getBatteryByLocaion(self,location):
        cursor = self.conn.cursor()
        query = "select * from batteries natural inner join resource where rlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, batteries_type, batteries_quantityPerUnit, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date,supplier_id):
        cursor = self.conn.cursor()
        query = "insert into resource (resource_name,resource_price,resource_city,resource_quantity," \
                "resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id; "
        cursor.execute(query, (resource_name, resource_price, resource_city, resource_quantity, resource_description,
                               resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into batteries (resource_id, batteries_type, batteries_quantityPerUnit) values (%s, %s, %s)"
        cursor.execute(query, (rid, batteries_type, batteries_quantityPerUnit,))
        self.conn.commit()
        query = 'insert into supplies(supplier_id , resource_id) values(%s,%s);'
        cursor.execute(query, (supplier_id,rid,))

        cursor.close()
        return rid

    def delete(self, pid):
        result = [[1,'AA',12,3.99,'bayamon',1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'AA',12,3.99,'bayamon',1],[2,'DD',4,5.99,'carolina', 5],[3,'AAA',12,6.99,'ponce',24]]
        return result
