from flask import jsonify
from dao.powerGenerator import PowerGeneratorDAO


# power generator attributes: powerGenerator_id, resource_id, powerGenerator_type

class PowerGeneratorHandler:
    def build_femenine_hygiene_dict(self, row):
        result = {'powerGenerator_id': row[0],
                  'resource_id': row[1],
                  'powerGenerator_type': row[2]}
        return result

    def build_femenine_hygiene_attributes(self, powerGenerator_id, resource_id, powerGenerator_type):
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

    def getPowerGeneratorById(self, id):
        return self.getAllPowerGenerator()

    def insert(self, item):
        return jsonify(powerGenerator=item), 200

    def delete(self, item):
        return jsonify(powerGenerator=item), 200

    def update(self, item):
        return jsonify(powerGenerator=item), 200
