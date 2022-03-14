import random

"""
class Node:
	def __init__(self, etat, actions):
		# liste représentant l'état du jeu
		self.__etat = etat

		self.__actions = actions
		self.__fils_gauche = fils_gauche
		self.__fils_droit = fils_droit
		self.__heuristique = self.heuristique()

	def heuristique(self):
		return 1
"""


class Taquin:
	
	# --------------------------------------------
	# constructeur
	# --------------------------------------------
	def __init__(self, nb):
		self.nb = nb
		#self.liste = [0, 1, 2, 3, 4, 5, 6, "x", 7]
		self.liste = self.nouvelle_grille()
		self.bingo = False
		
		# initialisation de la solution recherchée
		self.solution = []
		for i in range((self.nb * self.nb) - 1):
			self.solution.append(i)
		self.solution.append("x")
	
	# --------------------------------------------
	# méthodes
	# --------------------------------------------
	
	# --------------------------------------------
	# fonction qui calcul l'heuristique d'une case
	# --------------------------------------------
	def heuristique_case(self, valeur, trace=0):
		heuristique_case = 0
		#	position actuel de la case
		x, y = self.cart(valeur)
		if trace > 0:
			print("x:", x, "y:", y)
		
		#	position où elle doit être
		x_cible, y_cible = self.cart(valeur, self.solution)
		if trace > 0:
			print("x:", x_cible, "y:", y_cible)
		
		#   heuristique du nombre
		return abs(x_cible - x) + abs(y_cible - y)

	# --------------------------------------------
	# fonction qui calcul l'heuristique d'une plateau
	# --------------------------------------------
	def heuristique_plateau(self):
		heuristique = 0
		
		# ajoute l'heuristique de chaque case
		for i in self.liste:
			heuristique += self.heuristique_case(i)
		return heuristique
	# --------------------------------------------
	# fonction qui créée le plateau de jeu
	# --------------------------------------------
	def nouvelle_grille(self):
		self.liste = []
		for i in range(self.nb * self.nb - 1):
			self.liste.append(i)
		self.liste.append("x")
		random.shuffle(self.liste)
		return self.liste
	
	# --------------------------------------------
	# fonction qui affiche le plateau du jeu actuel
	# --------------------------------------------
	def afficher_grille(self):
		n = self.nb
		i = 0
		for _ in range(n):
			
			for _ in range(n):
				print("|", self.liste[i], end=" ")
				i += 1
			print("|\n")
	
	# --------------------------------------------
	# fonctions de mouvement
	# --------------------------------------------
	
	# fonction mouvement bas
	def mov_sud(self):
		n = self.nb
		i = 0
		trouve = False
		while i < len(self.liste) and not trouve and i < ((n * n) - n):
			if self.liste[i] == "x":
				self.liste[i], self.liste[i + n] = self.liste[i + n], self.liste[i]
				trouve = True
			i += 1
		if self.trace > 0 and not trouve:
			print("pas possible \n")
	
	# fonction mouvement haut
	def mov_nord(self):
		n = self.nb
		i = n
		trouve = False
		while i < len(self.liste) and not trouve:
			if self.liste[i] == "x":
				self.liste[i], self.liste[i - n] = self.liste[i - n], self.liste[i]
				trouve = True
			i += 1
		if self.trace > 0 and not trouve:
			print("pas possible \n")
	
	# fonction mouvement droite
	def mov_est(self):
		n = self.nb
		i = 0
		trouve = False
		
		while i < len(self.liste) and not trouve:
			if self.liste[i] == "x":
				if (i + 1) % n == 0:
					print("pas possible \n")
					trouve = True
				else:
					self.liste[i], self.liste[i + 1] = self.liste[i + 1], self.liste[i]
					trouve = True
			i += 1
	
	# fonction mouvement gauche
	def mov_ouest(self):
		n = self.nb
		i = 0
		trouve = False
		
		while i < len(self.liste) and not trouve:
			if self.liste[i] == "x":
				if (i + 1) % n == 1:
					print("pas possible \n")
					trouve = True
				else:
					self.liste[i], self.liste[i - 1] = self.liste[i - 1], self.liste[i]
					trouve = True
			i += 1
	
	# --------------------------------------------
	#   fonction qui donne les coordonnées cartésiennes du nombre
	# --------------------------------------------
	def cart(self, valeur,liste=[]):
		if liste ==[]:
					liste = self.liste
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
	def check(self, trace=0):
		if self.liste == self.solution:
			# la solution est trouvée
			self.bingo = True
			print("BINGO !")
		if trace > 0:
			print("test fait !")
	
	def jeu(self):
		self.afficher_grille()
		while not self.bingo:
			choix = input("Quel est votre choix ? ")
			if choix == "haut":
				self.mov_nord()
				self.afficher_grille()
				self.check()
			if choix == "bas":
				self.mov_sud()
				self.afficher_grille()
				self.check()
			if choix == "gauche":
				self.mov_ouest()
				self.afficher_grille()
				self.check()
			if choix == "droite":
				self.mov_est()
				self.afficher_grille()
				self.check()
		
		print("Réussie !!!!")
