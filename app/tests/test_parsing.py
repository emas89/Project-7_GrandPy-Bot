""" WORDS PARSING TEST """

from ..utils.words_parsing import Parser

class TestParser:
	""" testing class creation """

	def setup_method(self, test_parsing):
		# setup_method function to test word parsing
		query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		self.parser = Parser(query)


	def test_parsing(self):
		# expected returned data (only the key words are used in the research)
		assert self.parser.query_keywords == 'openclassrooms'
		assert self.parser.query_keywords_list == ['openclassrooms']