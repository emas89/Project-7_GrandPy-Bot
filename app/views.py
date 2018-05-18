# -*-coding:utf-8-*-
from flask import render_template, request
from app.utils import words_parsing, googlemaps_api, mediawiki_api, gp_sentences
from .starter import app
import json



@app.route('/')
@app.route('/index/')
def index():
	"""Main page of the web app"""
	return render_template('index.html', gmap_api_key=app.config['GOOGLE_JS_KEY']) # GOOGLE_JS_KEY to load google map

@app.route('/results/') #methods=['GET']
def results():
	"""Route called to get a response from GrandPyBot, return a json object"""

	#Get the query
	query = request.args.get('query')
	
	#parse the query to keep the keywords (an address)
	query_parser = words_parsing.Parser(query)

	#create an object to call the google map geocoding API
	google_Api_Object = googlemaps_api.GoogleApi(query_parser.query_keywords)

	#create an object to have a random answer from GrandPy
	Gp_answers = gp_sentences.Gp_answers()

	if google_Api_Object.gmap_address(google_Api_Object.query_keywords) is True:# if the reponse from Googlemap is ok

		#create variables to send it back to the client
		address_value = google_Api_Object.address
		longitude = google_Api_Object.longitude
		latitude = google_Api_Object.latitude

		#create an object to call Mediawiki API
		wiki_Api_Object = mediawiki_api.MediaWiki(latitude, longitude, query_parser.query_keywords_list)
		

		if wiki_Api_Object.sentences_return() is True: # if the reponse from Mediawiki is ok

			#create variables to send it back to the client
			wiki_result = wiki_Api_Object.wiki_search
			wiki_id = wiki_Api_Object.page_ids

			#create json response
			response = json.dumps({"response": {"Gp_answer_gmap": Gp_answers.show_geo_answer(),"Gp_answer_wiki": Gp_answers.show_wiki_answer(), "gmap": address_value, "wiki": wiki_result, "wiki_id": wiki_id, "latitude": latitude, "longitude": longitude}})
			
			# if everything is good
			return response  # return json

		else:
			response = json.dumps({"response": {"Gp_answer_gmap": Gp_answers.show_geo_answer(), "Gp_answer_wiki": Gp_answers.show_wiki_noresults_answer(), "gmap": address_value, "wiki": "ZERO_RESULT", "latitude": latitude, "longitude": longitude}})
			
			# if no results from Wikipedia
			return response
	else:

		# if no results at all
		return json.dumps({"response": {"gmap": "ZERO_RESULT", "wiki": "ZERO_RESULT", "Gp_answer": Gp_answers.show_geo_noresults_answer()}})