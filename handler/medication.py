from flask import jsonify
from dao.medication import MedicationDAO


class MedicationHandler:
    def build_Medication_dict(self, row):
        result = {}
        result['medication_id'] = row[0]
        result['name'] = row[1]
        result['ingredients'] = row[2]
        result['type'] = row[3]


        return result



    def getAllMedication(self):
        dao = MedicationDAO()
        medication_list = dao.getAllMedication()
        result_list = []
        for row in medication_list:
            result = self.build_Medication_dict(row)
            result_list.append(result)
        return jsonify(Medication=result_list)
