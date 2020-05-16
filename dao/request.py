from config.dbconfig import pg_config
from dao.resource import ResourceDAO
from dao.order import OrderDAO
import psycopg2


class RequestDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequest(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural inner join consumer natural inner join makesRequest; "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, request_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural inner join consumer natural inner join makesRequest " \
                "where request_id = %s;"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def getResourceInRequest(self, request_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request  " \
                "where request_id = %s"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def getRequestByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request  natural inner join consumer natural inner join makesRequest "\
                "where resource_keyword  ~*  %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, resource_keyword , resource_type, consumer_id ):
        cursor = self.conn.cursor()
        query ="insert into request(resource_keyword , request_date) values (%s , CURRENT_DATE ) returning request_id;"
        cursor.execute(query , (resource_keyword ,))
        request  = cursor.fetchone()[0]
        self.conn.commit()

        

        cursor = self.conn.cursor()
        query = "insert into makesRequest(consumer_id , request_id) values (%s , %s); "
        cursor.execute(query , (consumer_id , request))
        self.conn.commit()
        """ check for match """ 
        
        resources = ResourceDAO().getDAO(resource_type).getResourceByKeyWord(resource_keyword)
       
        if(len(resources) > 0 ):
            #found resource for order , create order
            order = OrderDAO().insert(resources[0][0])
           
            cursor = self.conn.cursor()

            #attach paymentmethod
            query =  "select paymentMethod_id from paymentMethod where consumer_id = %s;"
            cursor.execute(query , (consumer_id , ))
            paymentMethod_id =  cursor.fetchone()[0]

            self.conn.commit()
            cursor = self.conn.cursor()
            query = "insert into paysFor(paymentMethod_id , order_id) values (%s ,%s);"
            cursor.execute(query , ( paymentMethod_id , order))
            self.conn.commit()
            
            return (True , order)

        return ( False , request)




    def getRequestByKeyWordForMatch(self , resource_name , resource_description):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request  natural inner join consumer natural inner join makesRequest "\
                "where %s  ~*  resource_name OR % ~* resource_description; "

        
        cursor.execute(query , (resource_name , resource_description))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def checkForMatch(self , resource_name , resource_description , resource_id):

        """find a request for this resource"""

        requested = self.getRequestByKeyWordForMatch( resource_name, resource_description)
    
        if(len(requested) > 0 ):
            
            cursor = self.conn.cursor()
            query = " select consumer_id from request natural inner join makesRequest where request_id = %s;"
            cursor.execute(query , (requested[0][0] , ))
            consumer_id = cursor.fetchone()[0]
            self.conn.commit()

            #found resource for order , create order
            order = OrderDAO().insert(resource_id)
        
            cursor = self.conn.cursor()

            #attach paymentmethod
            query =  "select paymentMethod_id from paymentMethod where consumer_id = %s;"
            cursor.execute(query , (consumer_id , ))
            paymentMethod_id =  cursor.fetchone()[0]

            self.conn.commit()
            cursor = self.conn.cursor()
            query = "insert into paysFor(paymentMethod_id , order_id) values (%s ,%s);"
            cursor.execute(query , ( paymentMethod_id , order))
            self.conn.commit()
                
                
            
            



    def getRequestStatsPerDay(self):
        cursor = self.conn.cursor()
        query = "select resource_keyword, count(resource_keyword) as number_of_requests_per_resource, date_trunc('day', " \
                "request_date) as day from request  group by day, resource_keyword " \
                "order by date_trunc('day', request_date) ; "
        cursor.execute(query)
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return result

    def getRequestStatsPerWeek(self):
        cursor = self.conn.cursor()
        query = "select resource_keyword, count(resource_keyword) as number_of_requests_per_resource, date_trunc('week', " \
                "request_date) as week from request  group by week, resource_keyword " \
                "order by week; "
        cursor.execute(query)
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return result

    def getRequestStatsPerRegion(self):
        cursor = self.conn.cursor()
        query = "select resource_keyword, count(resource_keyword) as request_per_region, get_region(person_city) as region" \
                " from request  natural inner join makesRequest natural inner join consumer"\
                " natural inner join person group by region, resource_keyword order by region;"
        cursor.execute(query)
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return result


    def delete(self, cid):
        return self.getAllRequest()

    def update(self, request_id):
        return self.getAllRequest()
