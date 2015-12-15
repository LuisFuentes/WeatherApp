'''
    The public expose web service for the weather app
'''
from app import app
from flask import render_template
from location.location import LocationValidator

''' HTTP Public functions '''
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def Index():
    '''
    Test the hello world! page
    '''
	# TODO: Exposed welcome/index page...
	# for now, using index page as hello world page
    return render_template('index.html')

@app.route('/WeatherApp/<weatherformat>/<zipCode>', methods=['GET'])
def GetWeatherAppByZip(weatherformat, zipCode):
    '''
	'''
    location_validator = LocationValidator(zipCode)
    resp = location_validator.is_valid_zip_code_location()
    return '%s' % resp

    #return '%s' % zipCode

@app.route('/WeatherApp/<weatherformat>/<int:latitude>/<int:longitude>', methods=['GET'])
def GetWeatherAppByLatLong(weatherformat, latitude, longitude):
	'''
	'''
	# Find existing web service that checks lat-long
	# and Validate the lat-long is valid

	return '%s, %s' % (latitude, longitude)

@app.route('/WeatherApp/<weatherformat>/<city>/<state>', methods=['GET'])
def GetWeatherAppByCityState(weatherformat, city, state):
    '''
    '''
    # Find existing web service that checks city, state are correct and valid
    return '%s, %s' % (city, state)
