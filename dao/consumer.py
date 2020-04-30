from config.dbconfig import pg_config
import psycopg2
class ConsumerDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllConsumers(self):
        # cursor = self.conn.cursor()
        # query = "select * from consumer;"
        # cursor.execute(query)
        result = [[1, "Fabiola", "Badillo", "05/14/1998", "Quebradillas, PR", "787-555-5555", "fbr@gmail.com", "high"],
                  [2, "Pablo", "Santiago", "12/12/1997", "Ponce, PR", "787-666-6666","psu@hotmail.com", "low"],
                  [3, "Guillermo", "Betancourt", "01/28/1998", "Trujillo Alto, PR", "787-111-1111", "gbs@yahoo.com", "medium"]]
        # for row in cursor:
        #     result.append(row)
        return result


    def getConsumerById(self, id):
        return self.getAllConsumers()

    def getConsumerByName(self, consumer_first_name, consumer_last_name):
        return self.getAllConsumers()

    def getConsumerByDOB(self, dob):
        return self.getAllConsumers()

    def getConsumerByAddress(self, address):
        return self.getAllConsumers()

    def getConsumerByPhoneNumber(self, phone_number):
        return self.getAllConsumers()

    def getConsumerByEmail(self, email):
        return self.getAllConsumers()

    def getConsumerBySeverity(self, severity):
        return self.getAllConsumers()

    def insert(self, item):
        return self.getAllConsumers()

    def delete(self, cid):
        return self.getAllConsumers()

    def update(self, payment_method_id):
        return self.getAllConsumers()
