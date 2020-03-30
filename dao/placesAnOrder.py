from config.dbconfig import pg_config
import psycopg2

# Attr:
#     placesID
#     consumerID
#     orderId


class PlacesDAO:

    def getAllPlaces(self):
        return [[0 ,0 , 0] , [1 ,0 , 1]]

    def getPlacesByID(self , pid):

        for placed in self.getAllPlaces():
            if(placed[0] == pid):
                return placed
        return None