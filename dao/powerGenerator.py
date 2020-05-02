from config.dbconfig import pg_config
import psycopg2


class PowerGeneratorDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPowerGenerators(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from powerGenerator natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerGeneratorsById(self, powerGenerator_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from powerGenerator natural inner join resource" \
                "where powerGenerator_id = %s;"
        cursor.execute(query, (powerGenerator_id,))
        result = cursor.fetchone()
        return result

    def getPowerGeneratorsByPrice(self, price):
        return self.getAllPowerGenerators()

    def getPowerGeneratorsByLocation(self, location):
        return self.getAllPowerGenerators()

    def getPowerGeneratorsByQuantity(self, quantity):
        return self.getAllPowerGenerators()

    def getPowerGeneratorsByType(self, type):
        return self.getAllPowerGenerators()

    def getPowerGeneratorsByFlow(self, flow):
        return self.getAllPowerGenerators()

    def getPowerGeneratorsByBrand(self, brand):
        return self.getAllPowerGenerators()

    def getPowerGeneratorsByQuantityPerUnit(self, quantity_per_unit):
        return self.getAllPowerGenerators()

    def insert(self):
        return self.getAllPowerGenerators()

    def delete(self):
        return self.getAllPowerGenerators()

    def update(self):
        return self.getAllPowerGenerators()
