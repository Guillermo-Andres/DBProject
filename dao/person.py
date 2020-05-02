from config.dbconfig import pg_config
import psycopg2


class PersonDAO:

    def __init__(self):
        connection_url = "dbname=%s person=%s password=%s" % (pg_config['dbname'],
                                                              pg_config['person'],
                                                              pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPersons(self):
        cursor = self.conn.cursor()
        query = "select *" \
                "from person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPersonByID(self, person_id):
        cursor = self.conn.cursor()
        query = "select *" \
                "from person" \
                "where person_id = %s;"
        result = cursor.execute(query, (person_id,))
        return result

    def getPersonByName(self, name):
        return self.getAllPersons()

    def getPersonByDOB(self, DOB):
        return self.getAllPersons()

    def getPersonByLocation(self, location):
        return self.getAllPersons()

    def getPersonByPhone(self, phone):
        return self.getAllPersons()

    def getPersonByEmail(self, email):
        return self.getAllPersons()

    def insert(self, item):
        return self.getAllPersons()

    def delete(self, id):
        return self.getAllPersons()

    def update(self, item):
        return self.getAllPersons()
