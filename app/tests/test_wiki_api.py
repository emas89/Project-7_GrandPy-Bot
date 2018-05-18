""" TESTING MEDIAWIKI API """

from ..utils.mediawiki_api import MediaWiki # import of test's target class
import urllib.request # import urllib for request/response simulation
from .. import app
from io import BytesIO # to create an object where it will be possible call the read() method
import json

class TestWikiApi:
	""" Test class creation """

	def setup_method(self, test_wikitext):
		""" setup_method function called during the TestWikiApi class test """
		self.wiki_Api_Object = MediaWiki(48.8747578, 2.350564700000001, ['openclarooms', 'Paris'])

	def test_wikitext(self, monkeypatch):
		""" WikiMedia service test with monkeypatch helper:
	        a request to MediaWiki API is simulated, a response
	        in json format is expected
	    """

	    # open in read mode the json file with WikiMedia API data
		with open("mediawiki_api_data.json", "r") as f:
			self.returned_data = json.load(f)
			self.returned_dumps = json.dumps(self.returned_data)

		# BytesIO class utilisation
		def mockreturn(request):
			return BytesIO(self.returned_dumps.encode())

		# monkeypatch.setattr() method to change the returned value
		monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

		# expected returned values
		assert self.wiki_Api_Object.sentences_return() is True
		assert self.wiki_Api_Object.page_ids == 4338589