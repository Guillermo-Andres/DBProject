from flask import jsonify
from dao.order import OrderDAO


# order attributes: order_id, order_amount, order_date, order_status

class OrderHandler:

    def build_order_dict(self, row):
        result = {'order_id': row[0],
                  'order_amount': row[1],
                  'order_date': row[2],
                  'order_status': row[3]}
        return result

    def build_order_attributes(self, order_id, order_amount, order_date, order_status):
        result = {'order_id': order_id,
                  'order_amount': order_amount,
                  'order_date': order_date,
                  'order_status': order_status}
        return result

    def getAllOrders(self):
        dao = OrderDAO()
        order_list = dao.getAllOrders()
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def getOrderById(self, id):
        return self.getAllOrders()

    def getOrderByAmount(self, amount):
        return self.getAllOrders()

    def getOrderByDate(self, date):
        return self.getAllOrders()

    def getOrderByStatus(self, status):
        return self.getAllOrders()

    def insert(self, item):
        return jsonify(Order=item), 200

    def delete(self, item):
        return jsonify(Order=item), 200

    def update(self, item):
        return jsonify(Order=item), 200
