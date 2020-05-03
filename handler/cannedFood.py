from flask import jsonify
from dao.canedFood import canedFoodDAO


class canedFoodHandler:
    def build_canedFood_dict(self, row):
        result = {}
        result['fid'] = row[0]
        result['type'] = row[1]
        result['is_perishable?'] = row[2]
        result['ingredientlist'] = row[3]
        result['unit_size'] = row[4]
        result['description'] = row[5]
        result['Expiration_date'] = row[6]
        result['price'] = row[7]
        result['location'] = row[8]
        result['quantity'] = row[9]

        return result



    def getAllcanedFood(self):
        dao = canedFoodDAO()
        canedFood_list = dao.getAllcanedFood()
        result_list = []
        for row in canedFood_list:
            result = self.build_canedFood_dict(row)
            result_list.append(result)
        return jsonify(canedFood=result_list)

    def getAllcanedFood(self):
        dao = canedFoodDAO()
        canedFood_list = dao.getAllcanedFood()
        result_list = []
        for row in canedFood_list:
            result = self.build_canedFood_dict(row)
            result_list.append(result)
        return jsonify(canedFood=result_list)

    def getcanedFoodById(self, pid):
        dao = canedFoodDAO()
        canedFood_list = dao.getAllcanedFood()
        result_list = []
        for row in canedFood_list:
            result = self.build_canedFood_dict(row)
            result_list.append(result)
        return jsonify(canedFood=result_list)

    def getcanedFoodByType(self, color):
        dao = canedFoodDAO()
        canedFood_list = dao.getAllcanedFood()
        result_list = []
        for row in canedFood_list:
            result = self.build_canedFood_dict(row)
            result_list.append(result)
        return jsonify(canedFood=result_list)

    def getcanedFoodByIngredient(self, material):
        dao = canedFoodDAO()
        canedFood_list = dao.getAllcanedFood()
        result_list = []
        for row in canedFood_list:
            result = self.build_canedFood_dict(row)
            result_list.append(result)
        return jsonify(canedFood=result_list)

    def getcanedFoodByEXP(self,date):
        dao = canedFoodDAO()
        canedFood_list = dao.getAllcanedFood()
        result_list = []
        for row in canedFood_list:
            result = self.build_canedFood_dict(row)
            result_list.append(result)
        return jsonify(canedFood=result_list)


    def getcanedFoodByPrice(self,price):
        dao = canedFoodDAO()
        canedFood_list = dao.getAllcanedFood()
        result_list = []
        for row in canedFood_list:
            result = self.build_canedFood_dict(row)
            result_list.append(result)
        return jsonify(canedFood=result_list)


    def getcanedFoodByLocation(self,location):
        dao = canedFoodDAO()
        canedFood_list = dao.getAllcanedFood()
        result_list = []
        for row in canedFood_list:
            result = self.build_canedFood_dict(row)
            result_list.append(result)
        return jsonify(canedFood=result_list)



    def insert(self, item):
        return jsonify(canedFood= item) ,200



    def delete(self, pid):
        return jsonify(canedFood= item) ,200



    def update(self, pid):
        return jsonify(canedFood= pid) ,200
