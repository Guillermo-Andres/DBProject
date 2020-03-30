from flask import jsonify
from dao.femenine_hygiene import FemenineHygieneDAO

# femenine hygiene attributes: fh_id, fh_price, rh_location, rh_quantity, fh_type (pads, liners, tampons, cup), fh_flow (light, medium, heavy), fh_brand, fh_quantity_per_unit

class FemenineHygieneHandler:
    def build_femenine_hygiene_dict(self, row):
        result = {}
        result['fh_id'] = row[0]
        result['fh_price'] = row[1]
        result['fh_location'] = row[2]
        result['fh_quantity'] = row[3]
        result['fh_type'] = row[4]
        result['fh_flow'] = row[5]
        result['fh_brand'] = row[6]
        result['fh_quantity_per_unit'] = row[7]
        return result

    def build_femenine_hygiene_attributes(self, fh_id, fh_price, fh_location, fh_quantity, fh_type, fh_flow, fh_brand, fh_quantity_per_unit):
        result = {}
        result['fh_id'] = fh_id
        result['fh_price'] = fh_price
        result['fh_location'] = fh_location
        result['fh_quantity'] = fh_quantity
        result['fh_type'] = fh_type
        result['fh_flow'] = fh_flow
        result['fh_brand'] = fh_brand
        result['fh_quantity_per_unit'] = fh_quantity_per_unit
        return result

    def getAllFemenineHygiene(self):
        dao = FemenineHygieneDAO()
        resource_list = dao.getAllFemenineHygiene()
        result_list = []
        for row in resource_list:
            result = self.build_femenine_hygiene_dict(row)
            result_list.append(result)
        return jsonify(FemenineHygiene=result_list)
