from flask import jsonify
from dao.supplier import SupplierDAO


# supplier attributes: supplier_id, person_id

class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {'supplier_id': row[0],
                  'person_id': row[1]}
        return result

    def build_supplier_attributes(self, supplier_id, person_id):
        result = {'supplier_id': supplier_id, 'person_id' : person_id}
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, id):
        return self.getAllSuppliers()

    def getSupplierByName(self, first_name, last_name):
        return self.getAllSuppliers()

    def getSupplierByDOB(self, dob):
        return self.getAllSuppliers()

    def getSupplierByAddress(self, address):
        return self.getAllSuppliers()

    def getSupplierByPhone(self, phone):
        return self.getAllSuppliers()

    def getSupplierByEmail(self, email):
        return self.getAllSuppliers()

    def insert(self, item):
        return jsonify(Supplier=item), 200

    def delete(self, item):
        return jsonify(Supplier=item), 200

    def update(self, item):
        return jsonify(Supplier=item), 200
