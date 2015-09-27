'''
Setup the app folder as a python module.
'''
from flask import Flask

# Set the Flask app
app = Flask(__name__)


# Import the webservice
from app import webservice
