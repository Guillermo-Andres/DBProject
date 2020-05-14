from flask import jsonify
from dao.babyFood import babyFoodDAO


class babyFoodHandler:
    def build_babyFood_dict(self, row):
        result = {'resource id': row[0], 'baby_food_id': row[1], 'babyfood_type': row[2], 'is_perishable?': row[3],
                  'ingredientlist': row[4], 'unit_size': row[5], 'Expiration_date': row[6], 'name': row[7],
                  'price': row[8], 'location': row[9], 'quantity': row[10], 'description': row[11]}
        return result

    def build_babyFood_attributes(self, babyFood_type, babyFood_is_perishable, babyFood_ingredients, babyFood_unitSize,
                            babyFood_expDate, resource_name, resource_price, resource_city, resource_quantity,
                            resource_description, resource_date):
        result = {
            'babyFood_type': babyFood_type,
            'babyFood_is_perishable': babyFood_is_perishable,
            'babyFood_ingredients': babyFood_ingredients,
            'babyFood_unitSize': babyFood_unitSize,
            'babyFood_expDate': babyFood_expDate,
            'resource_name': resource_name,
            'resource_price': resource_price,
            'resource_city': resource_city,
            'resource_quantity': resource_quantity,
            'resource_description': resource_description,
            'resource_date': resource_date
        }
        return result

    def getAllResourceByKeyword(self, keyword):
        dao = babyFoodDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllbabyFood(self):
        dao = babyFoodDAO()
        babyFood_list = dao.getAllbabyFood()
        result_list = []
        for row in babyFood_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(babyFood=result_list)

    def getbabyFoodById(self, pid):
        dao = babyFoodDAO()
        babyFood_list = dao.getAllbabyFood()
        result_list = []
        for row in babyFood_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(babyFood=result_list)

    def getbabyFoodByLocation(self, location):
        dao = babyFoodDAO()
        babyFood_list = dao.getbabyFoodByLocation(location)
        result_list = []
        for row in babyFood_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(babyFood=result_list)

    def insert(self, item):
        babyFood_type = item['babyFood_type']
        babyFood_is_perishable = item['babyFood_is_perishable']
        babyFood_ingredients = item['babyFood_ingredients']
        babyFood_unitSize = item['babyFood_unitSize']
        babyFood_expDate = item['babyFood_expDate']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if babyFood_type and babyFood_is_perishable and babyFood_ingredients and babyFood_unitSize and babyFood_expDate\
                and resource_name and resource_price and resource_city and resource_quantity and resource_description\
                and resource_date:
            dao = babyFoodDAO()
            rid = dao.insert(babyFood_type, babyFood_is_perishable, babyFood_ingredients, babyFood_unitSize,
                             babyFood_expDate, resource_name, resource_price, resource_city, resource_quantity,
                             resource_description, resource_date)
            return jsonify(BabyFood=self.build_babyFood_attributes(babyFood_type, babyFood_is_perishable,
                            babyFood_ingredients, babyFood_unitSize, babyFood_expDate, resource_name, resource_price,
                            resource_city, resource_quantity, resource_description, resource_date)), 201
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400

    def delete(self, item):
        return jsonify(babyFood=item), 200

    def update(self, pid):
        return jsonify(babyFood=pid), 200
