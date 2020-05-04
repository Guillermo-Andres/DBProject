from flask import jsonify
from dao.powerGenerator import PowerGeneratorDAO


# power generator attributes: powerGenerator_id, resource_id, powerGenerator_type

class PowerGeneratorHandler:
    def build_powerGenerator_dict(self, row):
        result = {'resource_id': row[0],
                  'powerGenerator_id': row[1],
                  'powerGenerator_type': row[2],
                  'resource_name': row[3],
                  'resource_price': row[4],
                  'resource_location': row[5],
                  'resource_quantity': row[6],
                  'available': row[7]
                  }
        return result

    def build_powerGenerator_attributes(self, powerGenerator_id, resource_id, powerGenerator_type):
        result = {'powerGenerator_id': powerGenerator_id,
                  'resource_id': resource_id,
                  'powerGenerator_type': powerGenerator_type}
        return result

    def getAllPowerGenerator(self):
        dao = PowerGeneratorDAO()
        resource_list = dao.getAllPowerGenerator()
        result_list = []
        for row in resource_list:
            result = self.build_femenine_hygiene_dict(row)
            result_list.append(result)
        return jsonify(powerGenerator=result_list)

    def getPowerGeneratorById(self, powerGenerator_id):
        dao = PowerGeneratorDAO()
        row = dao.getPowerGeneratorsById(powerGenerator_id)
        if not row:
            return jsonify(Error='Power Generator not found'), 404
        else:
            powerGen = self.build_powerGenerator_dict(row)
            return powerGen

    def insert(self, item):
        return jsonify(powerGenerator=item), 200

    def delete(self, item):
        return jsonify(powerGenerator=item), 200

    def update(self, item):
        return jsonify(powerGenerator=item), 200
