from config.dbconfig import pg_config
import psycopg2
class babyFoodDAO:
    #babyFood ATTTRIBUTES fid, type, isperishable,ingredientlist,unit_size,description, expiration, price , location , quantity
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllbabyFood(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from babyFood natural  join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getbabyFoodById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from babyFood natural join resource where ice_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # def getbabyFoodByType(self, color):
    #     result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
    #     return result
    #
    # def getbabyFoodByIngredient(self, material):
    #     result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
    #     return result
    #
    # def getbabyFoodByEXP(self,date):
    #     result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
    #     return result
    #
    # def getbabyFoodByPrice(self,price):
    #     result = [[1,'canned','no','beans','12oz','red beans','12/25/2022',0,'SanJuan',3],[2,'fruit','yes','organic bannanas','5 lb','bannana','12/25/2022', 4.99,'Ponce',6],[3,'meat','yes','codero flesh','8 Oz','Corderito','12/25/2022',0,'Aguadilla',1]]
    #     return result

    def getbabyFoodByLocation(self,location):
        cursor = self.conn.cursor()
        query = "select * from babyFood natural inner join resource where rlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
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
