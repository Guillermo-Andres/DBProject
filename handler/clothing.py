from flask import jsonify
from dao.clothing import ClothingDAO

    #Clothing ATTTRIBUTES clothing_id, size, color,gender,material,description

class ClothingHandler:
    def build_Clothes_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['clothing_id'] = row[1]
        result['size'] = row[2]
        result['color'] = row[3]
        result['gender'] = row[4]
        result['material'] = row[5]
        result['name'] = row[6]
        result['price'] = row[7]
        result['location'] = row[8]
        result['quantity'] = row[9]
        resource['descrition']=row[10]

        return result





    def getAllResourceByKeyword(self , keyword):
        dao = ClothingDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllClothes(self):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClothesgById(self, id):
        dao = ClothingDAO()
        clothes_list = dao.getClothesgById(id)
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClothesByType(self, color):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClothesByGender(self, material):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)


    def getClothesByColor(self, material):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClothesByMaterial(self, material):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def ClothesByPrice(self,price):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClothesByLocation(self,location):
        dao = ClothingDAO()
        clothes_list = dao.getClothesByLocation(location)
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def insert(self, pname):
        return jsonify(Clothes= item) ,200


    def delete(self, item):
        return jsonify(Clothes= item) ,200

    def update(self, item):
        return jsonify(Clothes= item) ,200
