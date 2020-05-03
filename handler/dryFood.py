from flask import jsonify
from dao.dryFood import dryFoodDAO


class dryFoodHandler:
    def build_dryFood_dict(self, row):
        result = {}
        result['resource id'] = row[0]
        result['baby_food_id'] = row[1]
        result['dryFood_type'] = row[2]
        result['is_perishable?'] = row[3]
        result['ingredientlist'] = row[4]
        result['unit_size'] = row[5]
        result['description'] = row[6]
        result['Expiration_date'] = row[7]
        result['price'] = row[8]
        result['location'] = row[9]
        result['quantity'] = row[10]

        return result



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

    # def getdryFoodByType(self, color):
    #     dao = dryFoodDAO()
    #     dryFood_list = dao.getAlldryFood()
    #     result_list = []
    #     for row in dryFood_list:
    #         result = self.build_dryFood_dict(row)
    #         result_list.append(result)
    #     return jsonify(dryFood=result_list)
    #
    # def getdryFoodByIngredient(self, material):
    #     dao = dryFoodDAO()
    #     dryFood_list = dao.getAlldryFood()
    #     result_list = []
    #     for row in dryFood_list:
    #         result = self.build_dryFood_dict(row)
    #         result_list.append(result)
    #     return jsonify(dryFood=result_list)
    #
    # def getdryFoodByEXP(self,date):
    #     dao = dryFoodDAO()
    #     dryFood_list = dao.getAlldryFood()
    #     result_list = []
    #     for row in dryFood_list:
    #         result = self.build_dryFood_dict(row)
    #         result_list.append(result)
    #     return jsonify(dryFood=result_list)
    #
    #
    # def getdryFoodByPrice(self,price):
    #     dao = dryFoodDAO()
    #     dryFood_list = dao.getAlldryFood()
    #     result_list = []
    #     for row in dryFood_list:
    #         result = self.build_dryFood_dict(row)
    #         result_list.append(result)
    #     return jsonify(dryFood=result_list)


    def getdryFoodByLocation(self,location):
        dao = dryFoodDAO()
        dryFood_list = dao.getdryFoodByLocation(location)
        result_list = []
        for row in dryFood_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(dryFood=result_list)



    def insert(self, item):
        return jsonify(dryFood= item) ,200



    def delete(self, pid):
        return jsonify(dryFood= item) ,200



    def update(self, pid):
        return jsonify(dryFood= pid) ,200
