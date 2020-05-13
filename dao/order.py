from config.dbconfig import pg_config
import psycopg2


class OrderDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllOrders(self):
        cursor = self.conn.cursor()
        query = "select * from orders natural join (select supplier_id from supplier) as sup natural join resource natural join supplies natural join request natural join makesRequest natural join (select consumer_id , consumer_severety from consumer)as cons natural join paymentMethod natural join paysFor; "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderById(self, order_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from orders natural join supplier natural join resource natural join supplies natural join request natural join makesRequest natural join (select consumer_id , consumer_severety from consumer)as cons natural join paymentMethod natural join paysFor " \
                "where order_id = %s;"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        return result

    def getReserved(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from orders natural join supplier natural join resource natural join supplies natural join request natural join makesRequest natural join (select consumer_id , consumer_severety from consumer)as cons natural join paymentMethod natural join paysFor " \
                "where order_amount = 0;"
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchased(self):
        cursor = self.conn.cursor()
        query = "select * " \
                "from orders natural join (select supplier_id from supplier) as sup natural join resource natural join supplies natural join request natural join makesRequest natural join (select consumer_id , consumer_severety from consumer)as cons natural join paymentMethod natural join paysFor " \
                "where order_amount <> 0;"
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderByConsumerId(self, consumer_id):
        cursor = self.conn.cursor()
        query = "select * " \
                "from orders natural join supplier natural join resource natural join supplies natural join request natural join makesRequest natural join (select consumer_id , consumer_severety from consumer)as cons natural join paymentMethod natural join paysFor " \
                "where consumer_id = %s;"
        cursor.execute(query, (consumer_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderStatsPerDay(self):
        cursor = self.conn.cursor()
        query = "select resource_name, count(resource_name) as matching_resources, date_trunc('day', " \
                "order_date) as day from orders natural inner join resource group by day, resource_name " \
                "order by day ; "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderStatsPerWeek(self):
        cursor = self.conn.cursor()
        query = "select resource_name, count(resource_name) as matching_resources, date_trunc('week', " \
                "order_date) as week from orders natural inner join resource group by week, resource_name " \
                "order by week ; "
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderStatsPerRegion(self):
        cursor = self.conn.cursor()
        query = "select resource_name, count(resource_name) as order_per_region, get_region(person_city) as region" \
                " from orders natural inner join resource natural inner join supplier natural inner join person" \
                " group by region, resource_name " \
                " order by region;"
        cursor.execute(query)
        result = []
        for row in cursor:
            print(row)
            result.append(row)
        return result

    def getOrderByAmount(self, amount):
        return self.getAllOrders()

    def getOrderByDate(self, date):
        return self.getAllOrders()

    def getOrderByStatus(self, status):
        return self.getAllOrders()

    def insert(self):
        return self.getAllOrders()

    def delete(self):
        return self.getAllOrders()

    def update(self):
        return self.getAllOrders()
