from flask import jsonify
from dao.hygiene import HygieneDAO

# hygiene attributes: hygiene_id, hygiene_expiration_date, hygiene_price, hygiene_location, hygiene_units, hygiene_description, hygiene_quantity_per_unit, hygiene_brand

class HygieneHandler:
    def build_hygiene_dict(self, row):
        result = {}
        result['hygiene_id'] = row[0]
        result['hygiene_expiration_date'] = row[1]
        result['hygiene_price'] = row[2]
        result['hygiene_location'] = row[3]
        result['hygiene_units'] = row[4]
        result['hygiene_description'] = row[5]
        result['hygiene_quantity_per_unit'] = row[6]
        result['hygiene_brand'] = row[7]
        return result

    def build_hygiene_attributes(self, hygiene_id, hygiene_expiration_date, hygiene_price, hygiene_location, hygiene_units, hygiene_description, hygiene_quantity_per_unit, hygiene_brand):
        result = {}
        result['hygiene_id'] = hygiene_id
        result['hygiene_expiration_date'] = hygiene_expiration_date
        result['hygiene_price'] = hygiene_price
        result['hygiene_location'] = hygiene_location
        result['hygiene_units'] = hygiene_units
        result['hygiene_description'] = hygiene_description
        result['hygiene_quantity_per_unit'] = hygiene_quantity_per_unit
        result['hygiene_brand'] = hygiene_brand
        return result

    def getAllHygiene(self):
        dao = HygieneDAO()
        resource_list = dao.getAllHygiene()
        result_list = []
        for row in resource_list:
            result = self.build_hygiene_dict(row)
            result_list.append(result)
        return jsonify(Hygiene=result_list)

    def getHygieneById(self, id):
        return self.getAllHygiene()

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

    def insert(self):
        return self.getAllHygiene()

    def delete(self):
        return self.getAllHygiene()

    def update(self):
        return self.getAllHygiene()