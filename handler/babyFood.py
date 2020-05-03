from flask import jsonify
from dao.babyFood import babyFoodDAO


class babyFoodHandler:
    def build_babyFood_dict(self, row):
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



    def getAllbabyFood(self):
        dao = babyFoodDAO()
        babyFood_list = dao.getAllbabyFood()
        result_list = []
        for row in babyFood_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(babyFood=result_list)

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

    def getbabyFoodByType(self, color):
        dao = babyFoodDAO()
        babyFood_list = dao.getAllbabyFood()
        result_list = []
        for row in babyFood_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(babyFood=result_list)

    def getbabyFoodByIngredient(self, material):
        dao = babyFoodDAO()
        babyFood_list = dao.getAllbabyFood()
        result_list = []
        for row in babyFood_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(babyFood=result_list)

    def getbabyFoodByEXP(self,date):
        dao = babyFoodDAO()
        babyFood_list = dao.getAllbabyFood()
        result_list = []
        for row in babyFood_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(babyFood=result_list)


    def getbabyFoodByPrice(self,price):
        dao = babyFoodDAO()
        babyFood_list = dao.getAllbabyFood()
        result_list = []
        for row in babyFood_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(babyFood=result_list)


    def getbabyFoodByLocation(self,location):
        dao = babyFoodDAO()
        babyFood_list = dao.getAllbabyFood()
        result_list = []
        for row in babyFood_list:
            result = self.build_babyFood_dict(row)
            result_list.append(result)
        return jsonify(babyFood=result_list)



    def insert(self, item):
        return jsonify(babyFood= item) ,200



    def delete(self, pid):
        return jsonify(babyFood= item) ,200



    def update(self, pid):
        return jsonify(babyFood= pid) ,200
