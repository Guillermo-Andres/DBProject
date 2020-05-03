from flask import jsonify
from dao.hygiene import HygieneDAO


# hygiene attributes: hygiene_id, resource_id, hygiene_description, hygiene_quantityPerUnit, hygiene_brand

class HygieneHandler:
    def build_hygiene_dict(self, row):
        result = {'hygiene_id': row[0], 'resource_id': row[1], 'hygiene_description': row[2],
                  'hygiene_quantityPerUnit': row[3], 'hygiene_brand': row[4]}
        return result

    def build_hygiene_attributes(self, hygiene_id, resource_id, hygiene_description, hygiene_quantityPerUnit,
                                 hygiene_brand):
        result = {'hygiene_id': hygiene_id, 'resource_id': resource_id, 'hygiene_description': hygiene_description,
                  'hygiene_quantityPerUnit': hygiene_quantityPerUnit, 'hygiene_brand': hygiene_brand}
        return result

    def getAllHygiene(self):
        dao = HygieneDAO()
        resource_list = dao.getAllHygiene()
        result_list = []
        for row in resource_list:
            result = self.build_hygiene_dict(row)
            result_list.append(result)
        return jsonify(Hygiene=result_list)

    def getHygieneById(self, hygiene_id):
        dao = HygieneHandler()
        row = dao.getHygieneById(hygiene_id)
        if not row:
            return jsonify(Error='Hygiene not found'), 404
        else:
            hygiene = self. build_hygiene_dict(row)
            return jsonify(Hygiene=hygiene)

    def getHygieneByExpirationDate(self, expiration_date):
        return self.getAllHygiene()

    def getHygieneByPrice(self, price):
        return self.getAllHygiene()

    def getHygieneByLocation(self, location):
        return self.getAllHygiene()

    def getHygieneByUnits(self, units):
        return self.getAllHygiene()

    def getHygieneByDescription(self, description):
        return self.getAllHygiene()

    def getHygieneByQuantityPerUnit(self, quantity_per_unit):
        return self.getAllHygiene()

    def getHygieneByBrand(self, brand):
        return self.getAllHygiene()

    def insert(self, item):
        return jsonify(Hygiene=item), 200

    def delete(self, item):
        return jsonify(Hygiene=item), 200

    def update(self, item):
        return jsonify(Hygiene=item), 200
