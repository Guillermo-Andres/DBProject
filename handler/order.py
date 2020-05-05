from flask import jsonify
from dao.order import OrderDAO


# order attributes: order_id, order_amount, order_date, order_status

class OrderHandler:

    def build_order_dict(self, row):
        result = {'order_id': row[0],
                  'supplier_id' :row[1],
                  'order_amount': row[2],
                  'order_date': row[3],
                  'order_status': row[4],
                  'request_id': row[5],
                  'resource_id': row[6],
                  'request_date': row[7],
                  'person_id' : row[8],
                  'paymentmethod_id':row[9]
                  }
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

    def geOrdersByConsumerID(self , consumer_id):
        dao = OrderDAO()
        order_list = dao.getOrderByConsumerId(consumer_id)
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def getOrderById(self, order_id):
        dao = OrderDAO()
        row = dao.getOrderById(order_id)
        if not row:
            return jsonify(Error="Order not found"), 404
        else:
            order = self.build_order_dict(row)
            return jsonify(Order=order)

    
    def getReserved(self):
        dao = OrderDAO()
        order_list = dao.getReserved()
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def getPurchased(self):
        dao = OrderDAO()
        order_list = dao.getPurchased()
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)



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
