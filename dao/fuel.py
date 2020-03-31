from config.dbconfig import pg_config
import psycopg2
class FuelDAO:
    #Fuel ATTTRIBUTES fid, type,unit_size,description,price,location,quantity
    # def __init__(self):
    #
    #     connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
    #                                                         pg_config['user'],
    #                                                         pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):

        result = [[1,'Propane','12 Oz' , '1 Propane gas Tank',0,'Maunabo',12],[2,'Gas','24 Galons', '24 Gallons of liquid fuel',6.99,'Carolina',24],[3,'Disel','5 Galons','5 Galons of Disel',56.00,'Mayaguez',15]]
        return result

    def getFuelById(self, id):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

     def getFuelByType(self, type):
         result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
         return result

    def getFuelBySize(self, size):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def getFuelByPrice(self, price):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def getFuelByLocation(self, location):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def delete(self, pid):
         result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
         return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result
