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

    # def getSupplierById(self, sid):
    #
    #     dao = SupplierDAO()
    #
    #     row = dao.getSupplierById(sid)
    #     if not row:
    #         return jsonify(Error="Supplier Not Found"), 404
    #     else:
    #         part = self.build_supplier_dict(row)
    #     return jsonify(Part=part)
    #
    # def getPartsBySupplierId(self, sid):
    #     dao = SupplierDAO()
    #     if not dao.getSupplierById(sid):
    #         return jsonify(Error="Supplier Not Found"), 404
    #     parts_list = dao.getPartsBySupplierId(sid)
    #     result_list = []
    #     for row in parts_list:
    #         result = self.build_part_dict(row)
    #         result_list.append(result)
    #     return jsonify(PartsSupply=result_list)
    #
    # def searchSuppliers(self, args):
    #     if len(args) > 1:
    #         return jsonify(Error = "Malformed search string."), 400
    #     else:
    #         city = args.get("city")
    #         if city:
    #             dao = SupplierDAO()
    #             supplier_list = dao.getSuppliersByCity(city)
    #             result_list = []
    #             for row in supplier_list:
    #                 result = self.build_supplier_dict(row)
    #                 result_list.append(row)
    #             return jsonify(Suppliers=result_list)
    #         else:
    #             return jsonify(Error="Malformed search string."), 400
    #
    # def insertSupplier(self, form):
    #     if form and len(form) == 3:
    #         sname = form['sname']
    #         scity = form['scity']
    #         sphone = form['sphone']
    #         if sname and scity and sphone:
    #             dao = SupplierDAO()
    #             sid = dao.insert(sname, scity, sphone)
    #             result = {}
    #             result["sid"] = sid
    #             result["sname"] = sname
    #             result["scity"] = scity
    #             result["sphone"] = sphone
    #             return jsonify(Supplier=result), 201
    #         else:
    #             return jsonify(Error="Malformed post request")
    #     else:
    #         return jsonify(Error="Malformed post request")

