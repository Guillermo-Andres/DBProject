from config.dbconfig import pg_config
import psycopg2


class RequestDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequest(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural join resource natural join consumer; "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, request_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural join resource natural join consumer " \
                "where request_id = %s;"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        print(result)
        return result

    def insert(self, item):
        return self.getAllRequest()

    def delete(self, cid):
        return self.getAllRequest()

    def update(self, request_id):
        return self.getAllRequest()
