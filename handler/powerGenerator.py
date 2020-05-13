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
                  'resource_description': row[7],
                  'resource_date': row[8]
                  }
        return result

    def build_powerGenerator_attributes(self, powerGenerator_type):
        result = {   'powerGenerator_type': powerGenerator_type   }
        return result



    def getAllResourceByKeyword(self , keyword):
        dao = PowerGeneratorDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_powerGenerator_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllPowerGenerator(self):
        dao = PowerGeneratorDAO()
        resource_list = dao.getAllPowerGenerators()
        result_list = []
        for row in resource_list:
            result = self.build_powerGenerator_dict(row)
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
        ptype = item['powerGenerator_type']
        rname = item['resource_name']
        rprice = item['resource_price']
        resource_location = item['resource_location']
        resource_quantity = item['resource_quantity']
        resource_date = item['resource_date']
        resource_description = item['resource_description']
        if ptype and rname and rprice and resource_location and resource_quantity and resource_date and resource_description:
            dao = PowerGeneratorDAO()
            rid = dao.insert(rname, rprice,resource_location,resource_quantity,resource_description,resource_date,ptype)
            return jsonify(PowerGenerator=self.build_powerGenerator_attributes(ptype)), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
