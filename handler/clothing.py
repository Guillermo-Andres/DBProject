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




        return result



    def getAllClothes(self):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)
