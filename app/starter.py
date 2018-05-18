from flask import Flask

# Cross Origin Ressource Sharing
# see (doc. at https://pypi.python.org/pypi/Flask-Cors)
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #Cross Origin Ressource Sharing Allowing
app.config.from_object('config')