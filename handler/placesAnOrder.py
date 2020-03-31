from flask import jsonify
from dao.placesAnOrder import PlacesDAO

class PlacesAnOrderHandler:

    def build_placesAnOrder_dict(self , row):
        result = {}

        result['pid'] = row[0]
        result['cid'] = row[1]
        result['oid'] = row[2]

        return result

    def getAllPlacesAnOrder(self):
        dao = PlacesDAO()
        pao = []
        items = dao.getAllPlaces()

        for i in items:
            result = self.build_placesAnOrder_dict(i)
            pao.append(result)
        
        return jsonify(PlacesAnOrder = pao)

    def getPlacesAnOrderByID(self , id):
        dao = PlacesDAO()
        pao = []
        items = dao.getPlacesByID(id)

        for i in items:
            result = self.build_placesAnOrder_dict(i)
            pao.append(result)
        
        return jsonify(PlacesAnOrder = pao)


    def getPlacesAnOrderByConsumerID(self , id):
        dao = PlacesDAO()
        pao = []
        items = dao.getPlacesByID(id)

        for i in items:
            result = self.build_placesAnOrder_dict(i)
            pao.append(result)
        
        return jsonify(PlacesAnOrder = pao)

    def getPlacesAnOrderByOrderID(self , id):
        dao = PlacesDAO()
        pao = []
        items = dao.getPlacesByID(id)

        for i in items:
            result = self.build_placesAnOrder_dict(i)
            pao.append(result)
        
        return jsonify(PlacesAnOrder = pao)



    # def insert(self , placesAnOrder_list:
    #     placesAnOrder_dict = build_placesAnOrder_dict(placesAnOrder_list)
    #     dao = PlacesDAO()
    #     return dao.insert([placesAnOrder_dict['pid'] , placesAnOrder_dict['cid'] , placesAnOrder_dict['oid']])

    def insert(self , item):
        return 1
    def delete(self , id):
        return 1
    def update(self , item):
        return 1