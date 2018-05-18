# -*-coding:utf-8-*-

from unidecode import unidecode
import re
import os
import json

class Parser:
	""" class to return key words """

	def __init__(self, query):
		# load json stopwords file
		path = os.path.abspath(os.path.dirname(__file__)) + "/stop_words_fr.json"
		with open(path, "r") as f:
			self.stop_words = json.load(f)['stop_words']
		self.query = query
		# create generator
		self.generator = self.generator()
		self.generator = self.parser(self.generator)
		# parse the query with generator
		self.query_keywords_list = [w for w in self.generator] # key words list
		self.query_keywords = self.url_key_words(self.query_keywords_list) # key words string


	def generator(self):
		""" yeld words in a string """
		current_word = ""
		for character in self.query.lower():
			if re.search("\w", character):
				current_word += character
			else:
				if current_word != "":
					yield unidecode(current_word)
					current_word = ""
		if current_word != "" or re.search("\w", current_word) is True:
			yield unidecode(current_word)


	def parser(self, generator):
		""" compare stopwords json file and value in generator """
		return [w for w in generator if w not in self.stop_words]


	def url_key_words(self, query_keywords):
		""" return a string of query key words list """
		url_key_words = ""
		for element in query_keywords:
			if url_key_words != "":
				url_key_words += "," + element
			else:
				url_key_words += element
		return url_key_words