from config.dbconfig import pg_config
import psycopg2


class HygieneDAO:

    # hygiene attributes: hygiene_id, hygiene_expiration_date, hygiene_price, hygiene_location, hygiene_units,
    # hygiene_description, hygiene_quantity_per_unit, hygiene_brand

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHygiene(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from hygiene natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHygieneById(self, hygiene_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from hygiene natural inner join resource" \
                " where hygiene_id = %s;"
        cursor.execute(query, (hygiene_id,))
        result = cursor.fetchone()
        return result


    def getResourceByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from hygiene natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

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

    def insert(self, hygiene_quantityPerUnit, hygiene_brand, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date):
        cursor = self.conn.cursor()
        query = "insert into resource (resource_name,resource_price,resource_city,resource_quantity," \
                "resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id; "
        cursor.execute(query, (resource_name, resource_price, resource_city, resource_quantity, resource_description,
                               resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into hygiene (resource_id, hygiene_quantityPerUnit, hygiene_brand) values (%s, %s, %s)"
        cursor.execute(query, (rid, hygiene_quantityPerUnit, hygiene_brand,))
        self.conn.commit()
        cursor.close()
        return rid


    def delete(self):
        return self.getAllHygiene()

    def update(self):
        return self.getAllHygiene()
