# -*-coding:utf-8-*-

import urllib.request, urllib.error
import json
from app.starter import app

class MediaWiki:
	""" class to call MediaWiki API """
	def __init__(self, latitude, longitude, url_keywords_list):
		self.latitude = latitude
		self.longitude = longitude
		self.url_keywords = url_keywords_list
		self.page_ids = 0

	def keywords_searching(self):
		""" search Wikipedia page that contains the wanted key words """
		keywords = ""
		# browse the url_keywords list
		for element in self.url_keywords:
			if keywords != "":
				keywords += "%20" + element #add the percent-encoded space
			else:
				keywords += element

		keywords_searching_url = "https://fr.wikipedia.org/w/api.php?action=query&format=json&list=search&srlimit=1&srsearch={}".format(keywords)

		# manage page display and errors
		try:
			content = urllib.request.urlopen(keywords_searching_url)
			self.data = json.loads(content.read().decode("utf8"))

		except urllib.error.URLError as e:
			error = "MediaWiki API error in function (keywords_searching)."
			app.logger.error(e, error)

		if "search" in self.data['query'].keys():
			# if json file is not empty
			if len(self.data['query']['search']) > 0:
				self.page_ids = self.data['query']['search'][0]['pageid']
		else:
			# if json file is empty
			self.page_ids = 0


	def geo_searching(self):
		""" search Wikipedia page with the wanted coordinates """
		url_coord = "https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gsradius=5000&gslimit=1&format=json&gscoord={}%7C{}".format(self.latitude, self.longitude)

		# if keywords_searching function returns no results,
		# try to find a wiki page id by geo coordinates to show a similar content
		try:
			content = urllib.request.urlopen(url_coord)
			self.data = json.loads(content.read().decode("utf8"))

		except urllib.error.URLError as e:
			error = "MediaWiki API error in function (geo_searching)."
			app.logger.error(e, error)

		# if json file is not empty
		if "geosearch" in self.data['query'].keys() and len(self.data['query']['geosearch']) > 0:
			self.page_ids = self.data['query']['geosearch'][0]['pageid']
		else:
			# if json file is empty
			self.page_ids = 0


	def wiki_page_finder(self):
		""" function that finds the Wiki page by key words and coordinates """

		# by key words function
		self.keywords_searching()
		# if the research by key words produces no results
		if self.page_ids == 0:
			# research by coordinates function
			self.geo_searching()
		else:
			# if the research by key words is productive
			return True

		if self.page_ids != 0:
			return True
		else:
			return False


	def page_id_finder(self):
		""" if a Wiki page is found, go to read its first lines """
		if self.wiki_page_finder():
			page_searching_url = "https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=1&explaintext=1&exsentences=2&pageids={}".format(self.page_ids)

			try:
				content = urllib.request.urlopen(page_searching_url)
				self.data = json.loads(content.read().decode("utf8"))
				return True

			except urllib.error.URLError as e:
				error = "MediaWiki API error in function (page_id_finder)."
				app.logger.error(e, error)
				return False
		else:
			return False


	def sentences_return(self):
		""" Returns the two first sentences of Wiki page """

		# if content found
		if self.page_id_finder():
			if "query" in self.data.keys():
				self.wiki_search = self.data['query']['pages'][str(self.page_ids)]['extract']
				return True
			else:
				return False
		# if content not found
		else:
			return False