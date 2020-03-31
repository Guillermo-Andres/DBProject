from config.dbconfig import pg_config
import psycopg2

class HygieneDAO:

    # hygiene attributes: hygiene_id, hygiene_expiration_date, hygiene_price, hygiene_location, hygiene_units, hygiene_description, hygiene_quantity_per_unit, hygiene_brand

    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
    #                                                                        pg_config['user'],
    #                                                                        pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllHygiene(self):
        # cursor = self.conn.cursor()
        # query = "select * from payment_method;"
        # cursor.execute(query)
        result = [[1, "02/15/2023", 7.99, "Aguadilla", 2, "toilet paper", 12, "Charmin"],
                  [2, "08/23/2029", 5.00, "Guayanilla", 1, "paper towels", 2, "Bounty"],
                  [3, "12/15/2025", 6.00, "Hatillo", 3, "baby wipes", 50, "Huggies"]]
        # for row in cursor: # find efficient way to return values from the DB
        #     result.append(row)
        return result

    def getHygieneById(self, id):
        return self.getAllHygiene()

    def getHygieneByExpirationDate(self, expiration_date):
        return self.getAllHygiene()

    def getHygieneByPrice(self, price):
        return self.getAllHygiene()

    def getHygieneByLocation(self, location):
        return self.getAllHygiene()

    def getHygieneByUnits(self, units):
        return self.getAllHygiene()

    def getHygieneByDescription(self, description):
        return self.getAllHygiene()

    def getHygieneByQuantityPerUnit(self, quantity_per_unit):
        return self.getAllHygiene()

    def getHygieneByBrand(self, brand):
        return self.getAllHygiene()

    def insert(self):
        return self.getAllHygiene()

    def delete(self):
        return self.getAllHygiene()

    def update(self):
        return self.getAllHygiene()