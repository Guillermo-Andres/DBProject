from config.dbconfig import pg_config
import psycopg2


class OrderDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllOrders(self):
        cursor = self.conn.cursor()
        query = "select * from orders natural join request natural join supplier natural join paysFor;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderById(self, order_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from orders natural join request natural join supplier " \
                "where order_id = %s;"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        return result

    def getOrderByConsumerId(self , consumer_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from orders natural join request natural join supplier natural join consumer " \
                "where consumer_id = %s;"
        cursor.execute(query,(consumer_id ,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByAmount(self, amount):
        return self.getAllOrders()

    def getOrderByDate(self, date):
        return self.getAllOrders()

    def getOrderByStatus(self, status):
        return self.getAllOrders()

    def insert(self):
        return self.getAllOrders()

    def delete(self):
        return self.getAllOrders()

    def update(self):
        return self.getAllOrders()
