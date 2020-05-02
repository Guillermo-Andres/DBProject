from flask import jsonify
from dao.medicalDevices import MedicalDevicesDAO

# medicalDevices attributes: medicalDevices_id, resource_id, medicalDevices_type, medicalDevices_description

class MedicalDevicesHandler:
    def build_medicalDevices_dict(self, row):
        result = {'medicalDevices_id': row[0],
                  'resource_id': row[1],
                  'medicalDevices_type': row[2],
                  'medicalDevices_description': row[3]}
        return result

    def build_resorce_attributes(self, medicalDevices_id, resource_id, medicalDevices_type, medicalDevices_description):
        result = {'medicalDevices_id': medicalDevices_id,
                  'resource_id': resource_id,
                  'medicalDevices_type': medicalDevices_type,
                  'medicalDevices_description': medicalDevices_description}
        return result

    def getAllMedicalDevices(self):
        dao = MedicalDevicesDAO()
        resource_list = dao.getAllMedicalDevices()
        result_list = []
        for row in resource_list:
            result = self.build_medicalDevices_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevices=result_list)

    def getMedicalDevicesById(self, id):
        return self.getAllmedicalDevices()

    def getMedicalDevicesByPrice(self, price):
        return self.getAllmedicalDevices()

    def getMedicalDevicesByLocation(self, location):
        return self.getAllmedicalDevices()

    def getMedicalDevicesByQuantity(self, quantity):
        return self.getAllmedicalDevices()

    def getMedicalDevicesBySize(self, size):
        return self.getAllmedicalDevices()

    def getMedicalDevicesByMaterial(self, material):
        return self.getAllmedicalDevices()

    def getMedicalDevicesByBrand(self, brand):
        return self.getAllmedicalDevices()

    def insert(self, item):
        return jsonify(medicalDevices= item) ,200

    def delete(self,item):
        return jsonify(medicalDevices= item) ,200


    def update(self,item):
        return jsonify(medicalDevices= item) ,200
