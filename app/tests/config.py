""" Configuration script for tests purposes """

import random, string


SECRET_KEY = "".join([random.choice(string.printable) for _ in range(24)])

GOOGLE_JS_KEY = "AIzaSyCijZFozLf948SNQzcGVkRaPZ-8wymgkkk"
GOOGLE_GEO_KEY = "AIzaSyC-DXpHl3cl41Gn6nAAF-FTF4NVJxZgSI4"

URL = "http://localhost:5000/"


DEBUG = True
TESTING = True
LIVESERVER_PORT = 5000
LIVESERVER_TIMEOUT = 10