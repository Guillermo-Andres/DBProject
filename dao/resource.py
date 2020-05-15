from config.dbconfig import pg_config
import psycopg2
from dao.babyFood import babyFoodDAO
from dao.cannedFood import cannedFoodDAO
from dao.dryFood import dryFoodDAO
from dao.medication import MedicationDAO
from dao.batteries import BatteryDAO
from dao.clothing import ClothingDAO
from dao.heavyequipment import HeavyEquipmentDAO
from dao.ice import IceDAO
from dao.powertools import ToolsDAO
from dao.fuel import FuelDAO
from dao.medicalDevices import MedicalDevicesDAO
from dao.powerGenerator import PowerGeneratorDAO
from dao.hygiene import HygieneDAO
from dao.water import WaterDAO


# resource_id , resource_name , resource_price, resource_city, resource_quantity  , resource_description , resource_date

class ResourceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResource(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, resource_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from resource " \
                "where resource_id = %s;"
        cursor.execute(query, (resource_id,))
        result = cursor.fetchone()
        return result

    def getResourcesInStock(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from resource " \
                "where resource_quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        
    def getResourceByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceAvailablePerDay(self):
        cursor = self.conn.cursor()
        query = "select resource_name, count(resource_name) as available, date_trunc('day'," \
                "resource_date) as day " \
                "from resource " \
                "where resource_quantity > 0 " \
                "group by day, resource_name " \
                "order by day;"
        cursor.execute(query)
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return result

    def getResourceAvailablePerWeek(self):
        cursor = self.conn.cursor()
        query = "select resource_name, count(resource_name) as available, date_trunc('week'," \
                "resource_date) as week " \
                "from resource " \
                "where resource_quantity > 0 " \
                "group by week, resource_name " \
                "order by week;"
        cursor.execute(query)
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return result

    def getResourceAvailablePerRegion(self):
        cursor = self.conn.cursor()
        query = "select resource_name, count(resource_name) as available, get_region(resource_city) as region " \
                "from resource " \
                "group by region, resource_name " \
                "order by region;"
        cursor.execute(query)
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return result


    def getDAO(self , type):
        if(type == 'babyfood'):
            return babyFoodDAO()
        elif(type == 'dryfood'):
            return dryFoodDAO()
        elif(type == 'cannedfood'):
            return cannedFoodDAO()
        elif(type == 'medication'):
            return MedicationDAO()
        elif(type == 'batteries'):
            return BatteryDAO()
        elif(type == 'clothing'):
            return ClothingDAO()
        elif(type == 'heavyequipment'):
            return HeavyEquipmentDAO()
        elif(type == 'ice'):
            return IceDAO()
        elif(type == 'powertools'):
            return PowerToolsDAO()
        elif(type == 'fuel'):
            return FuelDAO()
        elif(type == 'medicaldevices'):
            return MedicalDevicesDAO()
        elif(type == 'powergenerator'):
            return PowerGeneratorDAO()
        elif(type == 'hygiene'):
            return HygieneDAO()
        elif(type == 'water'):
            return WaterDAO()

    def getResourceByName(self, resource_first_name, resource_last_name):
        return self.getAllResource()

    def getResourceByDOB(self, dob):
        return self.getAllResource()

    def getResourceByAddress(self, address):
        return self.getAllResource()

    def getResourceByPhoneNumber(self, phone_number):
        return self.getAllResource()

    def getResourceByEmail(self, email):
        return self.getAllResource()

    def getResourceBySeverity(self, severity):
        return self.getAllResource()

    def insert(self, item):
        return self.getAllResource()

    def delete(self, cid):
        return self.getAllResource()

    def update(self, payment_method_id):
        return self.getAllResource()
