from config.dbconfig import pg_config
import psycopg2


class babyFoodDAO:
    # babyFood ATTTRIBUTES fid, type, isperishable,ingredientlist,unit_size,description, expiration, price ,
    # location , quantity
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

    def getResourceByKeyWord(self, keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from babyFood natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query, (keyword, keyword,))
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

    def getbabyFoodByLocation(self, location):
        cursor = self.conn.cursor()
        query = "select * from babyFood natural inner join resource where rlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, babyFood_type, babyFood_is_perishable, babyFood_ingredients, babyFood_unitSize, babyFood_expDate,
               resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date):
        cursor = self.conn.cursor()
        query = "insert into resource (resource_name,resource_price,resource_city,resource_quantity," \
                "resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id; "
        cursor.execute(query, (resource_name, resource_price, resource_city, resource_quantity, resource_description,
                               resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into babyFood (resource_id, babyFood_type, babyFood_is_perishable, babyFood_ingredients, " \
                "babyFood_unitSize, babyFood_expDate) values (%s, %s, %s, %s, %s, %s); "
        cursor.execute(query, (rid, babyFood_type, babyFood_is_perishable, babyFood_ingredients, babyFood_unitSize, babyFood_expDate,))
        self.conn.commit()
        cursor.close()
        return rid


    def delete(self, pid):
        result = [[1, 'canned', 'no', 'beans', '12oz', 'red beans', '12/25/2022', 0, 'SanJuan', 3],
                  [2, 'fruit', 'yes', 'organic bannanas', '5 lb', 'bannana', '12/25/2022', 4.99, 'Ponce', 6],
                  [3, 'meat', 'yes', 'codero flesh', '8 Oz', 'Corderito', '12/25/2022', 0, 'Aguadilla', 1]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1, 'canned', 'no', 'beans', '12oz', 'red beans', '12/25/2022', 0, 'SanJuan', 3],
                  [2, 'fruit', 'yes', 'organic bannanas', '5 lb', 'bannana', '12/25/2022', 4.99, 'Ponce', 6],
                  [3, 'meat', 'yes', 'codero flesh', '8 Oz', 'Corderito', '12/25/2022', 0, 'Aguadilla', 1]]
        return result
