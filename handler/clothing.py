from flask import jsonify
from dao.clothing import ClothingDAO

    #Clothing ATTTRIBUTES clothing_id, size, color,gender,material,description

class ClothingHandler:
    def build_Clothes_dict(self, row):
        result = {}
        result['clothing_id'] = row[0]
        result['size'] = row[1]
        result['color'] = row[2]
        result['gender'] = row[3]
        result['material'] = row[4]
        result['description'] = row[5]
        result['price'] = row[6]
        result['location'] = row[7]
        result['quantity'] = row[8]




        return result



    def getAllClothes(self):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getAllClothes(self):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClothesgById(self, pid):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
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
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def insert(self, pname):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def delete(self, pid):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def update(self, pid):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)
