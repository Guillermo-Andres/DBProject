from config.dbconfig import pg_config
import psycopg2
class ConsumerDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # consumer attributes: consumer_id, consumer_first_name, consumer_last_name, consumer_dob, consumer_address, consumer_phone_number, consumer_email_address, consumer_severity

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


    def getConsumerById(self, cid):
        cursor = self.conn.cursor()
        query = "select cid, cseverity from consumer where cid = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def getConsumerBySeverity(self, cseverity):
        cursor = self.conn.cursor()
        query = "selects * from consumer where cseverity = %s;"
        cursor.execute(query, (cseverity,))
        result = []
        for row in cursor:
            result.append(row)
        # return result
        return "This will return all consumers by cseverity"

    def insert(self):
        return "This inserts a new record to the Consumer table"

    def delete(self, cid):
        return "This will delete the record with the specified cid"

    def update(self, payment_method_id):
        return "This updates an existing record from the PaymentMethod table"
