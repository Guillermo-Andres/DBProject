from flask import jsonify
from dao.supplier import SupplierDAO

# supplier attributes: supplier_id supplier_first_name, supplier_last_name, supplier_dob, supplier_address, supplier_phone_number, supplier_email_address

class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['supplier_id'] = row[0]
        result['supplier_first_name'] = row[1]
        result['supplier_last_name'] = row[2]
        result['supplier_dob'] = row[3]
        result['supplier_address'] = row[4]
        result['supplier_phone_number'] = row[5]
        result['supplier_email_address'] = row[6]
        return result

    def build_supplier_attributes(self, supplier_id, supplier_first_name, supplier_last_name, supplier_dob, supplier_address, supplier_phone_number, supplier_email_address):
        result = {}
        result['supplier_id'] = supplier_id
        result['supplier_first_name'] = supplier_first_name
        result['supplier_last_name'] = supplier_last_name
        result['supplier_dob'] = supplier_dob
        result['supplier_address'] = supplier_address
        result['supplier_phone_number'] = supplier_phone_number
        result['supplier_email_address'] = supplier_email_address
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

    def insert(self,item):
        return jsonify(Supplier= item) ,200

    def delete(self,item):
        return jsonify(Supplier= item) ,200


    def update(self,item):
        return jsonify(Supplier= item) ,200
