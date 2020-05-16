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


    def insert(self,pfname,plname,pdob,pcity,pphone, pemail,consumer_severity):
        cursor = self.conn.cursor()
        query = "insert into person (person_firstname, person_lastname, person_dob, person_city, person_phone_number, person_email) values (%s, %s, %s, %s, %s, %s) returning person_id;"
        cursor.execute(query, (pfname,plname,pdob,pcity,pphone, pemail,))
        self.conn.commit()
        pid = cursor.fetchone()[0]
        query = "insert into consumer(person_id,consumer_severety) values (%s,%s);"
        cursor.execute(query, (pid,consumer_severity))
        self.conn.commit()
