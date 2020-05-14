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
                "from request natural inner join resource natural inner join consumer natural inner join makesRequest; "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, request_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural inner join resource natural inner join consumer natural inner join makesRequest " \
                "where request_id = %s;"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def getResourceInRequest(self, request_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural inner join resource " \
                "where request_id = %s"
        cursor.execute(query, (request_id,))
        result = cursor.fetchone()
        return result

    def getRequestByKeyWord(self , keyword):
        cursor = self.conn.cursor()
        query = "select * " \
                "from request natural inner join resource natural inner join consumer natural inner join makesRequest "\
                "where resource_name  ~*  %s OR resource_description ~* %s; "

        keyword = "(" + keyword + ")"
        cursor.execute(query , (keyword,keyword))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, resource_id , consumer_id ):
        cursor = self.conn.cursor()
        query ="insert into request(resource_id , request_date) values (%s , CURRENT_DATE ) returning request_id;"
        cursor.execute(query , (resource_id ,))
        request  = cursor.fetchone()[0]
        self.conn.commit()

        cursor = self.conn.cursor()
        query = "insert into makesRequest(consumer_id , request_id) values (%s , %s); "
        cursor.execute(query , (consumer_id , request))
        self.conn.commit()
        """ check for match """ 
        
        resources = ResourceDAO().getResourceById(resource_id)

        if(resources[4] > 0 ):
            
            #found match , create order
            order = OrderDAO().insert(resource_id)
           
            cursor = self.conn.cursor()
            #attach a paymentMethod
            query =  "select paymentMethod_id from paymentMethod where consumer_id = %s;"
            cursor.execute(query , (consumer_id , ))
            paymentMethod_id =  cursor.fetchone()[0]
            print(paymentMethod_id)
            self.conn.commit()
            cursor = self.conn.cursor()
            print(str(paymentMethod_id) + " " + str(order))
            query = "insert into paysFor(paymentMethod_id , order_id) values (%s ,%s);"
            cursor.execute(query , ( paymentMethod_id , order))
            self.conn.commit()
            print (True , order)
            return (True , order)
        
        else:
            return (False , request)

       

        


    def getRequestStatsPerDay(self):
        cursor = self.conn.cursor()
        query = "select resource_name, count(resource_name) as number_of_requests_per_resource, date_trunc('day', " \
                "request_date) as day from request natural inner join resource group by day, resource_name " \
                "order by date_trunc('day', request_date) ; "
        cursor.execute(query)
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return result

    def getRequestStatsPerWeek(self):
        cursor = self.conn.cursor()
        query = "select resource_name, count(resource_name) as number_of_requests_per_resource, date_trunc('week', " \
                "request_date) as week from request natural inner join resource group by week, resource_name " \
                "order by week; "
        cursor.execute(query)
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return result

    def getRequestStatsPerRegion(self):
        cursor = self.conn.cursor()
        query = "select resource_name, count(resource_name) as request_per_region, get_region(person_city) as region" \
                " from request natural inner join resource natural inner join makesRequest natural inner join consumer"\
                " natural inner join person group by region, resource_name order by region;"
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
