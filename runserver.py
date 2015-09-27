'''
Starts up the weather app

'''

# Import the app's webservice
from app import app

# Setup logging
import logging
logging.basicConfig(filename="", format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)
logging.info("Starting Weather app web service...")

#  Public access & Enable debugger for now
app.run(host='0.0.0.0', debug=True)
