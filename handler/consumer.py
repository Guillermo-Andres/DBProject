from flask import jsonify
from dao.consumer import ConsumerDAO


class ConsumerHandler:

    # consumer attributes: consumer_id, consumer_first_name, consumer_last_name, consumer_dob, consumer_address,
    # consumer_phone_number, consumer_email_address, consumer_severity

    def build_consumer_dictionary(self, row):
        result = {'person_id': row[0],
                  'consumer_id': row[1],
                  'consumer_severity': row[2],
                  'person_firstname': row[3],
                  'person_lastname': row[4],
                  'person_dob': row[5],
                  'person_address': row[6],
                  'person_phone_number': row[7],
                  'person_email': row[8]}
        return result

    def build_payment_method_attributes(self, consumer_id, consumer_first_name, consumer_last_name, consumer_dob,
                                        consumer_address, consumer_phone_number, consumer_email_address,
                                        consumer_severity):
        result = {'consumer_id': consumer_id, 'consumer_first_name': consumer_first_name,
                  'consumer_last_name': consumer_last_name, 'consumer_dob': consumer_dob,
                  'consumer_address': consumer_address, 'consumer_phone_number': consumer_phone_number,
                  'consumer_email_address': consumer_email_address, 'consumer_severity': consumer_severity}
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

    def getConsumerByName(self, consumer_first_name, consumer_last_name):
        return self.getAllConsumers()

    def getConsumerByDOB(self, dob):
        return self.getAllConsumers()

    def getConsumerByAddress(self, address):
        return self.getAllConsumers()

    def getConsumerByPhoneNumber(self, phone_number):
        return self.getAllConsumers()

    def getConsumerByEmail(self, email):
        return self.getAllConsumers()

    def getConsumerBySeverity(self, severity):
        return self.getAllConsumers()

    def insert(self, item):
        return jsonify(Consumer=item), 200

    def delete(self, item):
        return jsonify(Consumer=item), 200

    def update(self, item):
        return jsonify(Consumer=item), 200
