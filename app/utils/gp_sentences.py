import random #to get a random answer

class Gp_answers:
	""" class that allows GrandPy Bot to get a random answer to users """
	
	def __init__(self):
		
		# answers about geography (gmaps)
		self.geo_answers = ["Bien sûr mon petit voyageur ! Voici ton adresse : ", "Ah, ce lieu me rappelle beaucoup de choses : ", "Je me souviens très bien de cette adresse : ", "J'étais encore jeune quand j'ai découvert cet endroit : "]
		# answers about place history (wiki)
		self.wiki_answers = ["J'ai un tas d'informations sur ce lieu !", "Et tu veux savoir une curiosité à propos de cette adresse ?", "Approche-toi, j'ai une histoire concernant ce lieu...", "Et si tu veux savoir une anecdote par rapport a ton adresse..."]
		# answer when no gmaps results
		self.geo_noresults_answer = "Est-ce que pourrais-tu me répéter ta question stp ? Tu sais, je suis vieux..."
		# answer when no wiki results
		self.wiki_noresults_answer = "C'est incroyable, je ne connais aucun endroit dans les alentours... Désolé"


	def show_geo_answer(self):
		# geography answer: it returns a random element from geo_answers list
		return self.geo_answers[random.randint(0, len(self.geo_answers)-1)]


	def show_wiki_answer(self):
		# wiki answer: it returns a random element from wiki_answers list
		return self.wiki_answers[random.randint(0, len(self.wiki_answers)-1)]


	def show_geo_noresults_answer(self):
		# answer if no geography results
		return self.geo_noresults_answer


	def show_wiki_noresults_answer(self):
		# answer if no wiki results
		return self.wiki_noresults_answer