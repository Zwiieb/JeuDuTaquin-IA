import random


class Taquin:
	# constructeur
	def __init__(self, nb):
		self.nb = nb
		self.__plateau = []
		self.__actions = ""
		
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
		
		self.__bingo = False
		
		self.__heuristique = self.heuristique_plateau()
	
	# surcharge d'opérateurs
	def __lt__(self, other):
		return self.__heuristique < other.__heuristique
	
	def __gt__(self, other):
		return self.__heuristique > other.__heuristique
	
	def __le__(self, other):
		return self.__heuristique <= other.__heuristique
	
	def __ge__(self, other):
		return self.__heuristique >= other.__heuristique
	
	def __eq__(self, other):
		return self.__plateau == other.__plateau and self.__heuristique == other.__heuristique and \
			   self.__actions == other.__actions and self.__bingo == other.__bingo
	
	def __ne__(self, other):
		return not self.__plateau != other.__plateau and not self.__heuristique != other.__heuristique and \
			   self.__actions != other.__actions and not self.__bingo != other.__bingo
	
	# --------------------------------------------
	# méthodes
	# --------------------------------------------
	
	# --------------------------------------------
	# fonction qui mélange le plateau et ne sauvegarde pas les mouvements
	# --------------------------------------------
	def creer_hasard(self):
		# melange le plateau
		self.shuffle_plateau(False)
	
	def placement(self, plateau):
		self.__plateau = plateau.copy()
	
	# --------------------------------------------
	# fonction qui recalcul l'heuristique
	# --------------------------------------------
	def recalcule_heuristique(self):
		self.__heuristique = self.heuristique_plateau()
	
	# --------------------------------------------
	# fonction qui compare si les taquins sont egaux
	# --------------------------------------------
	def est_egal(self, autre_taquin):
		return self.__plateau == autre_taquin.__plateau
	
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
			print("heuristique de la case ", valeur, ":", abs(x_cible - x) + abs(y_cible - y))
		
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
		heuristique += len(self.__actions)
		return heuristique
	
	# --------------------------------------------
	# fonction qui créée le plateau de jeu
	# --------------------------------------------
	def shuffle_plateau(self, flag):
		# le flag sert à ne pas enregister les mouvements
		# dans le taquin
		liste_actions = []
		liste_actions_possible = ['h', 'b', 'g', 'd']
		for _ in range(random.randint(1000, 10000)):
			i = random.randint(0, 3)
			liste_actions.append(liste_actions_possible[i])
		for i in liste_actions:
			self.mouvement[i](flag)
		self.recalcule_heuristique()
	
	# --------------------------------------------
	# fonction qui affiche le plateau du jeu actuel
	# --------------------------------------------
	def afficher_plateau(self):
		n = self.nb
		i = 0
		for _ in range(n):
			
			for _ in range(n):
				print("|", self.__plateau[i], end="")
				i += 1
			print("|")
	
	# --------------------------------------------
	# fonctions de mouvement
	# --------------------------------------------
	
	# fonction mouvement bas
	def mov_sud(self, flag, trace=0):
		n = self.nb
		i = 0
		trouve = False
		while i < len(self.__plateau) and not trouve and i < ((n * n) - n):
			if self.__plateau[i] == "x":
				self.__plateau[i], self.__plateau[i + n] = self.__plateau[i + n], self.__plateau[i]
				trouve = True
			i += 1
		if trace > 0 and not trouve:
			print("pas possible \n")
		if flag:
			self.__actions += 'S'
		self.recalcule_heuristique()
	
	# fonction mouvement haut
	def mov_nord(self, flag, trace=0):
		n = self.nb
		i = n
		trouve = False
		while i < len(self.__plateau) and not trouve:
			if self.__plateau[i] == "x":
				self.__plateau[i], self.__plateau[i - n] = self.__plateau[i - n], self.__plateau[i]
				trouve = True
			i += 1
		if trace > 0 and not trouve:
			print("pas possible \n")
		if flag:
			self.__actions += 'N'
		self.recalcule_heuristique()
	
	# fonction mouvement droite
	def mov_est(self, flag, trace=0):
		n = self.nb
		i = 0
		trouve = False
		
		while i < len(self.__plateau) and not trouve:
			if self.__plateau[i] == "x":
				if (i + 1) % n == 0:
					if trace > 0 and not trouve:
						print("pas possible \n")
					trouve = True
				else:
					self.__plateau[i], self.__plateau[i + 1] = self.__plateau[i + 1], self.__plateau[i]
					trouve = True
			i += 1
		if trace > 0 and not trouve:
			print("pas possible \n")
		if flag:
			self.__actions += 'E'
		self.recalcule_heuristique()
	
	# fonction mouvement gauche
	def mov_ouest(self, flag, trace=0):
		n = self.nb
		i = 0
		trouve = False
		
		while i < len(self.__plateau) and not trouve:
			if self.__plateau[i] == "x":
				if (i + 1) % n == 1:
					if trace > 0 and not trouve:
						print("pas possible \n")
					trouve = True
				else:
					self.__plateau[i], self.__plateau[i - 1] = self.__plateau[i - 1], self.__plateau[i]
					trouve = True
			i += 1
		if trace > 0 and not trouve:
			print("pas possible \n")
		if flag:
			self.__actions += 'O'
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
	def check(self, trace=0):
		if self.__plateau == self.etat_cible:
			# la solution est trouvée
			self.__bingo = True
			print("BINGO !")
		if trace > 0:
			print("test fait !")
	
	def jeu(self):
		self.afficher_plateau()
		self.deplacements_possibles()
		while not self.__bingo:
			print("Haut :   h")
			print("Bas :    b")
			print("Gauche : g")
			print("Droite : d")
			print("Fin : 0")
			choix = input("Quel est votre choix ? ")
			# pour ne pas crash quand l'utilisateur n'entre pas une valeur voulue
			if choix not in ['h', 'b', 'd', 'g', '0']:
				self.jeu()
			self.mouvement[choix](True)
			self.check()
			self.afficher_plateau()
		
		print("Réussie !!!!")
	
	# --------------------------------------------
	# fonction qui affiche les coups possible
	# --------------------------------------------
	
	def deplacements_possibles(self, trace=0):
		# variables 
		n = self.nb
		i = 0
		deplacements_possibles = []
		
		# code
		while i < len(self.__plateau):
			# recherche si on peut bouger x vers le haut
			if self.__plateau[i] == "x" and i >= n:
				deplacements_possibles.append('H')
			# recherche si on peut bouger x vers la gauche
			if self.__plateau[i] == "x":
				if (i + 1) % n != 1:
					deplacements_possibles.append('G')
			# recherche si on peut bouger x vers la droite
			if self.__plateau[i] == "x":
				if (i + 1) % n != 0:
					deplacements_possibles.append('D')
			# recherche si on peut bouger x vers le sud
			if self.__plateau[i] == "x" and i < (n * n) - n:
				deplacements_possibles.append('B')
			# incrémentation de l'indice i
			i += 1
		if trace > 0:
			print("les coups possibles sont : ", deplacements_possibles)
		return deplacements_possibles
	
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
