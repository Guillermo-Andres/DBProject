from config.dbconfig import pg_config
import psycopg2


class MedicalDevicesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from medicalDevices natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourceByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from medicalDevices natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicalDevicesById(self, medicalDevices_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from medicalDevices natural inner join resource" \
                " where medicalDevices_id = %s;"
        # TODO - check joins
        cursor.execute(query, (medicalDevices_id,))
        result = cursor.fetchone()
        return result



    def insert(self, medicalDevices_type, resource_name, resource_price, resource_city, resource_quantity, resource_description,
               resource_date,supplier_id):
        cursor = self.conn.cursor()
        query = "insert into resource (resource_name,resource_price,resource_city,resource_quantity," \
                "resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id; "
        cursor.execute(query, (resource_name, resource_price, resource_city, resource_quantity, resource_description,
                               resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into medicalDevices (resource_id, medicalDevices_type) values (%s, %s);"
        cursor.execute(query, (rid, medicalDevices_type,))
        self.conn.commit()
        query = 'insert into supplies(supplier_id , resource_id) values(%s,%s);'
        cursor.execute(query, (supplier_id,rid,))
        self.conn.commit()
        cursor.close()
        return rid
