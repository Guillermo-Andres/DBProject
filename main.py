from flask import Flask, jsonify, request , redirect , url_for
from handler.babyFood import babyFoodHandler
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
from handler.medicalDevices import MedicalDevicesHandler
from handler.powerGenerator import PowerGeneratorHandler
from handler.hygiene import HygieneHandler
from handler.order import OrderHandler
from handler.payment_method import PaymentMethodHandler
from handler.paysFor import PaysForHandler
from handler.placesAnOrder import PlacesAnOrderHandler
from handler.supplier import SupplierHandler
from handler.supplies import suppliesHandler
from handler.worksFor import WorksForHandler
from handler.ResourceHandler import ResourceHandler
from handler.water import WaterHandler
from handler.request import RequestHandler
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def sendtToLogin():
    return redirect(url_for('registerConsumer'))


#Register user route Unused for phase 2
@app.route('/almacenespr/register/consumer', methods = ['POST','GET'])
def registerConsumer():
    #orders specify if we are requesting, reserving or purchasing depending on its status
    if request.method == 'GET':
        return ConsumerHandler().getAllConsumers()

    elif request.method == 'POST':
        return ConsumerHandler().insert(request.get_json())

#Get consumer by ID
@app.route('/almacenespr/consumer/<int:consumer_id>', methods = ['GET'])
def getConsumerbyId(consumer_id):
    #orders specify if we are requesting, reserving or purchasing depending on its status
    if request.method == 'GET':
        return ConsumerHandler().getConsumerById(consumer_id)

#view all consumers
@app.route('/almacenespr/consumer', methods = ['GET'])
def getAllconsumer():
    #orders specify if we are requesting, reserving or purchasing depending on its status
    if request.method == 'GET':
        return ConsumerHandler().getAllConsumers()


@app.route('/almacenespr/register/admin', methods = ['POST','GET'])
def registerAdmin():
    #orders specify if we are requesting, reserving or purchasing depending on its status
    arg = request.get_json()
    if request.method == 'GET':
        return AdminHandler().getAllAdmins()

    elif request.method == 'POST':
        return AdminHandler().insert(request.get_json())

@app.route('/almacenespr/admin', methods = ['POST','GET'])
def getAllAdmin():
    #orders specify if we are requesting, reserving or purchasing depending on its status
    arg = request.get_json()

    if request.method == 'GET':
        return AdminHandler().getAllAdmins()

    elif request.method == 'POST':
        return AdminHandler().insert(request.get_json())

#search admin by id
@app.route('/almacenespr/admin/<int:admin_id>', methods = ['GET'])
def getAdminById(admin_id):
    #orders specify if we are requesting, reserving or purchasing depending on its status
    arg = request.get_json()

    if request.method == 'GET':
        return AdminHandler().getAdminByID(admin_id)


@app.route('/almacenespr/supplier', methods = ['POST','GET'])
def registerSupplier():
    #orders specify if we are requesting, reserving or purchasing depending on its status

    if request.method == 'GET':
        return SupplierHandler().getAllSuppliers()

    elif request.method == 'POST':
        return SupplierHandler().insert(request.get_json())

#get supplier by id
@app.route('/almacenespr/supplier/<int:supplier_id>', methods = ['GET'])
def getSupplierById(supplier_id):
    #orders specify if we are requesting, reserving or purchasing depending on its status
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(supplier_id)

#get all suppliers
@app.route('/almacenespr/supplier', methods = ['GET'])
def getAllSuppliers():
    #orders specify if we are requesting, reserving or purchasing depending on its status

    if request.method == 'GET':
        return SupplierHandler().getAllSuppliers()



@app.route('/almacenespr/consumer/<int:consumer_id>/orders', methods = ['GET','POST','PUT'])
def orderResources(consumer_id):
    #orders specify if we are requesting, reserving or purchasing depending on its status

    if request.method == 'GET':
        return OrderHandler().geOrdersByConsumerID(consumer_id)

    elif request.method == 'POST':
        #TODO aqui en el futuero hay que llamar varios inserts (orden , contains  , etc...)
        return OrderHandler().insert(request.get_json())

    elif request.method == 'PUT':
        return OrderHandler().update(request.get_json())

