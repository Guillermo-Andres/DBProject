from config.dbconfig import pg_config
import psycopg2




# Attr:
#     placesID
#     consumerID
#     orderId


class PlacesDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPlaces(self):
        cursor = self.conn.cursor()
        query = "select * from places_An_Order;"
        cursor.execute(query)
        result = []

        for row in cursor:
            result.append(row)
        return result

    def getPlacesByID(self , places_an_order_id):

        cursor = self.conn.cursor()
        query = "select * from supplies where places_an_order_id = %s;"
        cursor.execute(query , (places_an_order_id))
        result = []
        result.append(row)

        for row in cursor:
            result.append(row)
        return result

    def insert(self , item):
        return 1
    def delete(self , id):
        return 1
    def update(self , item):
        return 1