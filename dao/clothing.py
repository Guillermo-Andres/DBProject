from config.dbconfig import pg_config
import psycopg2
class ClothingDAO:
    #Clothing ATTTRIBUTES clothing_id, size, color,gender,material,description,price,location,quantity
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host = 127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClothes(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from clothing natural inner join resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothesgById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from clothing natural inner join resource where clothing_id = %s;"
        cursor.execute(query, (id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothesByLocation(self,location):
        cursor = self.conn.cursor()
        query = "select * from clothing natural inner join resource where rlocation = %s;"
        cursor.execute(query, (location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from clothing natural join resource where resource_name  ~*  %s  OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    # def getClothesByType(self, color):
    #     result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
    #     return result
    #
    # def getClothesByGender(self, material):
    #     result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
    #     return result
    #
    # def getClothesByColor(self, material):
    #     result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
    #     return result
    #
    # def getClothesByMaterial(self, material):
    #     result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
    #     return result
    #
    # def ClothesByPrice(self,price):
    #     result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
    #     return result

    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def delete(self, pid):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result
