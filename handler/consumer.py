from flask import jsonify
from dao.consumer import ConsumerDAO

class ConsumerHandler:

    # consumer attributes: consumer_id, consumer_first_name, consumer_last_name, consumer_dob, consumer_address, consumer_phone_number, consumer_email_address, consumer_severity

    def build_consumer_dictionary(self, row):
        result = {}
        result['consumer_id'] = row[0]
        result['consumer_first_name'] = row[1]
        result['consumer_last_name'] = row[2]
        result['consumer_dob'] = row[3]
        result['consumer_address'] = row[4]
        result['consumer_phone_number'] = row[5]
        result['consumer_email_address'] = row[6]
        result['consumer_severity'] = row[7]
        return result

    def build_payment_method_attributes(self, consumer_id, consumer_first_name, consumer_last_name, consumer_dob, consumer_address, consumer_phone_number, consumer_email_address, consumer_severity):
        result = {}
        result['consumer_id'] = consumer_id
        result['consumer_first_name'] = consumer_first_name
        result['consumer_last_name'] = consumer_last_name
        result['consumer_dob'] = consumer_dob
        result['consumer_address'] = consumer_address
        result['consumer_phone_number'] = consumer_phone_number
        result['consumer_email_address'] = consumer_email_address
        result['consumer_severity'] = consumer_severity

    def getAllConsumers(self):
        dao = ConsumerDAO()
        consumer_list = dao.getAllConsumers()
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dictionary(row)
            result_list.append(result)
        return jsonify(Consumer=result_list)

