from config.dbconfig import pg_config
import psycopg2


# supplier attributes: supplier_id supplier_first_name, supplier_last_name, supplier_dob, supplier_address,
# supplier_phone_number, supplier_email_address,

class SupplierDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from supplier natural inner join person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # TODO - check joins
    def getSupplierById(self, supplier_id):
        cursor = self.conn.cursor()
        query = "select *" \
                "from supplier natural inner join person" \
                "where supplier_id = %s;"
        result = cursor.execute(query, (supplier_id,))
        return result

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

    def insert(self, first_name, last_name, dob, address, phone_number, email):
        cursor = self.conn.cursor()
        query = "insert into person(person_firstname, person_lastname , person_dob , person_address , " \
                "person_phone_number, person_email ) values(%s , %s , %s , %s , %s , %s); "
        cursor.execute(query, (first_name, last_name, dob, address, phone_number, email,))
        user_id = cursor.fetchone()[0]
        self.conn.commit()
        cursor = self.conn.cursor()
        query = "insert into supplier(person_id) values(%s)"
        cursor.execute(query, (user_id,))
        self.conn.commit()
        return user_id

    def delete(self):
        return self.getAllSuppliers()

    def update(self):
        return self.getAllSuppliers()
