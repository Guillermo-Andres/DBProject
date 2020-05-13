from config.dbconfig import pg_config
import psycopg2

class HeavyEquipmentDAO:
#HeavyEquipment ATTTRIBUTES heavy_id, description,price,location,quantity

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host = 127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHeavyEquipment(self):
        cursor = self.conn.cursor()
        query = "select * from heavyEquipment natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from heavyEquipment natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHeavyEquimentById(self, id):
        cursor = self.conn.cursor()
        query = "select * from heavyEquipment natural inner join resource where heavyEquipment_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        
    def getHeavyEquipmentByPrice(self, price):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result

    def getHeavyEquipmentByLocation(self, location):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result

    def insert(self, sname, scity, sphone):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result
    def update(self):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result

    def delete(self):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result
