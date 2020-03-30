from config.dbconfig import pg_config
import psycopg2
class OrderDAO:

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
        result = [[1, 12.36, "02/05/2017", "in process"],
                  [2, 26.99, "12/16/2018", "delivered"],
                  [3, 5.00, "05/06/2020", "pending confirmation"]]
        # for row in cursor: # find efficient way to return values from the DB
        #     result.append(row)
        return result
