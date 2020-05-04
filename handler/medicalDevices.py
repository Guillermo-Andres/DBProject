from flask import jsonify
from dao.medicalDevices import MedicalDevicesDAO


# medicalDevices attributes: medicalDevices_id, resource_id, medicalDevices_type, medicalDevices_description

class MedicalDevicesHandler:
    def build_medicalDevices_dict(self, row):
        result = {'resource_id': row[0],
                  'medicalDevices_id': row[1],
                  'medicalDevices_type': row[2],
                  'resource_name': row[4],
                  'resource_price': row[5],
                  'resource_location': row[6],
                  'resource_quantity': row[7],
                  'available': row[8],
                  'resource_description': row[9]
                  }
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

    def getMedicalDevicesById(self, medicalDevices_id):
        dao = MedicalDevicesDAO()
        row = dao.getMedicalDevicesById(medicalDevices_id)
        if not row:
            return jsonify(Error="Medical Device not found"), 404
        else:
            medDevice = self.build_medicalDevices_dict(row)
            return medDevice

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
        return jsonify(medicalDevices=item), 200

    def delete(self, item):
        return jsonify(medicalDevices=item), 200

    def update(self, item):
        return jsonify(medicalDevices=item), 200
