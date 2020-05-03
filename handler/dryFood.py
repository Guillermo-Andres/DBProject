from flask import jsonify
from dao.dryFood import dryFoodDAO


class dryFoodHandler:
    def build_dryFood_dict(self, row):
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



    def getAlldryFood(self):
        dao = dryFoodDAO()
        dryFood_list = dao.getAlldryFood()
        result_list = []
        for row in dryFood_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(dryFood=result_list)

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

    def getdryFoodByType(self, color):
        dao = dryFoodDAO()
        dryFood_list = dao.getAlldryFood()
        result_list = []
        for row in dryFood_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(dryFood=result_list)

    def getdryFoodByIngredient(self, material):
        dao = dryFoodDAO()
        dryFood_list = dao.getAlldryFood()
        result_list = []
        for row in dryFood_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(dryFood=result_list)

    def getdryFoodByEXP(self,date):
        dao = dryFoodDAO()
        dryFood_list = dao.getAlldryFood()
        result_list = []
        for row in dryFood_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(dryFood=result_list)


    def getdryFoodByPrice(self,price):
        dao = dryFoodDAO()
        dryFood_list = dao.getAlldryFood()
        result_list = []
        for row in dryFood_list:
            result = self.build_dryFood_dict(row)
            result_list.append(result)
        return jsonify(dryFood=result_list)


    def getdryFoodByLocation(self,location):
        dao = dryFoodDAO()
        dryFood_list = dao.getAlldryFood()
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
