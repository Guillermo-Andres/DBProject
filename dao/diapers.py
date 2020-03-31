from config.dbconfig import pg_config
import psycopg2

class DiapersDAO:

    # diapers attributes: diaper_id, diaper_price, diaper_location, diaper_quantity, diaper_size, diaper_material, diaper_brand

    # def __init__(self):
    #     connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
    #                                                                        pg_config['user'],
    #                                                                        pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllDiapers(self):
        # cursor = self.conn.cursor()
        # query = "select * from payment_method;"
        # cursor.execute(query)
        result = [[1, 12.99, "Isabela", 1, "newborn", "cotton", "Pampers"],
                  [2, 10.99, "Camuy", 1, "2", "hemp", "Huggies"],
                  [3, 15.99, "Arecibo", 1, "5", "microfiber", "Luv"]]
        # for row in cursor: # find efficient way to return values from the DB
        #     result.append(row)
        return result

    def getDiapersById(self, id):
        return self.getAllDiapers()

    def getDiapersByPrice(self, price):
        return self.getAllDiapers()

    def getDiapersByLocation(self, location):
        return self.getAllDiapers()

    def getDiapersByQuantity(self, quantity):
        return self.getAllDiapers()

    def getDiapersBySize(self, size):
        return self.getAllDiapers()

    def getDiapersByMaterial(self, material):
        return self.getAllDiapers()

    def getDiapersByBrand(self, brand):
        return self.getAllDiapers()

    def insert(self):
        return self.getAllDiapers()

    def delete(self):
        return self.getAllDiapers()

    def update(self):
        return self.getAllDiapers()