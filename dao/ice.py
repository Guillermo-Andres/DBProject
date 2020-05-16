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

    def getResourceByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from ice natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword,))
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

    def insert(self, size, resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date,supplier_id):
        cursor = self.conn.cursor()
        query = "Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id;"
        cursor.execute(query, (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into ice (resource_id,ice_size) values (%s, %s);"
        cursor.execute(query, (rid,size,))
        self.conn.commit()
        query = 'insert into supplies(supplier_id , resource_id) values(%s,%s);'
        cursor.execute(query, (supplier_id,rid,))
        self.conn.commit()
        cursor.close()
        return rid
