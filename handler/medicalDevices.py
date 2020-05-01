from flask import jsonify
from dao.medicalDevices import MedicalDevicesDAO

# diapers attributes: diaper_id, diaper_price, diaper_location, diaper_quantity, diaper_size, diaper_material, diaper_brand

class DiapersHandler:
    def build_diapers_dict(self, row):
        result = {}
        result['diaper_id'] = row[0]
        result['diaper_price'] = row[1]
        result['diaper_location'] = row[2]
        result['diaper_quantity'] = row[3]
        result['diaper_size'] = row[4]
        result['diaper_material'] = row[5]
        result['diaper_brand'] = row[6]
        return result

    def build_resorce_attributes(self, diaper_id, diaper_price, diaper_location, diaper_quantity, diaper_size, diaper_material, diaper_brand):
        result = {}
        result['diaper_id'] = diaper_id
        result['diaper_price'] = diaper_price
        result['diaper_location'] = diaper_location
        result['diaper_quantity'] = diaper_quantity
        result['diaper_size'] = diaper_size
        result['diaper_material'] = diaper_material
        result['diaper_brand'] = diaper_brand
        return result

    def getAllDiapers(self):
        dao = DiapersDAO()
        resource_list = dao.getAllDiapers()
        result_list = []
        for row in resource_list:
            result = self.build_diapers_dict(row)
            result_list.append(result)
        return jsonify(Diapers=result_list)

    def getDiapersById(self, id):
        return self.getAllDiapers()

    def getDiapersByPrice(self, price):
        return self.getAllDiapers()

    def getDiapersByLocation(self, location):
        return self.getAllDiapers()

    def getDiapersByQuantity(self, quantity):
        return self.getAllDiapers()

    def getDiapersBySize(self, size):
        return self.getAllDiapers()

    def getDiapersByMaterial(self, material):
        return self.getAllDiapers()

    def getDiapersByBrand(self, brand):
        return self.getAllDiapers()

    def insert(self, item):
        return jsonify(Diapers= item) ,200

    def delete(self,item):
        return jsonify(Diapers= item) ,200


    def update(self,item):
        return jsonify(Diapers= item) ,200
