from flask import jsonify
from dao.payment_method import PaymentMethodDAO


class PaymentMethodHandler:

    def build_payment_method_dict(self, row):
        result = {'paymentMethod_id': row[0],
                  'paymentMethod_type': row[1],
                  'consumer_id': row[2]}
        return result

    def build_payment_method_attributes(self, payment_method_id, payment_method_type):
        result = {'payment_method_id': payment_method_id,
                  'payment_method_type': payment_method_type}
        return result

    def getAllPaymentMethods(self):
        dao = PaymentMethodDAO()
        payment_method_list = dao.getAllPaymentMethods()
        result_list = []
        for row in payment_method_list:
            result = self.build_payment_method_dict(row)
            result_list.append(result)
        return jsonify(PaymentMethod=result_list)

    def getPaymentMethodById(self, paymentMethod_id):
        dao = PaymentMethodDAO()
        row = dao.getPaymentMethodById(paymentMethod_id)
        if not row:
            return jsonify(Error="Payment Method not found"), 404
        else:
            paymentMethod = self.build_payment_method_dict(row)
            return paymentMethod

    def getPaymentMethodByType(self, type):
        return self.getAllPaymentMethods()

    def insert(self, item):
        return jsonify(Payment_Method=item), 200

    def delete(self, item):
        return jsonify(Payment_Method=item), 200

    def update(self, item):
        return jsonify(Payment_Method=item), 200

    def insertPaymentMethodJson(self, json):
        payment_method_type = json['type']
        if payment_method_type:
            dao = PaymentMethodDAO()
            payment_method_id = dao.insert()
            result = self.build_payment_method_attributes(payment_method_id, payment_method_type)
            return jsonify(PaymentMethod=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
