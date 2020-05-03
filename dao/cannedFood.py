from config.dbconfig import pg_config
import psycopg2
class cannedFoodDAO:
    #cannedFood ATTTRIBUTES fid, type, isperishable,ingredientlist,unit_size,description, expiration, price , location , quantity
    #def __init__(self):

        #connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            #pg_config['user'],
                                                            #pg_config['passwd'])
        #self.conn = psycopg2._connect(connection_url)

    def getAllcannedFood(self):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def getcannedFoodById(self, pid):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result
    def getcannedFoodByType(self, color):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def getcannedFoodByIngredient(self, material):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def getcannedFoodByEXP(self,date):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def getcannedFoodByPrice(self,price):
        result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
        return result

    def getcannedFoodByLocation(self,location):
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
