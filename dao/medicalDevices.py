from config.dbconfig import pg_config
import psycopg2


class MedicalDevicesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from medicalDevices natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicalDevicesById(self, medicalDevices_id):
        cursor = self.conn.cursor()
        query = "select *" \
                "from medicalDevices natural inner join resource" \
                "where medicalDevices_id = %s;"
        # TODO - check joins
        cursor.execute(query, (medicalDevices_id,))
        result = cursor.fetchone()
        return result

    def getMedicalDevicesByPrice(self, price):
        return self.getAllDiapers()

    def getMedicalDevicesByLocation(self, location):
        return self.getAllDiapers()

    def getMedicalDevicesByQuantity(self, quantity):
        return self.getAllDiapers()

    def getMedicalDevicesBySize(self, size):
        return self.getAllDiapers()

    def getMedicalDevicesByMaterial(self, material):
        return self.getAllDiapers()

    def getMedicalDevicesByBrand(self, brand):
        return self.getAllDiapers()

    def insert(self):
        return self.getAllDiapers()

    def delete(self):
        return self.getAllDiapers()

    def update(self):
        return self.getAllDiapers()
