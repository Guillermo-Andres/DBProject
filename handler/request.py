from flask import jsonify
from dao.request import RequestDAO


# request attributes: request_id, request_price, request_location, request_quantity

# TODO - add Request to ER and define relationships

class RequestHandler:
    def build_request_dict(self, row):
        result = {'request_id': row[0],
                  'request_id': row[1],
                  'request_price': row[2],
                  'request_location': row[3],
                  'request_quantity': row[4]}
        return result

    def build_request_attributes(self, request_id, request_price, request_location, request_quantity):
        result = {'request_id': request_id,
                  'request_price': request_price,
                  'request_location': request_location,
                  'request_quantity': request_quantity}
        return result

    def getAllRequests(self):
        dao = RequestDAO()
        requests_list = dao.getAllrequest()
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(requests=result_list)

    def insert(self, item):
        return jsonify(request=item), 200

    def delete(self, item):
        return jsonify(request=item), 200

    def update(self, item):
        return jsonify(request=item), 200
