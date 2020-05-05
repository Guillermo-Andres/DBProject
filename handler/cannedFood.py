from flask import jsonify
from dao.cannedFood import cannedFoodDAO


class cannedFoodHandler:
    def build_cannedFood_dict(self, row):
        result = {}
        result['resource id'] = row[0]
        result['baby_food_id'] = row[1]
        result['babyfood_type'] = row[2]
        result['is_perishable?'] = row[3]
        result['ingredientlist'] = row[4]
        result['unit_size'] = row[5]
        result['Expiration_date'] = row[6]
        result['name'] = row[7]
        result['price'] = row[8]
        result['location'] = row[9]
        result['quantity'] = row[10]
        result['description']=row[11]

        return result



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


    def getcannedFoodByLocation(self,location):
        dao = cannedFoodDAO()
        cannedFood_list = dao.getcannedFoodByLocation(location)
        result_list = []
        for row in cannedFood_list:
            result = self.build_cannedFood_dict(row)
            result_list.append(result)
        return jsonify(cannedFood=result_list)



    def insert(self, item):
        return jsonify(cannedFood= item) ,200



    def delete(self, pid):
        return jsonify(cannedFood= item) ,200



    def update(self, pid):
        return jsonify(cannedFood= pid) ,200
