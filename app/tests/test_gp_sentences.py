""" TESTING GRAND PY BOT SENTENCES """

from ..utils.gp_sentences import Gp_answers

class TestGp_answers:
	""" Test class creation """

	""" setup_method function called during the Gp_answers class test """
	def setup_method(self, test_gp_sentences):
		self.gp_sentences = Gp_answers()
		self.gp_sentences.geo_answers = ["Bien mon petit voyageur ! Voici ton adresse : "]
		self.gp_sentences.wiki_answers = ["J'ai un tas d'informations sur ce lieu !"]
		self.gp_sentences.geo_noresults_answer = "Est-ce que pourrais-tu me répéter ta question stp ? Tu sais, je suis vieux... &#9888"
		self.gp_sentences.wiki_noresults_answer = "C'est incroyable, je ne connais aucun endroit dans les alentours... Désolé &#9785"


	def test_gp_sentences(self):
		# expected returned values
		assert self.gp_sentences.show_geo_answer() == "Bien mon petit voyageur ! Voici ton adresse : "
		assert self.gp_sentences.show_wiki_answer() == "J'ai un tas d'informations sur ce lieu !"
		assert self.gp_sentences.show_geo_noresults_answer() == "Est-ce que pourrais-tu me répéter ta question stp ? Tu sais, je suis vieux... &#9888"
		assert self.gp_sentences.show_wiki_noresults_answer() == "C'est incroyable, je ne connais aucun endroit dans les alentours... Désolé &#9785"