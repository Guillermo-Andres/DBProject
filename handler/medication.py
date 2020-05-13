from flask import jsonify
from dao.medication import MedicationDAO

    # Medication ATTTRIBUTES medication_id, name,ingredient,type,exp,price,location,quantity

class MedicationHandler:
    def build_Medication_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['medication_id'] = row[1]
        result['ingredients'] = row[2]
        result['type'] = row[3]
        result['expiration_date'] = row[4]
        result['name'] = row[5]
        result['price'] = row[6]
        result['location'] = row[7]
        result['quantity'] = row[8]
        result['description'] = row[9]
        return result



    def getAllResourceByKeyword(self , keyword):
        dao = MedicationDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_Medication_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllMedication(self):
        dao = MedicationDAO()
        medication_list = dao.getAllMedication()
        result_list = []
        for row in medication_list:
            result = self.build_Medication_dict(row)
            result_list.append(result)
        return jsonify(Medication=result_list)

    def getMedicationById(self, id):
        dao = MedicationDAO()
        medication_list = dao.getMedicationById(id)
        result_list = []
        for row in medication_list:
            result = self.build_Medication_dict(row)
            result_list.append(result)
        return jsonify(Medication=result_list)

    def getMedicationByName(self, name):
        return self.getAllMedication()

    def getMedicationByIngredients(self, ingredients):
        return self.getAllMedication()

    def getMedicationByType(self, type):
        return self.getAllMedication()

    def getMedicationByExpirationDate(self, expiration_date):
        return self.getAllMedication()

    def getMedicationByPrice(self, price):
        return self.getAllMedication()

    def getMedicationByLocation(self, location):
        dao = MedicationDAO()
        medication_list = dao.getMedicationByLocation(location)
        result_list = []
        for row in medication_list:
            result = self.build_Medication_dict(row)
            result_list.append(result)
        return jsonify(Medication=result_list)

    def getMedicationByQuantity(self, quantity):
        return self.getAllMedication()

    def insert(self,item):
        return jsonify(Medication= item) ,200

    def delete(self,item):
        return jsonify(Medication= item) ,200


    def update(self,item):
        return jsonify(Medication= item) ,200
