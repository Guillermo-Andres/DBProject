from config.dbconfig import pg_config
import psycopg2


class ResourceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResource(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = "select *" \
                "from resource" \
                "where resource_id = %s;"
        result = cursor.execute(query, (resource_id,))
        return result

    def getResourceByName(self, resource_first_name, resource_last_name):
        return self.getAllResource()

    def getResourceByDOB(self, dob):
        return self.getAllResource()

    def getResourceByAddress(self, address):
        return self.getAllResource()

    def getResourceByPhoneNumber(self, phone_number):
        return self.getAllResource()

    def getResourceByEmail(self, email):
        return self.getAllResource()

    def getResourceBySeverity(self, severity):
        return self.getAllResource()

    def insert(self, item):
        return self.getAllResource()

    def delete(self, cid):
        return self.getAllResource()

    def update(self, payment_method_id):
        return self.getAllResource()
