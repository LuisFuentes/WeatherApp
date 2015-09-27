'''
    The public expose web service for the weather app
'''
from app import app
''' HTTP Public functions '''
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def Index():
    '''
    Test the hello world! page
    '''
	# TODO: Exposed welcome/index page...
	# for now, using index page as hello world page
    return "Hello World!"

@app.route('/WeatherApp/<weatherformat>/<int:zipcode>', methods=['GET'])
def GetWeatherAppByZip(weatherformat, zipcode):
	'''
	'''
	# Find existing web service that checks zip codes
	# and Validate the zipcode is valid
	
	return '%s' % zipcode

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
	# Find existing web service that checks city, state
	# are correct and valid
	
	return "%s, %s" % (city, state)
