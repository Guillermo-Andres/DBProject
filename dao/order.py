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
        query = "select * from order;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderById(self, order_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request " \
                "where order_id = %s;"
        result = cursor.execute(query, (order_id,))
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
