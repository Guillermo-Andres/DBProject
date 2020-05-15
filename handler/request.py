from flask import jsonify
from dao.request import RequestDAO


# request attributes: request_id, request_price, request_location, request_quantity

# TODO - add Request to ER and define relationships

class RequestHandler:
    def build_request_dict(self, row):
        result = {'request_id': row[0],
                  'resource_keyword': row[1],
                  'request_date': row[2]}
        return result

    def build_request_and_resource_and_consumer_makesRequest_dict(self, row):
        result = {'request_id': row[0],
                  'request_date': row[3],
                  'resource_id': row[2],
                  'resource_name': row[4],
                  'resource_price': row[5],
                  'resource_location': row[6],
                  'resource_quantity': row[7],
                  'resource_description': row[8],
                  'consumer_id': row[1],
                  'person_id': row[9],
                  'consumer_severety': row[10]
                  }
        return result
    
    def build_reqs_makes_consumer_dict(self , row):
        result = {
            'request_id': row[0],
            'consumer_id':row[1],
            'Searching for: ' : row[2],
            'Made on Date: ':row[3],
            'consumer_severety':row[5]
        }
        return result

    def build_reqs_stats_per_date_dict(self, row):
        result = {
            'resource_name': row[0],
            'number_of_requests': row[1],
            'request_date': row[2]
        }
        return result

    def build_reqs_stats_per_region_dict(self, row):
        result = {
            'resource_name': row[0],
            'number_of_requests': row[1],
            'region': row[2]
        }
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
            result = self.build_reqs_makes_consumer_dict(row)
            result_list.append(result)
        return jsonify(requests=result_list)

    def getAllRequestByKeyword(self, keyword):
        dao = RequestDAO()
        requests_list = dao.getRequestByKeyWord(keyword)
        result_list = []
        for row in requests_list:
            result = self.build_reqs_makes_consumer_dict(row)
            result_list.append(result)
        return jsonify(requests=result_list)

    def getRequestById(self, request_id):
        dao = RequestDAO()
        row = dao.getRequestById(request_id)
        if not row:
            return jsonify(Error="Request not found"), 404
        else:
            request = self.build_reqs_makes_consumer_dict(row)
            return request

    def getRequestStatsPerDay(self):
        dao = RequestDAO()
        request_list = dao.getRequestStatsPerDay()
        result_list = []
        for row in request_list:
            result = self.build_reqs_stats_per_date_dict(row)
            result_list.append(result)
        return jsonify(request=result_list)

    def getRequestStatsPerWeek(self):
        dao = RequestDAO()
        request_list = dao.getRequestStatsPerWeek()
        result_list = []
        for row in request_list:
            result = self.build_reqs_stats_per_date_dict(row)
            result_list.append(result)
        return jsonify(request=result_list)

    def getRequestStatsPerRegion(self):
        dao = RequestDAO()
        request_list = dao.getRequestStatsPerRegion()
        result_list = []
        for row in request_list:
            result = self.build_reqs_stats_per_region_dict(row)
            result_list.append(result)
        return jsonify(request=result_list)

    def insert(self, resource_keyword , resource_type , consumer_id):
        request_dao =  RequestDAO()
        return request_dao.insert(resource_keyword , resource_type, consumer_id)

    def delete(self, item):
        return jsonify(request=item), 200

    def update(self, item):
        return jsonify(request=item), 200