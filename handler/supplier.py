from flask import jsonify
from dao.supplier import SupplierDAO


# supplier attributes: supplier_id, person_id

class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {'person_id': row[0],
                  'supplier_id': row[1],
                  'person_firstname': row[2],
                  'person_lastname': row[3],
                  'person_dob': row[4],
                  'person_city': row[5],
                  'person_phone_number': row[6],
                  'person_email': row[7]}
        return result

    def build_attribute_dict(self,pfname,plname,pdob,pcity,pphone,pemail):
        result = {}

        result['person_firstname'] = pfname
        result['person_lastname'] = plname
        result['person_dob'] = pdob
        result['person_city'] = pcity
        result['person_phone'] = pphone
        result['person_email'] = pemail
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, supplier_id):
        dao = SupplierDAO()
        row = dao.getSupplierById(supplier_id)
        if not row:
            return jsonify(Error="Supplier not Found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier=supplier)


        return self.getAllSuppliers()

    def insert(self, item):

        pfname = item['person_firstname']
        plname = item['person_lastname']
        pdob = item['person_dob']
        pcity = item['person_city']
        pphone = item['person_phone_number']
        pemail = item['person_email']

        if pfname and plname and pdob and pcity and pphone and pemail :
            dao = SupplierDAO()
            dao.insert(pfname,plname,pdob,pcity,pphone,pemail)
            return jsonify(supplier=self.build_attribute_dict(pfname,plname,pdob,pcity,pphone,pemail)), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
