from copy import deepcopy

import Node


class Resolution:
	# constructeur
	def __init__(self, taquin):
		self.__taquin = taquin
		self.__non_visite = Node.Node(taquin)
		self.__visite = []
		
		# nombre de noeuds
		self.nb_noeuds = 1
	
	# --------------------------------------------
	# méthodes
	# --------------------------------------------
	
	# penser a somme h et len(actions)
	def resolution(self):
		nb = 0
		trouve = False
		
		while not trouve:
			# recuperation du noeud avec la plus petite valeur
			taquin_min = self.__non_visite.donne_min()
			nb += 1
			
			print("Plateau envisagé ", nb, " : ")
			taquin_min.afficher_plateau()
			print("Arbre : ")
			self.__non_visite.affiche()
			print("Taquin => ", taquin_min)
			input()
			
			if taquin_min.get_plateau() == self.__taquin.etat_cible:
				# print("deja vu !")
				trouve = True
			else:
				# envisage tous les coups possibles
				coups_possibles = taquin_min.deplacements_possibles()
				# pour tous les coups possibles
				for i in coups_possibles:
					# création d'une copie du taquin pour ne pas le modifier
					taquin_temp = deepcopy(taquin_min)
					# ajoute le noeud en analyse dans les noeuds visités
					self.__visite.append(taquin_min)
					taquin_temp.mouvement[i.lower()](True)
					# si taquin_temp n'a pas deja été visité
					if not self.deja_vu(taquin_temp):
						# on l'ajoute a l'arbre binaire
						self.__non_visite = self.__non_visite.inserer(taquin_temp)
						# on incrémente le nombre de noeuds
						self.nb_noeuds += 1
				print("Arbre  avant suppression : ")
				self.__non_visite.affiche()
				self.__non_visite = self.__non_visite.supprime(taquin_min, 1)
				print("Arbre  après suppression : ")
				self.__non_visite.affiche()
		print("fin!! \n les mouvements sont :", taquin_min.get_actions(), " en ", nb, " evaluations")
		return taquin_min
	
	def deja_vu(self, taquin):
		retour = False
		i = 0
		while i < len(self.__visite) and not retour:
			retour = taquin.est_egal(self.__visite[i])
			i += 1
		return retour
