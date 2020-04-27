from flask import jsonify
from dao.medication import MedicationDAO

    # Medication ATTTRIBUTES medication_id, name,ingredient,type,exp,price,location,quantity

class MedicationHandler:
    def build_Medication_dict(self, row):
        result = {}
        result['medication_id'] = row[0]
        result['name'] = row[1]
        result['ingredients'] = row[2]
        result['type'] = row[3]
        result['expiration_date'] = row[4]
        result['price'] = row[5]
        result['location'] = row[6]
        result['quantity'] = row[7]
        return result



    def getAllMedication(self):
        dao = MedicationDAO()
        medication_list = dao.getAllMedication()
        result_list = []
        for row in medication_list:
            result = self.build_Medication_dict(row)
            result_list.append(result)
        return jsonify(Medication=result_list)

    def getMedicationById(self, id):
        return self.getAllMedication()

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
        return self.getAllMedication()

    def getMedicationByQuantity(self, quantity):
        return self.getAllMedication()

    def insert(self,item):
        return jsonify(Medication= item) ,200

    def delete(self,item):
        return jsonify(Medication= item) ,200


    def update(self,item):
        return jsonify(Medication= item) ,200
