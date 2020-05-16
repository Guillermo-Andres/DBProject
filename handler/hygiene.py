from flask import jsonify
from dao.hygiene import HygieneDAO


# hygiene attributes: hygiene_id, resource_id, hygiene_description, hygiene_quantityPerUnit, hygiene_brand

class HygieneHandler:
    def build_hygiene_dict(self, row):
        result = {'resource_id': row[0],
                  'hygiene_id': row[1],
                  'hygiene_quantityPerUnit': row[2],
                  'hygiene_brand': row[3],
                  'resource_name': row[4],
                  'resource_price': row[5],
                  'resource_location': row[6],
                  'resource_quantity': row[7],
                  'resource_description': row[8]
                  }
        return result

    def build_hygiene_attributes(self, hygiene_quantityPerUnit, hygiene_brand, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date):
        result = {
            'hygiene_quantityPerUnit': hygiene_quantityPerUnit,
            'hygiene_brand': hygiene_brand,
            'resource_name': resource_name,
            'resource_price': resource_price,
            'resource_city': resource_city,
            'resource_quantity': resource_quantity,
            'resource_description': resource_description,
            'resource_date': resource_date
        }
        return result

    def getAllResourceByKeyword(self , keyword):
        dao = HygieneDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_hygiene_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllHygiene(self):
        dao = HygieneDAO()
        resource_list = dao.getAllHygiene()
        result_list = []
        for row in resource_list:
            result = self.build_hygiene_dict(row)
            result_list.append(result)
        return jsonify(Hygiene=result_list)

    def getHygieneById(self, hygiene_id):
        dao = HygieneDAO()
        row = dao.getHygieneById(hygiene_id)
        if not row:
            return jsonify(Error='Hygiene not found'), 404
        else:
            hygiene = self.build_hygiene_dict(row)
            return jsonify(Hygiene=hygiene)


    def insert(self, item,supplier_id):
        hygiene_quantityPerUnit = item['hygiene_quantityPerUnit']
        hygiene_brand = item['hygiene_brand']
        resource_name = item['resource_name']
        resource_price = item['resource_price']
        resource_city = item['resource_city']
        resource_quantity = item['resource_quantity']
        resource_description = item['resource_description']
        resource_date = item['resource_date']
        if hygiene_quantityPerUnit and hygiene_brand and resource_name and resource_price and resource_city and resource_quantity and resource_description and resource_date:
            dao = HygieneDAO()
            rid = dao.insert(hygiene_quantityPerUnit, hygiene_brand, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date,supplier_id)
            return jsonify(Hygiene=self.build_hygiene_attributes(hygiene_quantityPerUnit, hygiene_brand, resource_name, resource_price, resource_city, resource_quantity, resource_description, resource_date))
        else:
            return jsonify(Error="Unexpected attributes in POST request"), 400

    def delete(self, item):
        return jsonify(Hygiene=item), 200

    def update(self, item):
        return jsonify(Hygiene=item), 200
