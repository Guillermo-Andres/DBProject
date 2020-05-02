from flask import jsonify
from dao.person import PersonDAO


class PersonHandler:

    def build_Person_dict(self, row):
        result = {}

        result['uid'] = row[0]
        result['uname'] = row[1]
        result['uAddress'] = row[2]
        result['uPhone'] = row[3]
        result['uEmail'] = row[4]

        return result

    def getAllPersons(self):
        dao = PersonDAO()
        persons = []
        items = dao.getAllPersons()

        for i in items:
            result = self.build_Person_dict(i)
            persons.append(result)

        return jsonify(Person=persons)

    def getPersonByID(self, aid):
        dao = PersonDAO()
        persons = []
        items = dao.getPersonByID(aid)

        for i in items:
            result = self.build_Person_dict(i)
            persons.append(result)

        return jsonify(Person=persons)

    def getPersonByName(self, name):
        dao = PersonDAO()
        persons = []
        items = dao.getPersonByName(name)

        for i in items:
            result = self.build_Person_dict(i)
            persons.append(result)

        return jsonify(Person=persons)

    def getPersonByAddress(self, location):
        dao = PersonDAO()
        persons = []
        items = dao.getPersonByLocation(location)

        for i in items:
            result = self.build_Person_dict(i)
            persons.append(result)

        return jsonify(Person=persons)

    def getPersonByPhone(self, phone):
        dao = PersonDAO()
        persons = []
        items = dao.getPersonByPhone(phone)

        for i in items:
            result = self.build_Person_dict(i)
            persons.append(result)

        return jsonify(Person=persons)

    def getPersonByEmail(self, email):
        dao = PersonDAO()
        persons = []
        items = dao.getPersonByEmail(email)

        for i in items:
            result = self.build_Person_dict(i)
            persons.append(result)

        return jsonify(Person=persons)

    def insert(self, item):
        return 1

    def delete(self, id):
        return 1

    def update(self, item):
        return 1
