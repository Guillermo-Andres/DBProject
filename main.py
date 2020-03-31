from flask import Flask, jsonify, request
from handler.food import FoodHandler
from handler.medication import MedicationHandler
from handler.batteries import BatteryHandler
from handler.clothing import ClothingHandler
from handler.heavyequipment import HeavyEquipmentHandler
from handler.ice import IceHandler
from handler.powertools import PowerToolsHandler
from handler.fuel import FuelHandler
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


#4. Add a request for a given resource   4.)almacenespr/user<id>/orders   4.)POST de ORDER
#5.)almacenespr/supplier<id>/newresource
#6. Reserve or purchase a resource. Free resources are reserved. Otherwise, they are purchased. 6.)almacenespr/user<id>/orders (aqui mismo el front end se encarga de split entre reserved y eso) 
#7.) almacenespr/requested/  7.) GET de order    7.) almacenespr/requested/
#8.) almacenespr/available/  8.) GET de resource 8.) almacenespr/available/
# 9. See detail of resources, including location on a Google Map    9.)almacenespr/resource<type>/resource<id> (todos los attributos de a given reource) 9.)GET de resource
# 10. Keyword search resources being requested, with sorting by resource name             10.) almacenespr/requested/resource<type>/search<keyword>            10.)GET  de order
# 11. Keyword search resources available, with sorting by resource name               11.)almacenespr/available/resource<type> /search<keyword>                11.) get resource


# 12.)almacenespr/dashboard/statistics/daily/<type>
# 13.)almacenespr/dashboard/statistics/weekly/<type>
# 14.)almacenespr/dashboard/statistics/region<type>

@app.route('/almacenespr/user/<int:user_id>/orders', methods = ['POST'])
def orderResources(user_id):
    #orders specify if we are requesting, reserving or purchasing depending on its status
    return FoodHandler().getAllFood()

@app.route('/almacenespr/supplier/<int:sid>/newresource', methods = ['POST'])
def newResource(sid):
    return FoodHandler().getAllFood()

@app.route('/almacenespr/requested', methods = ['GET'])
def viewRequested():
    return FoodHandler().getAllFood()

@app.route('/almacenespr/available', methods = ['GET'])
def viewAvailable():
    return FoodHandler().getAllFood()

@app.route('/almacenespr/<string:resource_type>/', methods = ['GET'])
def getAllResources(resource_type):
    return FoodHandler().getAllFood()

@app.route('/almacenespr/requested/<string:resource_type>/<string:search_keyword>', methods = ['GET'])
def searchRequested(resource_type,search_keyword):
    return FoodHandler().getAllFood()

@app.route('/almacenespr/available/<string:resource_type>/<string:search_keyword>', methods = ['GET'])
def searchAvailable(resource_type,search_keyword):
    return FoodHandler().getAllFood()

@app.route('/almacenespr/dashboard/statistics/daily/<int:type>', methods = ['GET'])
def dailyStatistics(type):
    return FoodHandler().getAllFood()

@app.route('/almacenespr/dashboard/statistics/weekly/<int:type>', methods = ['GET'])
def weeklyStatistics(type):
    return FoodHandler().getAllFood()

@app.route('/almacenespr/dashboard/statistics/region/<int:type>', methods = ['GET'])
def regionStatistics(type):
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
