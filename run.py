#! /usr/bin/env python

# to launch the server from console: "python run.py"
from app import app

if __name__ == '__main__':
	app.run(debug=True)