from flask import Flask, jsonify, request
from handler.food import FoodHandler
from handler.medication import MedicationHandler
from handler.batteries import BatteryHandler
from handler.clothing import ClothingHandler
from handler.heavyequipment import HeavyEquipmentHandler
from handler.ice import IceHandler
from handler.powertools import PowerToolsHandler
from handler.fuel import FuelHandler
from handler.admin import AdminHandler
from handler.supplier import SupplierHandler
from handler.company import CompanyHandler
from handler.consumer import ConsumerHandler
from handler.contains import ContainsHandler
from handler.diapers import DiapersHandler
from handler.femenine_hygiene import FemenineHygieneHandler
from handler.hygiene import HygieneHandler
from handler.order import OrderHandler
from handler.payment_method import PaymentMethodHandler
from handler.paysFor import PaysForHandler
from handler.placesAnOrder import PlacesAnOrderHandler
from handler.supplier import SupplierHandler
from handler.supplies import suppliesHandler
from handler.worksFor import WorksForHandler
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/almacenespr/register/consumer', methods = ['POST','GET'])
def registerconsumer():
    #orders specify if we are requesting, reserving or purchasing depending on its status
    return ConsumerHandler().insert()

@app.route('/almacenespr/register/admin', methods = ['POST','GET'])
def registerAdmin():
    #orders specify if we are requesting, reserving or purchasing depending on its status
    return AdminHandler().insert(3)

@app.route('/almacenespr/register/supplier', methods = ['POST','GET'])
def registerSupplier():
    #orders specify if we are requesting, reserving or purchasing depending on its status
    return SupplierHandler.insert()

@app.route('/almacenespr/consumer/<int:consumer_id>/orders', methods = ['POST','PUT'])
def orderResources(consumer_id):
    #orders specify if we are requesting, reserving or purchasing depending on its status
    return PlacesAnOrderHandler().insert(3)

@app.route('/almacenespr/supplier/<int:sid>/newresource', methods = ['POST','PUT'])
def newResource(sid):
    return suppliesHandler().insert(3)

@app.route('/almacenespr/requested', methods = ['GET'])
def viewRequested():
    return OrderHandler().getOrderByStatus('pending')

@app.route('/almacenespr/available', methods = ['GET'])
def viewAvailable():
    return AdminHandler.getAllAdmins()

@app.route('/almacenespr/requested/<string:resource_type>/<string:search_keyword>', methods = ['GET'])
def searchRequested(resource_type,search_keyword):
    return FoodHandler().getAllFood()

@app.route('/almacenespr/<string:resource_type>/', methods = ['GET'])
def getAllResources(resource_type):
    return FoodHandler().getAllFood()

@app.route('/almacenespr/available/<string:resource_type>/<string:search_keyword>', methods = ['GET'])
def searchAvailable(resource_type,search_keyword):
    return FoodHandler().getAllFood()

@app.route('/almacenespr/dashboard/statistics/daily/<int:type>', methods = ['GET'])
def dailyStatistics(type):
    if type == 0:
        #return stats for in need
        return FoodHandler().getAllFood()
    elif type == 1 :
        #return stats for available
        return FoodHandler().getAllFood()
    else :
        #return stats for match
        return FoodHandler().getAllFood()

@app.route('/almacenespr/dashboard/statistics/weekly/<int:type>', methods = ['GET'])
def weeklyStatistics(type):
    if type == 0:
        #return stats for in need
        return FoodHandler().getAllFood()
    elif type == 1 :
        #return stats for available
        return FoodHandler().getAllFood()
    else :
        #return stats for match
        return FoodHandler().getAllFood()
@app.route('/almacenespr/dashboard/statistics/region/<int:type>', methods = ['GET'])
def regionStatistics(type):
    if type == 0:
        #return stats for in need
        return FoodHandler().getAllFood()
    elif type == 1 :
        #return stats for available
        return FoodHandler().getAllFood()
    else :
        #return stats for match
        return FoodHandler().getAllFood()

@app.route('/almacenespr/food', methods=['GET', 'PUT'])
def searchFood():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return FoodHandler().getAllFood()
        else:
            return PartHandler().searchParts(request.args)


@app.route('/almacenespr/medication', methods=['GET', 'PUT'])
def searchMedication():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return MedicationHandler().getAllMedication()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/batteries', methods=['GET', 'PUT'])
def searchBatteries():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return BatteryHandler().getAllbattery()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/clothes', methods=['GET', 'PUT'])
def searchClothing():
    if request.method == 'POST':

        print("REQUEST: ", requegetAllHeavyEquipmentst.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return ClothingHandler().getAllClothes()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/heavyequipment', methods=['GET', 'PUT'])
def searchHeavyEquipment():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return HeavyEquipmentHandler().getAllHeavyEquipment()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/ice', methods=['GET', 'PUT'])
def searchIce():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return IceHandler().getAllIce()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/tools', methods=['GET', 'PUT'])
def searchTools():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return PowerToolsHandler().getAllTools()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/fuel', methods=['GET', 'PUT'])
def searchFuel():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return FuelHandler().getAllFuel()
        else:
            return PartHandler().searchParts(request.args)





if __name__ == '__main__':
     app.run()
