from config.dbconfig import pg_config
import psycopg2
class PaymentMethodDAO:

    # payment_method_attributes: payment_method_id, type

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPaymentMethods(self):
        # cursor = self.conn.cursor()
        # query = "select * from payment_method;"
        # cursor.execute(query)
        result = [[1, "credit"], [2, "debit"], [3, "cash"]]
        # for row in cursor: # find efficient way to return values from the DB
        #     result.append(row)
        return result

    def getPaymentMethodById(self, payment_method_id):
        cursor = self.conn.cursor()
        query = "select * from payment_method where payment_method_id = %s;"
        cursor.execute(query, (payment_method_id,))
        result = cursor.fetchone()
        return "This will return payment methods by id"

    def getPaymentMethodByType(self, type):
        cursor = self.conn.cursor()
        query = "select * from payment_method;"
        cursor.execute(query)
        result = []
        for row in cursor:  # find efficient way to return values from the DB
            result.append(row)
        return "This will return payment methods by type"

    def insert(self):
        return "This inserts a new record to the PaymentMethod table"

    def delete(self, payment_method_id):
        return "This deletes a record from the PaymentMethod table"

    def update(self, payment_method_id):
        return "This updates an existing record from the PaymentMethod table"