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
