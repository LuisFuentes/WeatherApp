import re
import requests
from xml.etree import ElementTree as ET


class LocationValidator:
    '''
        Validator class for locations
    '''

    def __init__(self, zipCode=None, city=None, state=None):
        self.zipCode = zipCode
        self.city = city
        self.state = state
        self.time_zone = None

    def is_valid_zip_code_location(self):
        '''
            Checks if the location of the zip code is valid
        '''
        # First check if it's a valid format
        if not is_valid_zip_format(self.zipCode):
            return {"IsValidZip": False, "Message": "Error - Incorrect format"}

        # Now use a REST api to check if the zip is a valid location
        # TODO: Let's pass this in as a config item, but for now
        # hard code it

        # Get the response and check if the Zip is valid
        xml_response = requests.get("http://www.webservicex.net/"
            "uszip.asmx/GetInfoByZIP?USZip=" + self.zipCode)
        if xml_response is None:
            return "ERROR" #TODO: Handle this better
        xml_response = xml_response.content

        # Parse the xml response
        tree = ET.fromstring(xml_response)[0]
        # Get each element
        self.city = tree.find('CITY').text
        self.state = tree.find('STATE').text
        self.time_zone = tree.find('TIME_ZONE').text
        return {"IsValidZip": True,
                "City": self.city,
                "State": self.state}


def is_valid_zip_format(zipCode):
        '''
            Validates the zip code of a location
        '''
        validZipCodes = re.compile("^[0-9]{5}(?:-[0-9]{4})?$")
        if validZipCodes.match(zipCode):
            return True
        return False