@app.route('/almacenespr/supplier/<int:sid>/newresource', methods = ['POST','PUT','GET'])
def newResource(sid):
    #TODO otros resources aqui es donde seria bueno tener un "ResourceHandler" que se encarge de la logica internamente

    if request.method == 'GET':
        return babyFoodHandler().getAllFood()

    elif request.method == 'POST':
        return babyFoodHandler().insert(request.get_json())

    elif request.method == 'PUT':
        return babyFoodHandler().update(request.get_json())

@app.route('/almacenespr/requested', methods = ['GET'])
def viewRequested():
    return RequestHandler().getAllRequestsAll()

@app.route('/almacenespr/requested/<string:keyword>', methods = ['GET'])
def viewRequestedByKeyword(keyword):
    return RequestHandler().getAllRequestByKeyword(keyword)

@app.route('/almacenespr/available', methods = ['GET'])
def viewAvailable():
    return ResourceHandler().getAll()

# @app.route('/almacenespr/requested/<string:resource_type>', methods = ['GET'])
# def searchRequested(resource_type,search_keyword):
#
#     return RequestHandler().getAllByType(resource_type)

@app.route('/almacenespr/requested/<int:request_id>', methods = ['GET'])
def searchRequestedById(request_id):

    return RequestHandler().getRequestById(request_id)

@app.route('/almacenespr/resource/<int:resource_id>', methods = ['GET'])
def getResourcesbyId(resource_id):
    return ResourceHandler().getResourceById(resource_id)


@app.route('/almacenespr/resource/<string:resource_type>/<int:resource_type_id>', methods = ['GET'])
def getResourcesbyTypeId(resource_type, resource_type_id):
    if resource_type == 'fuel':
        return FuelHandler().getFuelById(resource_type_id)
    if resource_type == 'ice':
        return IceHandler().getIceById(resource_type_id)
    if resource_type == 'clothing':
        return ClothingHandler().getClothesgById(resource_type_id)
    if resource_type == 'battery':
        return BatteryHandler().getBatteryById(resource_type_id)
    if resource_type == 'babyfood':
        return babyFoodHandler().getbabyFoodById(resource_type_id)
    if resource_type == 'cannedfood':
        return cannedFoodHandler().getcannedFoodById(resource_type_id)
    if resource_type == 'dryfood':
        return dryFoodHandler().getdryFoodById(resource_type_id)
    if resource_type == 'heavyequipment':
        return HeavyEquipmentHandler().getHeavyEquimentById(resource_type_id)
    if resource_type == 'medication':
        return MedicationHandler().getMedicationById(resource_type_id)
    if resource_type == 'tools':
        return PowerToolsHandler().getToolById(resource_type_id)
    if resource_type == 'water':
        return WaterHandler().getWaterById(resource_type_id)
    else:
        return ResourceHandler().getAllByType(resource_type)

@app.route('/almacenespr/resource/<string:resource_type>/', methods = ['GET'])
def getResources(resource_type):
    return ResourceHandler().getAllByType(resource_type)


@app.route('/almacenespr/available/<string:resource_type>/<string:search_keyword>', methods = ['GET'])
def searchAvailable(resource_type,search_keyword):
    return ResourceHandler().getAllByType(resource_type)

@app.route('/almacenespr/dashboard/statistics/daily/<int:type>', methods = ['GET'])
def dailyStatistics(type):
    if type == 0:
        #return stats for in need
        return babyFoodHandler().getAllFood()
    elif type == 1 :
        #return sta
        # ts for available
        return babyFoodHandler().getAllFood()
    else :
        #return stats for match
        return babyFoodHandler().getAllFood()

@app.route('/almacenespr/dashboard/statistics/weekly/<int:type>', methods = ['GET'])
def weeklyStatistics(type):
    if type == 0:
        #return stats for in need
        return babyFoodHandler().getAllFood()
    elif type == 1 :
        #return stats for available
        return babyFoodHandler().getAllFood()
    else :
        #return stats for match
        return babyFoodHandler().getAllFood()
@app.route('/almacenespr/dashboard/statistics/region/<int:type>', methods = ['GET'])
def regionStatistics(type):
    if type == 0:
        #return stats for in need
        return babyFoodHandler().getAllFood()
    elif type == 1 :
        #return stats for available
        return babyFoodHandler().getAllFood()
    else :
        #return stats for match
        return babyFoodHandler().getAllFood()

if __name__ == '__main__':
     app.run()
