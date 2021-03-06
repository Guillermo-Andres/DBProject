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

    def insert(self, clothing_size, clothing_color, clothing_gender, clothing_material, resource_name, resource_price,
               resource_city, resource_quantity, resource_description, resource_date,supplier_id):
        cursor = self.conn.cursor()
        query = "insert into resource (resource_name,resource_price,resource_city,resource_quantity," \
                "resource_description, resource_date) values (%s, %s, %s, %s, %s, %s) returning resource_id; "
        cursor.execute(query, (resource_name, resource_price, resource_city, resource_quantity, resource_description,
                               resource_date,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        query = "insert into clothing (resource_id, clothing_size, clothing_color, clothing_gender, " \
                "clothing_material) values (%s, %s, %s, %s, %s) "
        cursor.execute(query, (rid, clothing_size, clothing_color, clothing_gender, clothing_material,))
        self.conn.commit()
        query = 'insert into supplies(supplier_id , resource_id) values(%s,%s);'
        cursor.execute(query, (supplier_id,rid,))
        self.conn.commit()
        cursor.close()
        return rid


    def delete(self, pid):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result

    def update(self, pid, pname, pcolor, pmaterial, pprice):
        result = [[1,'small','blue','unisex','cotton','solid blue short',6.99,'gurabo',1],[2,'medium','blue','unisex','jean','regular denim jeans',15.99,'caguas',2],[3,'XL','black','Male','cotton','solid Polo tee',0,'Quebadillas',1]]
        return result
