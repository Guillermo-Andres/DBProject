from flask import jsonify
from dao.medicalDevices import MedicalDevicesDAO


# medicalDevices attributes: medicalDevices_id, resource_id, medicalDevices_type, medicalDevices_description

class MedicalDevicesHandler:
    def build_medicalDevices_dict(self, row):
        result = {'resource_id': row[0],
                  'medicalDevices_id': row[1],
                  'medicalDevices_type': row[2],
                  'resource_name': row[3],
                  'resource_price': row[4],
                  'resource_location': row[5],
                  'resource_quantity': row[6],
                  'resource_description': row[7]
                  }
        return result

    def build_resorce_attributes(self, medicalDevices_id, resource_id, medicalDevices_type, medicalDevices_description):
        result = {'medicalDevices_id': medicalDevices_id,
                  'resource_id': resource_id,
                  'medicalDevices_type': medicalDevices_type,
                  'medicalDevices_description': medicalDevices_description}
        return result

    def build_medicalDevices_attrs(self, medicalDevices_type, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date):
        result = {
            'medicalDevices_type': medicalDevices_type,
            'resource_name': resource_name,
            'resource_price': resource_price,
            'resource_city': resource_city,
            'resource_quantity': resource_quantity,
            'resource_description': resource_description,
            'resource_date': resource_date
        }
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



    def getAllResourceByKeyword(self , keyword):
        dao = MedicalDevicesDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_medicalDevices_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)


    def insert(self, item,supplier_id):
        medicalDevices_type = item['medicalDevices_type']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if medicalDevices_type and resource_name and resource_price and resource_city and resource_quantity and resource_description and resource_date:
            dao = MedicalDevicesDAO()
            rid = dao.insert(medicalDevices_type, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date,supplier_id)
            return jsonify(medicalDevices=self.build_medicalDevices_attrs(medicalDevices_type, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date))
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400

    def delete(self, item):
        return jsonify(medicalDevices=item), 200

    def update(self, item):
        return jsonify(medicalDevices=item), 200
