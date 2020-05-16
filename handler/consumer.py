from flask import jsonify
from dao.consumer import ConsumerDAO


class ConsumerHandler:

    # consumer attributes: consumer_id, consumer_first_name, consumer_last_name, consumer_dob, consumer_address,
    # consumer_phone_number, consumer_email_address, consumer_severity

    def build_consumer_dictionary(self, row):
        result = {'person_id': row[0],
                  'consumer_id': row[1],
                  'consumer_severety': row[2],
                  'person_firstname': row[3],
                  'person_lastname': row[4],
                  'person_dob': row[5],
                  'person_address': row[6],
                  'person_phone_number': row[7],
                  'person_email': row[8]}
        return result

    def build_attribute_dict(self,pfname,plname,pdob,pcity,pphone,pemail):
        result = {}

        result['person_firstname'] = pfname
        result['person_lastname'] = plname
        result['person_dob'] = pdob
        result['person_city'] = pcity
        result['person_phone'] = pphone
        result['person_email'] = pemail
        return result

    def getAllConsumers(self):
        dao = ConsumerDAO()
        consumer_list = dao.getAllConsumers()
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dictionary(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

    def getConsumerById(self, consumer_id):
        dao = ConsumerDAO()
        row = dao.getConsumerById(consumer_id)
        if not row:
            return jsonify(Error="Consumer not found")
        else:
            consumer = self.build_consumer_dictionary(row)
            return consumer

    def insert(self, item):

        csev = item['consumer_severety']
        pfname = item['person_firstname']
        plname = item['person_lastname']
        pdob = item['person_dob']
        pcity = item['person_city']
        pphone = item['person_phone_number']
        pemail = item['person_email']

        if  pfname and plname and pdob and pcity and pphone and pemail :
            dao = ConsumerDAO()
            dao.insert(pfname,plname,pdob,pcity,pphone,pemail,csev)
            return jsonify(consumer=self.build_attribute_dict(pfname,plname,pdob,pcity,pphone,pemail)), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
