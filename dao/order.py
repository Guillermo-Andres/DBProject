from config.dbconfig import pg_config
import psycopg2
class OrderDAO:




    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # order attributes: order_id, order_amount, order_date, order_status

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllOrders(self):
        # cursor = self.conn.cursor()
        # query = "select * from payment_method;"
        # cursor.execute(query)
        
        # for row in cursor: # find efficient way to return values from the DB
        #     result.append(row)
        cursor = self.conn.cursor()
        query = "select * from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        print(result)
        return result

    def getOrderById(self, id):
        cursor = self.conn.cursor()
        query = "select * from request where request_id = %s;"
        result = cursor.execute(query, (id,))
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