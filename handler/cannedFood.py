from flask import jsonify
from dao.cannedFood import cannedFoodDAO


class cannedFoodHandler:
    def build_cannedFood_dict(self, row):
        result = {'resource id': row[0], 'canned_food_id': row[1], 'cannedfood_type': row[2], 'is_perishable?': row[3],
                  'ingredientlist': row[4], 'unit_size': row[5], 'Expiration_date': row[6], 'name': row[7],
                  'price': row[8], 'location': row[9], 'quantity': row[10], 'description': row[11]}
        return result

    def build_cannedFood_attributes(self, cannedFood_type, cannedFood_is_perishable, cannedFood_ingredients,
                                    cannedFood_unitSize, cannedFood_expDate, resource_name, resource_price,
                                    resource_city, resource_quantity, resource_description, resource_date):
        result = {
            'cannedFood_type': cannedFood_type,
            'cannedFood_is_perishable': cannedFood_is_perishable,
            'cannedFood_ingredients': cannedFood_ingredients,
            'cannedFood_unitSize': cannedFood_unitSize,
            'cannedFood_expDate': cannedFood_expDate,
            'resource_name': resource_name,
            'resource_price': resource_price,
            'resource_city': resource_city,
            'resource_quantity': resource_quantity,
            'resource_description': resource_description,
            'resource_date': resource_date
        }
        return result

    def getAllResourceByKeyword(self, keyword):
        dao = cannedFoodDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_cannedFood_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllcannedFood(self):
        dao = cannedFoodDAO()
        cannedFood_list = dao.getAllcannedFood()
        result_list = []
        for row in cannedFood_list:
            result = self.build_cannedFood_dict(row)
            result_list.append(result)
        return jsonify(cannedFood=result_list)

    def getcannedFoodById(self, pid):
        dao = cannedFoodDAO()
        cannedFood_list = dao.getAllcannedFood()
        result_list = []
        for row in cannedFood_list:
            result = self.build_cannedFood_dict(row)
            result_list.append(result)
        return jsonify(cannedFood=result_list)

    # def getcannedFoodByType(self, color):
    #     dao = cannedFoodDAO()
    #     cannedFood_list = dao.getAllcannedFood()
    #     result_list = []
    #     for row in cannedFood_list:
    #         result = self.build_cannedFood_dict(row)
    #         result_list.append(result)
    #     return jsonify(cannedFood=result_list)
    #
    # def getcannedFoodByIngredient(self, material):
    #     dao = cannedFoodDAO()
    #     cannedFood_list = dao.getAllcannedFood()
    #     result_list = []
    #     for row in cannedFood_list:
    #         result = self.build_cannedFood_dict(row)
    #         result_list.append(result)
    #     return jsonify(cannedFood=result_list)
    #
    # def getcannedFoodByEXP(self,date):
    #     dao = cannedFoodDAO()
    #     cannedFood_list = dao.getAllcannedFood()
    #     result_list = []
    #     for row in cannedFood_list:
    #         result = self.build_cannedFood_dict(row)
    #         result_list.append(result)
    #     return jsonify(cannedFood=result_list)
    #
    #
    # def getcannedFoodByPrice(self,price):
    #     dao = cannedFoodDAO()
    #     cannedFood_list = dao.getAllcannedFood()
    #     result_list = []
    #     for row in cannedFood_list:
    #         result = self.build_cannedFood_dict(row)
    #         result_list.append(result)
    #     return jsonify(cannedFood=result_list)

    def getcannedFoodByLocation(self, location):
        dao = cannedFoodDAO()
        cannedFood_list = dao.getcannedFoodByLocation(location)
        result_list = []
        for row in cannedFood_list:
            result = self.build_cannedFood_dict(row)
            result_list.append(result)
        return jsonify(cannedFood=result_list)

    def insert(self, item):
        cannedFood_type = item['cannedFood_type']
        cannedFood_is_perishable = item['cannedFood_is_perishable']
        cannedFood_ingredients = item['cannedFood_ingredients']
        cannedFood_unitSize = item['cannedFood_unitSize']
        cannedFood_expDate = item['cannedFood_expDate']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if cannedFood_type and cannedFood_is_perishable and cannedFood_ingredients and cannedFood_unitSize and \
                cannedFood_expDate and resource_name and resource_price and resource_city and resource_quantity and \
                resource_description and resource_date:
            dao = cannedFoodDAO()
            rid = dao.insert(cannedFood_type, cannedFood_is_perishable, cannedFood_ingredients, cannedFood_unitSize,
                             cannedFood_expDate, resource_name, resource_price, resource_city, resource_quantity,
                             resource_description, resource_date)
            return jsonify(
                cannedFood=self.build_cannedFood_attributes(cannedFood_type, cannedFood_is_perishable,
                                                            cannedFood_ingredients, cannedFood_unitSize,
                                                            cannedFood_expDate, resource_name, resource_price,
                                                            resource_city, resource_quantity, resource_description,
                                                            resource_date)), 201
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400

    def delete(self, pid):
        return jsonify(cannedFood=pid), 200

    def update(self, pid):
        return jsonify(cannedFood=pid), 200
