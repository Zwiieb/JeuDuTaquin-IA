import random
import time
from copy import deepcopy

import Resolution


class Taquin:
	# constructeur
	def __init__(self, nb, etat_initial=None):
		# largeur du taquin
		self.nb = nb
		
		# sauvegarde de l'état initial
		if etat_initial is None:
			self.__etat_initial = deepcopy(self)
		
		# variable qui stock la disposition du plateau
		self.__plateau = []
		
		# chaine de caractère qui stock les movement fait pour arriver à ce taquin
		self.__actions = ""
		
		# variable qui va stocker le timing du début d'exécution du programme
		self.start = None
		
		# dictionnaire de mouvement
		self.mouvement = {'h': self.mov_nord,
						  'g': self.mov_ouest,
						  'd': self.mov_est,
						  'b': self.mov_sud,
						  '0': quit}
		
		# remplissage du plateau des cases qui vont le former
		for i in range(self.nb * self.nb - 1):
			self.__plateau.append(i)
		self.__plateau.append("x")
		
		# copie du tableau résolu dans une variable pour être le tableau cible
		self.etat_cible = self.__plateau.copy()
		
		# on mélange le plateau
		self.shuffle_plateau()
		
		# variable de fin de jeu
		self.__bingo = False
		
		# variable d'heuristique de plateau
		self.__heuristique = self.heuristique_plateau()
	
	# --------------------------------------------
	# surcharge d'opérateurs
	# --------------------------------------------
	def __lt__(self, autre_taquin):
		return self.__heuristique < autre_taquin.__heuristique
	
	def __gt__(self, autre_taquin):
		return self.__heuristique > autre_taquin.__heuristique
	
	def __le__(self, autre_taquin):
		return self.__heuristique <= autre_taquin.__heuristique
	
	def __ge__(self, autre_taquin):
		return self.__heuristique >= autre_taquin.__heuristique
	
	def __eq__(self, autre_taquin):
		return self.__plateau == autre_taquin.__plateau
	
	def __ne__(self, other):
		return not (self == other)
	
	# --------------------------------------------
	# méthodes
	# --------------------------------------------
	
	# --------------------------------------------
	# méthodes
	# --------------------------------------------
	def copy(self,autre_taquin):
		self.__etat_initial = autre_taquin.__etat_initial
		self.__plateau = autre_taquin.set_plateau()
		self.__actions = autre_taquin.set_actions()
		self.etat_cible = autre_taquin.etat_cible
	# --------------------------------------------
	# fonction qui recalcul l'heuristique
	# --------------------------------------------
	def recalcule_heuristique(self):
		self.__heuristique = self.heuristique_plateau()
	
	# --------------------------------------------
	# fonction qui calcul l'heuristique d'une case
	# --------------------------------------------
	def heuristique_case(self, valeur):
		# position actuel de la case
		x, y = self.cart(valeur)
		
		# position où elle doit être
		x_cible, y_cible = self.cart(valeur, self.etat_cible)
		
		#   heuristique du nombre
		return abs(x_cible - x) + abs(y_cible - y)
	
	# --------------------------------------------
	# fonction qui calcul l'heuristique d'une plateau
	# --------------------------------------------
	def heuristique_plateau(self):
		heuristique = 0
		
		# ajoute l'heuristique de chaque case
		for i in self.__plateau:
			heuristique += self.heuristique_case(i)
		
		# pour avoir la fonction d'évaluation : heuristique(mouvement théorique) + nombre de mouvement(réel)
		heuristique += len(self.__actions)
		
		return heuristique
	
	# --------------------------------------------
	# fonction qui mélange le plateau de jeu
	# --------------------------------------------
	def shuffle_plateau(self):
		liste_actions = []
		liste_actions_possible = ['h', 'b', 'g', 'd']
		for _ in range(random.randint(1000, 10000)):
			i = random.randint(0, 3)
			liste_actions.append(liste_actions_possible[i])
		for i in liste_actions:
			# le False indique que le taquin n'enregistre pas les déplacements dans 'actions'
			self.mouvement[i](False)
		self.recalcule_heuristique()
	
	# --------------------------------------------
	# fonction qui affiche le plateau du jeu actuel
	# --------------------------------------------
	def afficher_plateau(self):
		n = self.nb
		i = 0
		print("-" * 10)
		for _ in range(n):
			for _ in range(n):
				print("|", self.__plateau[i], end="")
				i += 1
			print("|")
		print("-" * 10)
	
	# --------------------------------------------
	# fonctions de mouvement
	# --------------------------------------------
	
	# fonction mouvement bas
	def mov_sud(self, flag):
		n = self.nb
		i = 0
		trouve = False
		while i < len(self.__plateau) and not trouve and i < ((n * n) - n):
			if self.__plateau[i] == "x":
				self.__plateau[i], self.__plateau[i + n] = self.__plateau[i + n], self.__plateau[i]
				trouve = True
			i += 1
		if flag:
			self.__actions += 'b'
		self.recalcule_heuristique()
	
	# fonction mouvement haut
	def mov_nord(self, flag):
		n = self.nb
		i = n
		trouve = False
		while i < len(self.__plateau) and not trouve:
			if self.__plateau[i] == "x":
				self.__plateau[i], self.__plateau[i - n] = self.__plateau[i - n], self.__plateau[i]
				trouve = True
			i += 1
		if flag:
			self.__actions += 'h'
		self.recalcule_heuristique()
	
	# fonction mouvement droite
	def mov_est(self, flag):
		n = self.nb
		i = 0
		trouve = False
		
		while i < len(self.__plateau) and not trouve:
			if self.__plateau[i] == "x":
				if (i + 1) % n == 0:
					trouve = True
				else:
					self.__plateau[i], self.__plateau[i + 1] = self.__plateau[i + 1], self.__plateau[i]
					trouve = True
			i += 1
		if flag:
			self.__actions += 'd'
		self.recalcule_heuristique()
	
	# fonction mouvement gauche
	def mov_ouest(self, flag):
		n = self.nb
		i = 0
		trouve = False
		
		while i < len(self.__plateau) and not trouve:
			if self.__plateau[i] == "x":
				if (i + 1) % n == 1:
					trouve = True
				else:
					self.__plateau[i], self.__plateau[i - 1] = self.__plateau[i - 1], self.__plateau[i]
					trouve = True
			i += 1
		if flag:
			self.__actions += 'g'
		self.recalcule_heuristique()
	
	# --------------------------------------------
	#   fonction qui donne les coordonnées cartésiennes du nombre
	# --------------------------------------------
	def cart(self, valeur, liste=None):
		if liste is None:
			liste = []
		if not liste:
			liste = self.__plateau
		x = 0
		y = 0
		# indice de la case recherchée
		indice = 0
		while liste[indice] != valeur:
			indice = indice + 1
		# calcul la coordonnée y
		while indice >= self.nb:
			indice = indice - self.nb
			y = y + 1
		# calcul la coordonnée x
		while indice > 0:
			indice = indice - 1
			x = x + 1
		return x, y
	
	# --------------------------------------------
	# fonction qui vérifie si le plateau est en état de solution
	# --------------------------------------------
	def check(self):
		if self.__plateau == self.etat_cible:
			# la solution est trouvée
			self.__bingo = True
			print("BINGO !")
	
	# --------------------------------------------
	# permet de rejouer la resolution d'un taquin
	# --------------------------------------------
	def rejoue(self, actions):
		for a in actions:
			self.mouvement[a](False)
			self.afficher_plateau()
			print()
	
	# --------------------------------------------
	# fonction qui affiche les coups possible
	# --------------------------------------------
	
	def deplacements_possibles(self):
		# variables 
		n = self.nb
		i = 0
		deplacements_possibles = []
		
		# code
		while i < len(self.__plateau):
			# recherche si on peut bouger x vers le haut
			if self.__plateau[i] == "x" and i >= n:
				deplacements_possibles.append('h')
			# recherche si on peut bouger x vers la gauche
			if self.__plateau[i] == "x":
				if (i + 1) % n != 1:
					deplacements_possibles.append('g')
			# recherche si on peut bouger x vers la droite
			if self.__plateau[i] == "x":
				if (i + 1) % n != 0:
					deplacements_possibles.append('d')
			# recherche si on peut bouger x vers le sud
			if self.__plateau[i] == "x" and i < (n * n) - n:
				deplacements_possibles.append('b')
			# incrémentation de l'indice i
			i += 1
		return deplacements_possibles
	
	# --------------------------------------------
	#   fonction qui permet de jouer au jeu manuellement
	# --------------------------------------------
	def jeu(self):
		if self.start is None:
			self.start = time.time()
		self.afficher_plateau()
		resolution_utilise = False
		while not self.__bingo:
			print("Haut :   h")
			print("Bas :    b")
			print("Gauche : g")
			print("Droite : d")
			print("Fin : 0")
			print("Resolution : R")
			choix = input("Quel est votre choix ? ")
			# pour ne pas crash quand l'utilisateur n'entre pas une valeur voulue
			if choix not in ['h', 'b', 'd', 'g', '0', 'R']:
				self.jeu()
			if choix == 'R':
				print(self.__etat_initial.afficher_plateau())
				r = Resolution.Resolution(self)
				r.resolution()
				self.__bingo = True
				resolution_utilise = True
			else:
				self.mouvement[choix](True)
				self.check()
				self.afficher_plateau()
		
		if not resolution_utilise:
			print("Temps mis pour finir le jeu:", time.time() - self.start, "secondes")
			print("Réussie !!!!")
	
	# --------------------------------------------
	#   Getter/Setter
	# --------------------------------------------
	def get_liste(self):
		return self.__plateau
	
	def get_heuristique(self):
		return self.__heuristique
	
	def get_actions(self):
		return self.__actions
	
	def get_plateau(self):
		return self.__plateau
	
	def get_etat_initial(self):
		return self.__etat_initial
	
	def set_etat_initial(self, etat_initial):
		self.__etat_initial = etat_initial
