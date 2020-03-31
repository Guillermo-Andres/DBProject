from flask import jsonify
from dao.company import CompanyDAO

class CompanyHandler:

    def build_company_dict(self , row ):
        result = {}

        result['cid']  = row[0]
        result['cname'] = row[1]
        result['cDes'] = row[2]


        return result
    
    def getAllComapnies(self):
        dao = CompanyDAO()
        cms = []
        items = dao.getAllCompanies()

        for i in items:
            result = self.build_company_dict(i)
            cms.append(result)
        
        return jsonify(Companies = cms)

    def getCompanyByID(self , cid):
        dao = CompanyDAO()
        cms = []
        items = dao.getCompanyByID(cid)

        for i in items:
            result = self.build_company_dict(i)
            cms.append(result)
        
        return jsonify(Companies = cms)

    def getCompanyByName(self , name):
        dao = CompanyDAO()
        cms = []
        items = dao.getCompanyByName(name)

        for i in items:
            result = self.build_company_dict(i)
            cms.append(result)
        
        return jsonify(Companies = cms)


    def getCompanyByDes(self , name):
        dao = CompanyDAO()
        cms = []
        items = dao.getCompanyByDes(name)

        for i in items:
            result = self.build_company_dict(i)
            cms.append(result)
        
        return jsonify(Companies = cms)

    def insert(self , item):
        return jsonify(Company= item) ,200
    def delete(self , id):
        return jsonify(Company= id) ,200
    def update(self , item):
        return jsonify(Company= item) ,200