from config.dbconfig import pg_config
import psycopg2
class cannedFoodDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllcannedFood(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from cannedFood natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getcannedFoodById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from cannedFood natural inner join resource where ice_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from cannedFood natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # 'yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]] return result

    def getcannedFoodByLocation(self,location):
        cursor = self.conn.cursor()
        query = "select * from cannedFood natural inner join resource where rlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, cannedFood_type, cannedFood_is_perishable, cannedFood_ingredients, cannedFood_unitSize,
               cannedFood_expDate, resource_name, resource_price, resource_city, resource_quantity,
               resource_description, resource_date,supplier_id):
        cursor = self.conn.cursor()
        query = "insert into resource (resource_name,resource_price,resource_city,resource_quantity," \
                "resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id; "
        cursor.execute(query, (resource_name, resource_price, resource_city, resource_quantity, resource_description,
                               resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into cannedFood (resource_id, cannedFood_type, cannedFood_is_perishable, " \
                "cannedFood_ingredients, cannedFood_unitSize, cannedFood_expDate) values (%s, %s, %s, %s, %s, %s); "
        cursor.execute(query, (rid, cannedFood_type, cannedFood_is_perishable, cannedFood_ingredients,
                               cannedFood_unitSize, cannedFood_expDate,))
        self.conn.commit()
        query = 'insert into supplies(supplier_id , resource_id) values(%s,%s);'
        cursor.execute(query, (supplier_id,rid,))
        self.conn.commit()
        cursor.close()
        return rid
