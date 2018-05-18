# CONFIGURATION VARIABLES

import random, string

# see doc at http://flask.pocoo.org/docs/0.12/quickstart/ -> paragraph "SESSION"
SECRET_KEY = "".join([random.choice(string.printable) for _ in range(24)])

# to get your JS API key go to https://developers.google.com/maps/documentation/javascript/get-api-key
GOOGLE_JS_KEY = "AIzaSyCijZFozLf948SNQzcGVkRaPZ-8wymgkkk"
# to get your GEO API key go to https://developers.google.com/maps/documentation/geocoding/get-api-key
GOOGLE_GEO_KEY = "AIzaSyC-DXpHl3cl41Gn6nAAF-FTF4NVJxZgSI4"

URL = "https://ema-grandpybot.herokuapp.com/"
