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
    
@app.route('/heating')
def heating_root():
    return heating.get_heating_root()

@app.route('/heating/status')
def heating_status():
    return heating.get_heating_status()

if __name__ == '__main__':
    app.run(host='0.0.0.0') # run our Flask app