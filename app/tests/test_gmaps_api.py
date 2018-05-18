""" TESTING GOOGLE MAPS API"""

from ..utils.googlemaps_api import GoogleApi # import of test's target class
import urllib.request # import urllib for request/response simulation
from .. import app
from io import BytesIO # to create an object where it will be possible call the read() method
import json

class TestGoogleApi:
    """ Test class creation """


    def create_map(self):
        app.config.from_object('app.tests.config')
        return app
        
    def setup_method(self, test_geocode):
        """ setup_method function called during the TestGoogleApi class test """
        self.google_Api_Object = GoogleApi("openclassrooms,paris")

    def test_geocode(self, monkeypatch):
        """ geocoding service test with monkeypatch helper:
            a request to googlemaps API is simulated, a response
            in json format is expected
        """

        # open in read mode the json file with gmaps API data
        with open("gmaps_api_data.json", "r") as f:
            results = json.load(f)
        
        # BytesIO class utilisation
        self.results = BytesIO(json.dumps(results).encode())
        
        def mockreturn(request):

            return self.results
            
        # monkeypatch.setattr() method to change the returned value
        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        
        # expected returned values
        assert self.google_Api_Object.gmap_address(self.google_Api_Object.query_keywords) is True
        assert self.google_Api_Object.latitude == 48.8747578
        assert self.google_Api_Object.longitude == 2.350564700000001