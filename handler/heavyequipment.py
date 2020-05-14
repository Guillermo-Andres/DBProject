from flask import jsonify
from dao.heavyequipment import HeavyEquipmentDAO
#HeavyEquipment ATTTRIBUTES heavy_id, description


class HeavyEquipmentHandler:
    def build_heavyE_dict(self, row):
        result = {'resource_id': row[0], 'heavy_id': row[1], 'type': row[2], 'name': row[3], 'price': row[4],
                  'location': row[5], 'quantity': row[6], 'description': row[7]}
        return result

    def build_heavyEquipment_attrs(self, heavyEquipment_type, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date):
        result = {
            'heavyEquipment_type': heavyEquipment_type,
            'resource_name': resource_name,
            'resource_price': resource_price,
            'resource_city': resource_city,
            'resource_quantity': resource_quantity,
            'resource_description': resource_description,
            'resource_date': resource_date
        }
        return result

    def getAllResourceByKeyword(self , keyword):
        dao = HeavyEquipmentDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllHeavyEquipment(self):

        dao = HeavyEquipmentDAO()
        HE_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def getHeavyEquimentById(self, id):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getHeavyEquimentById(id)
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)


    def getHeavyEquipmentByPrice(self, price):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getHeavyEquipmentByPrice(price)
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def getHeavyEquipmentByLocation(self, location):
        dao = HeavyEquipmentDAO()
        HE_list = dao.getHeavyEquipmentByLocation(location)
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

    def insert(self, item):
        heavyEquipment_type = item['heavyEquipment_type']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if heavyEquipment_type and resource_name and resource_price and resource_city and resource_quantity and resource_description and resource_date:
            dao = HeavyEquipmentDAO()
            rid = dao.insert(heavyEquipment_type, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date)
            return jsonify(HeavyEquipment=self.build_heavyEquipment_attrs(heavyEquipment_type, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date))
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400


    def update(self,item):
        return jsonify(HeavyEquiment= item) ,200

    def delete(self,item):
        return jsonify(HeavyEquiment= item) ,200
