from flask import jsonify
from dao.clothing import ClothingDAO


# Clothing ATTTRIBUTES clothing_id, size, color,gender,material,description

class ClothingHandler:
    def build_Clothes_dict(self, row):
        result = {'resource_id': row[0], 'clothing_id': row[1], 'size': row[2], 'color': row[3], 'gender': row[4],
                  'material': row[5], 'name': row[6], 'price': row[7], 'location': row[8], 'quantity': row[9],
                  'descrition': row[10]}

        return result

    def build_clothes_attrs(self, clothing_size, clothing_color, clothing_gender, clothing_material, resource_name,
                            resource_price, resource_city, resource_quantity, resource_description, resource_date):
        result = {
            'clothing_size': clothing_size,
            'clothing_color': clothing_color,
            'clothing_gender': clothing_gender,
            'clothing_material': clothing_material,
            'resource_name': resource_name,
            'resource_price': resource_price,
            'resource_city': resource_city,
            'resource_quantity': resource_quantity,
            'resource_description': resource_description,
            'resource_date': resource_date
        }
        return result

    def getAllResourceByKeyword(self, keyword):
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

    def ClothesByPrice(self, price):
        dao = ClothingDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def getClothesByLocation(self, location):
        dao = ClothingDAO()
        clothes_list = dao.getClothesByLocation(location)
        result_list = []
        for row in clothes_list:
            result = self.build_Clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)

    def insert(self, item,supplier_id):
        clothing_size = item['clothing_size']
        clothing_color = item['clothing_color']
        clothing_gender = item['clothing_gender']
        clothing_material = item['clothing_material']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if clothing_size and clothing_color and clothing_gender and clothing_material and resource_name \
                and resource_price and resource_city and resource_quantity and resource_description and resource_date:
            dao = ClothingDAO()
            rid = dao.insert(clothing_size, clothing_color, clothing_gender, clothing_material, resource_name,
                             resource_price, resource_city, resource_quantity, resource_description, resource_date,supplier_id)
            return jsonify(Clothing=self.build_clothes_attrs(clothing_size, clothing_color, clothing_gender,
                                                             clothing_material, resource_name, resource_price,
                                                             resource_city, resource_quantity, resource_description,
                                                             resource_date))
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400

    def delete(self, item):
        return jsonify(Clothes=item), 200

    def update(self, item):
        return jsonify(Clothes=item), 200
