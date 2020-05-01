from config.dbconfig import pg_config
import psycopg2

class PowerGeneratorsDAO:

    # femenine hygiene attributes: fh_id, fh_price, rh_location, rh_quantity, fh_type (pads, liners, tampons, cup), fh_flow (light, medium, heavy), fh_brand, fh_quantity_per_unit

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPowerGenerators(self):
        # cursor = self.conn.cursor()
        # query = "select * from payment_method;"
        # cursor.execute(query)
        result = [[1, 6.36, "Ponce", 1, "pad", "heavy", "Kotex", 40],
                  [2, 4.00, "Barranquitas", 2, "tampon", "light", "Tampax", 25],
                  [3, 7.65, "Mayaguez", 1, "cup", "medium", "Always", 30]]
        # for row in cursor: # find efficient way to return values from the DB
        #     result.append(row)
        return result

    def getPowerGeneratorsById(self, id):
        return self.getAllFemenineHygiene()

    def getPowerGeneratorsByPrice(self, price):
        return self.getAllFemenineHygiene()

    def getPowerGeneratorsByLocation(self, location):
        return self.getAllFemenineHygiene()

    def getPowerGeneratorsByQuantity(self, quantity):
        return self.getAllFemenineHygiene()

    def getPowerGeneratorsByType(self, type):
        return self.getAllFemenineHygiene()

    def getPowerGeneratorsByFlow(self, flow):
        return self.getAllFemenineHygiene()

    def getPowerGeneratorsByBrand(self, brand):
        return self.getAllFemenineHygiene()

    def getPowerGeneratorsByQuantityPerUnit(self, quantity_per_unit):
        return self.getAllFemenineHygiene()

    def insert(self):
        return self.getAllFemenineHygiene()

    def delete(self):
        return self.getAllFemenineHygiene()

    def update(self):
        return self.getAllFemenineHygiene()