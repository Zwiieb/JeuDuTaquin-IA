import random

"""
class Node:
	def __init__(self, etat, pere, actions, fils=[]):
		self.__etat = etat
		self.__pere = pere
		self.__actions = actions
		self.__fils = fils
		self.__heuristique = self.heuristique()

	def heuristique(self):
		return 1
"""


class Taquin:
	
	# --------------------------------------------
	# constructeur
	# --------------------------------------------
	def __init__(self, nb, trace=0):
		self.nb = nb
		self.liste = [0,1,2,3,4,5,6,"x",7]
		#self.liste = self.nouvelle_grille()
		self.trace = trace
		self.bingo = False

		#	initialisation de la solution recherchée
		self.solution = []
		for i in range((self.nb*self.nb)-1):
			self.solution.append(i)
		self.solution.append("x")
		
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
				
	#fonction mouvement bas
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
			
	#fonction mouvement haut
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
			
	#fonction mouvement droite
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
					
	#fonction mouvement gauche
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
	# fonction qui transforme la position dans nombre
	#	dans la liste en coordonnées cartésienness			
	# --------------------------------------------
	def cart(self, i):
		x = -1
		y = 0
		#calcul la coordonnée y
		while i > self.nb:
			i = i - self.nb
			y = y + 1
		#calcul la coordonnée x
		while i > 0:
			i = i - 1
			x = x + 1
		return(x,y)

	# --------------------------------------------
	# fonction qui vérifie si le plateau est en état de solution
	# --------------------------------------------
	def check(self,trace=0):
		if self.liste == self.solution :
			#la solution est trouvée
			self.bingo = True
			print("BINGO !")
		if trace > 0:	
			print("test fait !")
		