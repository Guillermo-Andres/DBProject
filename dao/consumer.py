from config.dbconfig import pg_config
import psycopg2


class ConsumerDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllConsumers(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from consumer natural join person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerById(self, consumer_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from consumer natural join person " \
                "where consumer_id = %s;"
        cursor.execute(query, (consumer_id,))
        result = cursor.fetchone()
        return result

    def getConsumerByName(self, consumer_firstname, consumer_lastname):
        cursor = self.conn.cursor()
        query = "select * " \
                "from consumer inner join person " \
                "where person.person_firstname = %s " \
                "and person.person_lastname = %s;"
        cursor.execute(query, (consumer_firstname, consumer_lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

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

    def update(self, consumer_id):
        return self.getAllConsumers()
