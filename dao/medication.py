from config.dbconfig import pg_config
import psycopg2


class MedicationDAO:
    # Medication ATTTRIBUTES medication_id, name,ingredient,type,exp,price,location,quantity
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedication(self):
        cursor = self.conn.cursor()
        query = "select * from medication natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByKeyWord(self, keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from medication natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query, (keyword, keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicationById(self, id):
        cursor = self.conn.cursor()
        query = "select * from medication natural inner join resource where medication_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def insert(self, medication_ingredients, medication_type, medication_expDate, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date,supplier_id):
        cursor = self.conn.cursor()
        query = "insert into resource (resource_name,resource_price,resource_city,resource_quantity," \
                "resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id; "
        cursor.execute(query, (resource_name, resource_price, resource_city, resource_quantity, resource_description,
                               resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into medication (resource_id, medication_ingredients, medication_type, medication_expDate) values (%s, %s, %s, %s)"
        cursor.execute(query, (rid, medication_ingredients, medication_type, medication_expDate,))
        self.conn.commit()
        query = 'insert into supplies(supplier_id , resource_id) values(%s,%s);'
        cursor.execute(query, (supplier_id,rid,))
        self.conn.commit()
        cursor.close()
        return rid
