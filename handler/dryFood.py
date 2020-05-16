from flask import jsonify
from dao.dryFood import dryFoodDAO


class dryFoodHandler:
    def build_dryFood_dict(self, row):
        result = {'resource id': row[0], 'dry_food_id': row[1], 'dryfood_type': row[2], 'is_perishable?': row[3],
                  'ingredientlist': row[4], 'unit_size': row[5], 'Expiration_date': row[6], 'name': row[7],
                  'price': row[8], 'location': row[9], 'quantity': row[10], 'description': row[11]}
        return result

    def build_dryFood_attributes(self, dryFood_type, dryFood_is_perishable, dryFood_ingredients, dryFood_unitSize,
                                 dryFood_expDate, resource_name, resource_price, resource_city, resource_quantity,
                                 resource_description, resource_date):
        result = {
            'dryFood_type': dryFood_type,
            'dryFood_is_perishable': dryFood_is_perishable,
            'dryFood_ingredients': dryFood_ingredients,
            'dryFood_unitSize': dryFood_unitSize,
            'dryFood_expDate': dryFood_expDate,
            'resource_name': resource_name,
            'resource_price': resource_price,
            'resource_city': resource_city,
            'resource_quantity': resource_quantity,
            'resource_description': resource_description,
            'resource_date': resource_date
        }
        return result

    def getAllResourceByKeyword(self, keyword):
        dao = dryFoodDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAlldryFood(self):
        dao = dryFoodDAO()
        dryFood_list = dao.getAlldryFood()
        result_list = []
        for row in dryFood_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(dryFood=result_list)

    def getdryFoodById(self, pid):
        dao = dryFoodDAO()
        dryFood_list = dao.getAlldryFood()
        result_list = []
        for row in dryFood_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(dryFood=result_list)



    def getdryFoodByLocation(self, location):
        dao = dryFoodDAO()
        dryFood_list = dao.getdryFoodByLocation(location)
        result_list = []
        for row in dryFood_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(dryFood=result_list)

    def insert(self, item,supplier_id):
        dryFood_type = item['dryFood_type']
        dryFood_is_perishable = item['dryFood_is_perishable']
        dryFood_ingredients = item['dryFood_ingredients']
        dryFood_unitSize = item['dryFood_unitSize']
        dryFood_expDate = item['dryFood_expDate']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if dryFood_type and dryFood_is_perishable and dryFood_ingredients and dryFood_unitSize and dryFood_expDate and resource_name and resource_price and resource_city and resource_quantity and resource_description and resource_date:
            dao = dryFoodDAO()
            rid = dao.insert(dryFood_type, dryFood_is_perishable, dryFood_ingredients, dryFood_unitSize,
                             dryFood_expDate, resource_name, resource_price, resource_city, resource_quantity,
                             resource_description, resource_date,supplier_id)
            return jsonify(
                dryFood=self.build_dryFood_attributes(dryFood_type, dryFood_is_perishable, dryFood_ingredients,
                                                      dryFood_unitSize, dryFood_expDate, resource_name,
                                                      resource_price, resource_city, resource_quantity,
                                                      resource_description, resource_date)), 201
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400

    def delete(self, pid):
        return jsonify(dryFood=pid), 200

    def update(self, pid):
        return jsonify(dryFood=pid), 200
