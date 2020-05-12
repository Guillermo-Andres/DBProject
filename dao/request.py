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
                "from request natural join resource natural join consumer natural join makesRequest; "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, request_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural join resource natural join consumer natural join makesRequest " \
                "where request_id = %s;"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def getResourceInRequest(self, request_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural join resource " \
                "where request_id = %s"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def getRequestByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural join resource natural join consumer natural join makesRequest where resource_name  ~*  %s OR resource_description ~* %s; "
        
        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, type , consumer_id , date ):
        cursor = self.conn.cursor()
        query ="insert into request(resource_id , request_date) values (%s , %s) " \
               "insert into makesRequest(consumer_id , request_id) values (%s , %s); " 
        
        cursor.execute(query , (type , date , consumer_id , type))

    def delete(self, cid):
        return self.getAllRequest()

    def update(self, request_id):
        return self.getAllRequest()
