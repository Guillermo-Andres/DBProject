from config.dbconfig import pg_config
import psycopg2
class ClothingDAO:
    #Clothing ATTTRIBUTES clothing_id, size, color,gender,material,description,price,location,quantity
    # def __init__(self):
        #
        # connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        #                                                     pg_config['user'],
        #                                                     pg_config['passwd'])
        # self.conn = psycopg2._connect(connection_url)

    def getAllClothes(self):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def getClothesgById(self, pid):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def getClothesByType(self, color):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def getClothesByGender(self, material):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def getClothesByColor(self, material):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def getClothesByMaterial(self, material):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def ClothesByPrice(self,price):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def getClothesByLocation(self,location):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result


    def insert(self, pname, pcolor, pmaterial, pprice):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def delete(self, pid):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result
