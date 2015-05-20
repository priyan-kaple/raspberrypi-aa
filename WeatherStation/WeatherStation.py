#!/usr/bin/env python
#
#
# To get BMP085 library:
#sudo apt-get update
#sudo apt-get install git build-essential python-dev python-smbus
#git clone https://github.com/adafruit/Adafruit_Python_BMP.git
#cd Adafruit_Python_BMP
#sudo python setup.py install
#
#

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import Adafruit_BMP.BMP085 as BMP085


app = Flask(__name__, static_folder='static', static_url_path='')
sensor = BMP085.BMP085()

def readWeatherSensors():
    return {'temp': sensor.read_temperature(),
            'pressure': sensor.read_pressure()};

@app.route("/")
def index():
    current = readWeatherSensors()
    return render_template('index.html',
                           homePage = True,
                           page_title = "Home Page",
                           temp = current['temp'],
                           pressure = current['pressure'])
                           
                           
                           
@app.route("/temp")
def temp():
    return render_template('index.html',
                           tempPage = True,
                           page_title = "Past Temperatures")    

@app.route("/pressure")
def pressure():
    return render_template('index.html',
                           pressurePage = True,
                           page_title = "Past Pressures")

@app.route("/forecast")
def forecast():
    return render_template('index.html',
                           forecastPage = True,
                           page_title = "Forecast")

if __name__ == "__main__":
    app.debug = True
    Bootstrap(app)
    app.run(host="0.0.0.0")
