# CONFIGURATION VARIABLES

import random, string

# see doc at http://flask.pocoo.org/docs/0.12/quickstart/ -> paragraph "SESSION"
SECRET_KEY = "".join([random.choice(string.printable) for _ in range(24)])

# to get your JS API key go to https://developers.google.com/maps/documentation/javascript/get-api-key
GOOGLE_JS_KEY = "your personal Google Maps API JavaScrpt key"
# to get your GEO API key go to https://developers.google.com/maps/documentation/geocoding/get-api-key
GOOGLE_GEO_KEY = "your personal Google Maps API Geocoding key"

URL = "https://ema-grandpybot.herokuapp.com/"
