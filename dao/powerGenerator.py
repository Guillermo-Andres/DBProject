from config.dbconfig import pg_config
import psycopg2


class PowerGeneratorDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPowerGenerators(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from powerGenerator natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourceByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from powerGenerator natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerGeneratorsById(self, powerGenerator_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from powerGenerator natural inner join resource" \
                " where powerGenerator_id = %s;"
        cursor.execute(query, (powerGenerator_id,))
        result = cursor.fetchone()
        return result

    def insert(self, resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date,ptype):
        cursor = self.conn.cursor()
        query = "Insert into resource (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id;"
        cursor.execute(query, (resource_name,resource_price,resource_city,resource_quantity,resource_description, resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into powerGenerator (resource_id,powerGenerator_type) values (%s, %s);"
        cursor.execute(query, (rid,ptype,))
        self.conn.commit()
        cursor.close()
        return rid
