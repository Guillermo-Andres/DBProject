from config.dbconfig import pg_config
import psycopg2
class MedicationDAO:
    #Medication ATTTRIBUTES medication_id, name,ingredient,type,exp,price,location,quantity
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMedication(self):
        cursor = self.conn.cursor()
        query = "select * from medication natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicationById(self, id):
        cursor = self.conn.cursor()
        query = "select * from medication natural inner join resource where medication_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getMedicationByName(self, name):
        result = [[1,'cannabis','OG Ganja','Natural','12/25/2021',35.00,'Trujillo Alto',3],[2,'tylenol','ibuprofen','pills','12/25/2021',35.00,'Trujillo Alto',3],[3,'viagra','cosa buena','pills','12/25/2021',35.00,'Trujillo Alto',3]]
        return result
    def getMedicationByType(self, type):
        result = [[1,'cannabis','OG Ganja','Natural','12/25/2021',35.00,'Trujillo Alto',3],[2,'tylenol','ibuprofen','pills','12/25/2021',35.00,'Trujillo Alto',3],[3,'viagra','cosa buena','pills','12/25/2021',35.00,'Trujillo Alto',3]]
        return result
    def getMedicationByIngredient(self, ingredient):
        result = [[1,'cannabis','OG Ganja','Natural','12/25/2021',35.00,'Trujillo Alto',3],[2,'tylenol','ibuprofen','pills','12/25/2021',35.00,'Trujillo Alto',3],[3,'viagra','cosa buena','pills','12/25/2021',35.00,'Trujillo Alto',3]]
        return result
    def getMedicationByPrice(self, price):
        result = [[1,'cannabis','OG Ganja','Natural','12/25/2021',35.00,'Trujillo Alto',3],[2,'tylenol','ibuprofen','pills','12/25/2021',35.00,'Trujillo Alto',3],[3,'viagra','cosa buena','pills','12/25/2021',35.00,'Trujillo Alto',3]]
        return result
    def getMedicationByLocation(self, location):
        result = [[1,'cannabis','OG Ganja','Natural','12/25/2021',35.00,'Trujillo Alto',3],[2,'tylenol','ibuprofen','pills','12/25/2021',35.00,'Trujillo Alto',3],[3,'viagra','cosa buena','pills','12/25/2021',35.00,'Trujillo Alto',3]]
        return result



    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'cannabis','OG Ganja','Natural','12/25/2021',35.00,'Trujillo Alto',3],[2,'tylenol','ibuprofen','pills','12/25/2021',35.00,'Trujillo Alto',3],[3,'viagra','cosa buena','pills','12/25/2021',35.00,'Trujillo Alto',3]]
        return result

    def delete(self, pid):
        result = [[1,'cannabis','OG Ganja','Natural','12/25/2021',35.00,'Trujillo Alto',3],[2,'tylenol','ibuprofen','pills','12/25/2021',35.00,'Trujillo Alto',3],[3,'viagra','cosa buena','pills','12/25/2021',35.00,'Trujillo Alto',3]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'cannabis','OG Ganja','Natural','12/25/2021',35.00,'Trujillo Alto',3],[2,'tylenol','ibuprofen','pills','12/25/2021',35.00,'Trujillo Alto',3],[3,'viagra','cosa buena','pills','12/25/2021',35.00,'Trujillo Alto',3]]
        return result
