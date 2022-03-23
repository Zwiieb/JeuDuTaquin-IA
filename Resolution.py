import Node


class Resolution:
	# constructeur
	def __init__(self,taquin):
		self.__taquin = taquin
	
	# --------------------------------------------
	# méthodes
	# --------------------------------------------
	
	# penser a somme h et len(actions)
	def resolution(self):
		trouve = False
		# création de l'arbre binaire de recherche (abr)
		abr = Node.Node(self.taquin)
		while not trouve:
			pass