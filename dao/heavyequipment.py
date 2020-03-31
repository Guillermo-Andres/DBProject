from config.dbconfig import pg_config
import psycopg2

class HeavyEquipmentDAO:
#HeavyEquipment ATTTRIBUTES heavy_id, description,price,location,quantity

    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllHeavyEquipment(self):

        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result

    def getHeavyEquimentById(self, id):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result

    def getHeavyEquipmentByPrice(self, price):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result

    def getHeavyEquipmentByLocation(self, location):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result

    def insert(self, sname, scity, sphone):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result
    def update(self):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result

    def delete(self):
        result = [[1,'15-ft Camping Tents',0,'Bayamon',1],[2,'20-ft Tents',199.99,'Carolina',2]]
        return result
