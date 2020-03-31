from flask import jsonify
from dao.order import OrderDAO

# order attributes: order_id, order_amount, order_date, order_status

class OrderHandler:
    def build_order_dict(self, row):
        result = {}
        result['order_id'] = row[0]
        result['order_amount'] = row[1]
        result['order_date'] = row[2]
        result['order_status'] = row[3]
        return result

    def build_order_attributes(self, order_id, order_amount, order_date, order_status):
        result = {}
        result['order_id'] = order_id
        result['order_amount'] = order_amount
        result['order_date'] = order_date
        result['order_status'] = order_status
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

    def insert(self,item):
        return jsonify(Order= item) ,200

    def delete(self,item):
        return jsonify(Order= item) ,200


    def update(self,item):
        return jsonify(Order= item) ,200
