from flask import jsonify
from dao.medication import MedicationDAO

    # Medication ATTTRIBUTES medication_id, name,ingredient,type,exp,price,location,quantity

class MedicationHandler:
    def build_Medication_dict(self, row):
        result = {'resource_id': row[0], 'medication_id': row[1], 'ingredients': row[2], 'type': row[3],
                  'expiration_date': row[4], 'name': row[5], 'price': row[6], 'location': row[7], 'quantity': row[8],
                  'description': row[9]}
        return result

    def build_medication_attrs(self, medication_ingredients, medication_type, medication_expDate, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date):
        result = {
        'medication_ingredients' : medication_ingredients,
        'medication_type': medication_type,
        'medication_expDate': medication_expDate,
        'resource_name': resource_name,
        'resource_price': resource_price,
        'resource_city': resource_city,
        'resource_quantity': resource_quantity,
        'resource_description': resource_description,
        'resource_date': resource_date
        }
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

    def insert(self,item,supplier_id):
        medication_ingredients = item['medication_ingredients']
        medication_type = item['medication_type']
        medication_expDate = item['medication_expDate']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if medication_ingredients and medication_type and medication_expDate and resource_name and resource_price and resource_city and resource_quantity and resource_description and resource_date:
            dao = MedicationDAO()
            rid = dao.insert(medication_ingredients, medication_type, medication_expDate, resource_name, resource_price,
                             resource_city, resource_quantity, resource_description, resource_date,supplier_id)
            return jsonify(Medication=self.build_medication_attrs(medication_ingredients, medication_type, medication_expDate, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date))
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400
