from flask import Flask
from flask_restful import Api
from Routes import water, heating
app = Flask(__name__)
api = Api(app)


@app.route('/water')
def water_root():
    return water.get_water_root()

@app.route('/water/status')
def water_status():
    return water.get_water_status()

@app.route('/water/boost', methods = ['POST'])
def boost_water():
    return water.boost_water()

@app.route('/water/turn_off', methods = ['POST'])
def turn_off_water():
    return water.turn_off_water()

    
@app.route('/heating')
def heating_root():
    return heating.get_heating_root()

@app.route('/heating/status')
def heating_status():
    return heating.get_heating_status()

@app.route('/heating/turn_on', methods = ['POST'])
def turn_on_heating():
    return heating.turn_on_heating()

@app.route('/heating/turn_off', methods = ['POST'])
def turn_off_heating():
    return heating.turn_off_heating()


if __name__ == '__main__':
    app.run(host='0.0.0.0') # run our Flask app