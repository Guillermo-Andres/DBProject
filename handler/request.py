from flask import jsonify
from dao.request import RequestDAO


# request attributes: request_id, request_price, request_location, request_quantity

# TODO - add Request to ER and define relationships

class RequestHandler:
    def build_request_dict(self, row):
        result = {'request_id': row[0],
                  'resource_id': row[1],
                  'request_date': row[2]}
        return result

    def build_request_attributes(self, request_id, request_price, request_location, request_quantity):
        result = {'request_id': request_id,
                  'request_price': request_price,
                  'request_location': request_location,
                  'request_quantity': request_quantity}
        return result

    def getAllRequests(self):
        dao = RequestDAO()
        requests_list = dao.getAllRequest()
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(requests=result_list)

    def getRequestById(self, request_id):
        dao = RequestDAO()
        row = dao.getRequestById(request_id)
        if not row:
            return jsonify(Error="Request not found"), 404
        else:
            request = self.build_request_dict(row)
            return request

    def insert(self, item):
        return jsonify(request=item), 200

    def delete(self, item):
        return jsonify(request=item), 200

    def update(self, item):
        return jsonify(request=item), 200
