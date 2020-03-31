from config.dbconfig import pg_config
import psycopg2
class IceDAO:
    #ICE ATTTRIBUTES iid, size,quantity,description,price,location,

    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)


    def build_ice_dict(self , row):
        iceDict = {}

        iceDict['iid'] = row[0]
        iceDict['size'] = row[1]
        iceDict['unit_size'] = row[2]
        iceDict['description'] = row[3]

        return iceDict






    def getAllIce(self):

        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result

    def getIceById(self, id):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result

    def getIceBySize(self, size):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result

    def getIceByPrice(self,price):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result

    def getIceByLocation(self,location):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result

    def delete(self, pid):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'8 Oz',1, '8 Oz bag of ice',0,'Guayanilla'],[2,'6 Oz',1, '6 Oz bag of ice',4.99,'Humacao'],[3,'12 Oz',6, '12 Oz bag of ice',0,'Coamo',0]]
        return result
