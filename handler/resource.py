from flask import jsonify
from dao.resource import ResourceDAO


# resource attributes: resource_id, resource_price, resource_location, resource_quantity

class ResourceHandler:
    def build_resource_dict(self, row):
        result = {'resource_id': row[0],
                  'resource_name': row[1],
                  'resource_price': row[2],
                  'resource_location': row[3],
                  'resource_quantity': row[4],
                  'available': row[5]}
        return result

    def build_resource_attributes(self, resource_id, resource_price, resource_location, resource_quantity):
        result = {'resource_id': resource_id,
                  'resource_price': resource_price,
                  'resource_location': resource_location,
                  'resource_quantity': resource_quantity}
        return result

    def getAllResources(self):
        dao = ResourceDAO()
        resources_list = dao.getAllResource()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, resource_id):
        dao = ResourceDAO()
        row = dao.getResourceById(resource_id)
        if not row:
            return jsonify(Error='Resource not found'), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    def getResourcesInStock(self):
        dao = ResourceDAO()
        resources_list = dao.getResourcesInStock()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllResourceByKeyword(self , keyword):
        dao = ResourceDAO()
        Resources_list = dao.getResourceByKeyWord(keyword)
        result_list = []
        for row in Resources_list:
            result = self.build_Resource_and_resource_and_consumer_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def insert(self, item):
        return jsonify(Resource=item), 200

    def delete(self, item):
        return jsonify(Resource=item), 200

    def update(self, item):
        return jsonify(Resource=item), 200
