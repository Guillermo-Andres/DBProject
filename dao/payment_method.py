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
        cursor = self.conn.cursor()
        query = "select * from paymentMethod;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPaymentMethodById(self, paymentMethod_id):
        cursor = self.conn.cursor()
        query = "select *" \
                "from paymentMethod" \
                "where paymentMethod_id = %s;"
        result = cursor.execute(query, (paymentMethod_id,))

    def getPaymentMethodByType(self, type):
        return self.getAllPaymentMethods()

    def insert(self):
        return self.getAllPaymentMethods()

    def delete(self):
        return self.getAllPaymentMethods()

    def update(self):
        return self.getAllPaymentMethods()
