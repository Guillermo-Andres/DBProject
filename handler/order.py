from flask import jsonify
from dao.order import OrderDAO


# order attributes: order_id, order_amount, order_date, order_status

class OrderHandler:

    def build_order_dict(self, row):
        result = {'order_id': row[0],
                  'paymentmethod_id': row[1],
                  'consumer_id': row[2],
                  'request_id': row[3],
                  'resource_id': row[4],
                  'supplier_id': row[5],
                  'order_amount': row[6],
                  'order_date': row[7],
                  'order_status': row[8],
                  'resource_name': row[9],
                  'resource_price': row[10],
                  'resource_city': row[11],
                  'resource_quantity': row[12],
                  'resource_description': row[13],
                  'resource_date': row[14],
                  'resource_keyword': row[15],
                  'request_date':row[16],
                  'consumer_severity': row[17],
                  'paymentmethod_type': row[18]
                  }
        return result

    def build_order_attributes(self, order_id, order_amount, order_date, order_status):
        result = {'order_id': order_id,
                  'order_amount': order_amount,
                  'order_date': order_date,
                  'order_status': order_status}
        return result

    def build_order_stats_per_date_dict(self, row):
        result = {
            'resource_name': row[0],
            'number_of_matches': row[1],
            'order_date': row[2]
        }
        return result

    def build_reqs_stats_per_region_dict(self, row):
        result = {
            'resource_name': row[0],
            'number_of_requests': row[1],
            'region': row[2]
        }
        return result

    def getAllOrders(self):
        dao = OrderDAO()
        order_list = dao.getAllOrders()
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def getOrdersByConsumerID(self, consumer_id):
        dao = OrderDAO()
        order_list = dao.getOrderByConsumerId(consumer_id)
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def getOrderStatsPerRegion(self):
        dao = OrderDAO()
        order_list = dao.getOrderStatsPerRegion()
        result_list = []
        for row in order_list:
            result = self.build_reqs_stats_per_region_dict(row)
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

    def getOrderStatsPerDay(self):
        dao = OrderDAO()
        order_list = dao.getOrderStatsPerDay()
        result_list = []
        for row in order_list:
            result = self.build_order_stats_per_date_dict(row)
            result_list.append(result)
        return jsonify(order=result_list)

    def getOrderStatsPerWeek(self):
        dao = OrderDAO()
        order_list = dao.getOrderStatsPerWeek()
        result_list = []
        for row in order_list:
            result = self.build_order_stats_per_date_dict(row)
            result_list.append(result)
        return jsonify(order=result_list)
