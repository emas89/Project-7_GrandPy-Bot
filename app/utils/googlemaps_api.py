# -*-coding:utf-8-*-

import urllib.request, urllib.error
from app.starter import app
import json

class GoogleApi:

	"""Class that calls Google Maps Api by address keywords 
	and returns an object with address, longitude, latitude """

	def __init__(self, url_key_words):

		self.key = app.config['GOOGLE_GEO_KEY']
		self.query_keywords = url_key_words
		self.longitude = 0
		self.latitude = 0

	def gmap_response(self):
		# manage content display and/or catch any errors

		url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(self.query_keywords, self.key)

		try:
			content = urllib.request.urlopen(url)
			self.data = json.loads(content.read().decode("utf8"))
			return True


		except urllib.error.HTTPError as e_http:
			app.logger.error(("HTTP Error (Google Maps API) on link "+" "+url, e_http))
			return False


		except urllib.error.URLError as e_url:
			
			app.logger.error(("URL Error (Google Maps API) on link "+" "+url, e_url))
			return False


		except json.decoder.JSONDecodeError as e_json:
			app.logger.error("Content not found (Google Maps API) ", e_json)
			return False


	def gmap_address(self, query_keywords):

		if self.gmap_response(): #content found

			if 'status' in self.data.keys() and self.data['status'] == "OK":

				self.address = self.data['results'][0]['formatted_address']
				self.longitude = self.data['results'][0]['geometry']['location']['lng']
				self.latitude = self.data['results'][0]['geometry']['location']['lat']
	
				return True

			else:
	
				return False

		else: #zero results
			

			return False