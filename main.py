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

@app.route('/')
def greeting():
    return 'Hello, this is the almacenespr App!'

@app.route('/almacenespr/resource/food', methods=['GET', 'PUT'])
def searchFood():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return FoodHandler().getAllFood()
        else:
            return PartHandler().searchParts(request.args)


@app.route('/almacenespr/resource/medication', methods=['GET', 'PUT'])
def searchMedication():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return MedicationHandler().getAllMedication()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/resource/batteries', methods=['GET', 'PUT'])
def searchBatteries():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return BatteryHandler().getAllbattery()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/resource/clothes', methods=['GET', 'PUT'])
def searchClothing():
    if request.method == 'POST':

        print("REQUEST: ", requegetAllHeavyEquipmentst.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return ClothingHandler().getAllClothes()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/resource/heavyequipment', methods=['GET', 'PUT'])
def searchHeavyEquipment():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return HeavyEquipmentHandler().getAllHeavyEquipment()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/resource/ice', methods=['GET', 'PUT'])
def searchIce():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return IceHandler().getAllIce()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/resource/tools', methods=['GET', 'PUT'])
def searchTools():
    if request.method == 'POST':

        print("REQUEST: ", request.json)
        return UserHandler().insertUserJson(request.json)
    else:
        if not request.args:
            return PowerToolsHandler().getAllTools()
        else:
            return PartHandler().searchParts(request.args)

@app.route('/almacenespr/resource/fuel', methods=['GET', 'PUT'])
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
