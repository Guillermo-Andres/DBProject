from config.dbconfig import pg_config
import psycopg2

    # supplier attributes: supplier_id supplier_first_name, supplier_last_name, supplier_dob, supplier_address, supplier_phone_number, supplier_email_address,

class SupplierDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        # cursor = self.conn.cursor()
        # query = "select * from supplier;"
        # cursor.execute(query)
        result = [[1, "Antonio", "Matos", "12/04/1970", "Arroyo, PR", "787-123-4567", "antonio.matos@walmart.com"],
                  [2, "Juan", "Del Pueblo", "06/16/1982", "Humacao, PR", "787-444-4444", "juandelpueblo@sams.com"],
                  [3, "Maria", "Magdalena", "07/17/1992", "Orocovis, PR", "939-333-3333", "mariamagdalena@econo.com"]]
        # for row in cursor:
        #     result.append(row)
        return result

    def getSupplierById(self, id):
        return self.getAllSuppliers()

    def getSupplierByName(self, first_name, last_name):
        return self.getAllSuppliers()

    def getSupplierByDOB(self, dob):
        return self.getAllSuppliers()

    def getSupplierByAddress(self, address):
        return self.getAllSuppliers()

    def getSupplierByPhone(self, phone):
        return self.getAllSuppliers()

    def getSupplierByEmail(self, email):
        return self.getAllSuppliers()

    def insert(self):
        return self.getAllSuppliers()

    def delete(self):
        return self.getAllSuppliers()

    def update(self):
        return self.getAllSuppliers()