import random


class Taquin:
	
	# --------------------------------------------
	# constructeur
	# --------------------------------------------
	def __init__(self, __nb):
		self.nb = __nb
		# self.liste = [0, 1, 2, 3, 4, 5, 6, "x", 7]
		self.__liste = self.nouveau_plateau()
		self.__bingo = False
		
		# initialisation de la solution recherchée
		self.etat_cible = []
		for i in range((self.nb * self.nb) - 1):
			self.etat_cible.append(i)
		self.etat_cible.append("x")
		
		self.__heuristique = self.heuristique_plateau()
	
	# --------------------------------------------
	# méthodes
	# --------------------------------------------
	
	# --------------------------------------------
	# fonction qui calcul l'heuristique d'une case
	# --------------------------------------------
	def heuristique_case(self, valeur, trace=0):
		# position actuel de la case
		x, y = self.cart(valeur)
		if trace > 0:
			print("x:", x, "y:", y)
		
		# position où elle doit être
		x_cible, y_cible = self.cart(valeur, self.etat_cible)
		if trace > 0:
			print("x_cible:", x_cible, "y_cible:", y_cible)
			print("heuristique de la case ",valeur,":",abs(x_cible - x) + abs(y_cible - y))
		
		#   heuristique du nombre
		return abs(x_cible - x) + abs(y_cible - y)
	
	# --------------------------------------------
	# fonction qui calcul l'heuristique d'une plateau
	# --------------------------------------------
	def heuristique_plateau(self):
		heuristique = 0
		
		# ajoute l'heuristique de chaque case
		for i in self.__liste:
			heuristique += self.heuristique_case(i)
		return heuristique
	
	# --------------------------------------------
	# fonction qui créée le plateau de jeu
	# --------------------------------------------
	def nouveau_plateau(self):
		self.__liste = []
		for i in range(self.nb * self.nb - 1):
			self.__liste.append(i)
		self.__liste.append("x")
		random.shuffle(self.__liste)
		return self.__liste
	
	# --------------------------------------------
	# fonction qui affiche le plateau du jeu actuel
	# --------------------------------------------
	def afficher_plateau(self):
		n = self.nb
		i = 0
		for _ in range(n):
			
			for _ in range(n):
				print("|", self.__liste[i], end=" ")
				i += 1
			print("|\n")
	
	# --------------------------------------------
	# fonctions de mouvement
	# --------------------------------------------
	
	# fonction mouvement bas
	def mov_sud(self, trace=0):
		n = self.nb
		i = 0
		trouve = False
		while i < len(self.__liste) and not trouve and i < ((n * n) - n):
			if self.__liste[i] == "x":
				self.__liste[i], self.__liste[i + n] = self.__liste[i + n], self.__liste[i]
				trouve = True
			i += 1
		if trace > 0 and not trouve:
			print("pas possible \n")
	
	# fonction mouvement haut
	def mov_nord(self, trace=0):
		n = self.nb
		i = n
		trouve = False
		while i < len(self.__liste) and not trouve:
			if self.__liste[i] == "x":
				self.__liste[i], self.__liste[i - n] = self.__liste[i - n], self.__liste[i]
				trouve = True
			i += 1
		if trace > 0 and not trouve:
			print("pas possible \n")
	
	# fonction mouvement droite
	def mov_est(self):
		n = self.nb
		i = 0
		trouve = False
		
		while i < len(self.__liste) and not trouve:
			if self.__liste[i] == "x":
				if (i + 1) % n == 0:
					print("pas possible \n")
					trouve = True
				else:
					self.__liste[i], self.__liste[i + 1] = self.__liste[i + 1], self.__liste[i]
					trouve = True
			i += 1
	
	# fonction mouvement gauche
	def mov_ouest(self):
		n = self.nb
		i = 0
		trouve = False
		
		while i < len(self.__liste) and not trouve:
			if self.__liste[i] == "x":
				if (i + 1) % n == 1:
					print("pas possible \n")
					trouve = True
				else:
					self.__liste[i], self.__liste[i - 1] = self.__liste[i - 1], self.__liste[i]
					trouve = True
			i += 1
	
	# --------------------------------------------
	#   fonction qui donne les coordonnées cartésiennes du nombre
	# --------------------------------------------
	def cart(self, valeur, liste=None):
		if liste is None:
			liste = []
		if not liste:
			liste = self.__liste
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
		if self.__liste == self.etat_cible:
			# la solution est trouvée
			self.__bingo = True
			print("BINGO !")
		if trace > 0:
			print("test fait !")
	
	def jeu(self):
		self.afficher_plateau()
		while not self.__bingo:
			choix = input("Quel est votre choix ? ")
			if choix == "haut":
				self.mov_nord()
				self.afficher_plateau()
				self.check()
			if choix == "bas":
				self.mov_sud()
				self.afficher_plateau()
				self.check()
			if choix == "gauche":
				self.mov_ouest()
				self.afficher_plateau()
				self.check()
			if choix == "droite":
				self.mov_est()
				self.afficher_plateau()
				self.check()
		
		print("Réussie !!!!")
	# --------------------------------------------
	#   Getter/Setter
	# --------------------------------------------
	def get_liste(self):
		return self.__liste
	def get_heuristique(self):
		return  self.__heuristique