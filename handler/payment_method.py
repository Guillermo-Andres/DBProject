from flask import jsonify
from dao.payment_method import PaymentMethodDAO

class PaymentMethodHandler:
    def build_payment_method_dict(self, row):
        result = {}
        result['payment_method_id'] = row[0]
        result['payment_method_type'] = row[1]
        return result

    def build_payment_method_attributes(self, payment_method_id, payment_method_type):
        result = {}
        result['payment_method_id'] = payment_method_id
        result['payment_method_type'] = payment_method_type
        return result


    def getAllPaymentMethods(self):
        dao = PaymentMethodDAO()
        payment_method_list = dao.getAllPaymentMethods()
        result_list = []
        for row in payment_method_list:
            result = self.build_payment_method_dict(row)
            result_list.append(result)
        return jsonify(PaymentMethod=result_list)


    def getPaymentMethodById(self, payment_method_id):
        return self.getAllPaymentMethods()

    def getPaymentMethodByType(self, type):
        return self.getAllPaymentMethods()

    def insert(self):
        return self.getAllPaymentMethods()

    def delete(self):
        return self.getAllPaymentMethods()

    def update(self):
        return self.getAllPaymentMethods()

    def insertPaymentMethodJson(self, json):
        payment_method_type = json['type']
        if payment_method_type:
            dao = PaymentMethodDAO()
            payment_method_id = dao.insert()
            result = self.build_payment_method_attributes(payment_method_id, payment_method_type)
            return jsonify(PaymentMethod=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400



