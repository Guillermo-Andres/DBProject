from flask import jsonify
from dao.heavyequipment import HeavyEquipmentDAO
#HeavyEquipment ATTTRIBUTES heavy_id, description


class HeavyEquipmentHandler:
    def build_heavyE_dict(self, row):
        result = {}
        result['heavy_id'] = row[0]
        result['description'] = row[1]

        return result

    def build_part_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pmaterial'] = row[2]
        result['pcolor'] = row[3]
        result['pprice'] = row[4]
        result['quantity'] = row[5]
        return result

    def getAllHeavyEquipment(self):

        dao = HeavyEquipmentDAO()
        HE_list = dao.getAllHeavyEquipment()
        result_list = []
        for row in HE_list:
            result = self.build_heavyE_dict(row)
            result_list.append(result)
        return jsonify(Heavy_Equipment=result_list)

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
