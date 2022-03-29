import time
from copy import deepcopy

import Node


class Resolution:
	# constructeur
	def __init__(self, taquin):
		# le jeu de taquin qu'on va résoudre
		self.__taquin = taquin
		# arbre binaire de recherche pour trier les taquins pas encore analysés
		self.__non_visite = Node.Node(taquin)
		# liste des états de taquins déjà analysés
		self.__visite = []
		
		# nombre de noeuds
		self.nb_noeuds = 1
	
	# --------------------------------------------
	# méthodes
	# --------------------------------------------
	
	# --------------------------------------------
	# méthode coeur de la résolution
	# --------------------------------------------
	def resolution(self):
		# pour calculer le temps d'exécution
		debut = time.process_time()
		# variable qui stock le nombre d'états analysés avant de trouver la solution
		nb_evaluation = 0
		trouve = False
		
		while not trouve:
			# recuperation du noeud avec la plus petite valeur
			taquin_min = self.__non_visite.donne_min()
			# incrémentation du nombre d'états testés
			nb_evaluation += 1
			
			if nb_evaluation % 1000 == 0:
				print("Calcul en cours, ", nb_evaluation,"états analysés")
			
			# on l'a trouvé
			if taquin_min.get_plateau() == self.__taquin.etat_cible:
				trouve = True
			# ou pas
			else:
				# envisage tous les coups possibles
				coups_possibles = taquin_min.deplacements_possibles()
				# pour tous les coups possibles
				for i in coups_possibles:
					# création d'une copie du taquin pour ne pas le modifier
					taquin_temp = deepcopy(taquin_min)
					taquin_temp.set_etat_initial(taquin_min.get_etat_initial())
					
					# ajoute le noeud en analyse dans les noeuds visités
					self.__visite.append(taquin_min)
					taquin_temp.mouvement[i](True)
					
					# si taquin_temp n'a pas deja été visité
					if not self.deja_vu(taquin_temp):
						# on l'ajoute a l'arbre binaire
						self.__non_visite = self.__non_visite.inserer(taquin_temp)
						# on incrémente le nombre de noeuds
						self.nb_noeuds += 1
				
				# suppression du taquin analysé de l'abr des taquins non visités
				self.__non_visite, _ = self.__non_visite.supprime(taquin_min)
		
		# variable qui stock le temps de la fin du programme
		fin = time.process_time()
		print("fin!! \n les mouvements sont :", taquin_min.get_actions().upper())
		print("La solution a été trouve en ", nb_evaluation, " evaluations,")
		print("en",len(taquin_min.get_actions()),"actions,")
		print("et en :", fin - debut, 'secondes')
		return taquin_min, nb_evaluation, fin - debut
	
	# --------------------------------------------
	# méthode qui détermine si on a déjà analysé le taquin
	# --------------------------------------------
	def deja_vu(self, taquin):
		retour = False
		i = 0
		while i < len(self.__visite) and not retour:
			retour = taquin == self.__visite[i]
			i += 1
		return retour
