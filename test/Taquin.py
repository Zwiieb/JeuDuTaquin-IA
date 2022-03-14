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
	def __init__(self, nb, trace=0):
		self.nb = nb
		self.liste = self.nouvelle_grille()
		self.trace = trace
	
	def nouvelle_grille(self):
		
		self.liste = []
		for i in range(self.nb * self.nb - 1):
			self.liste.append(i)
		self.liste.append("x")
		random.shuffle(self.liste)
		return self.liste
	
	def afficher_grille(self):
		n = self.nb
		i = 0
		
		for _ in range(n):
			
			for _ in range(n):
				print("|", self.liste[i], end=" ")
				i += 1
			print("|\n")
	
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
	
	def mov_nord(self):
		n = self.nb
		i = 0
		trouve = False
		while i < len(self.liste) and not trouve:
			if self.liste[i] == "x":
				self.liste[i], self.liste[i - n] = self.liste[i - n], self.liste[i]
				trouve = True
			i += 1
	
	def mov_est(self):
		n = self.nb
		i = 0
		trouve = False
		
		while i < len(self.liste) and not trouve:
			if self.liste[i] == "x":
				self.liste[i], self.liste[i + 1] = self.liste[i + 1], self.liste[i]
				trouve = True
			i += 1
	
	def mov_ouest(self):
		n = self.nb
		i = 0
		trouve = False
		while i < len(self.liste) and not trouve:
			if self.liste[i] == "x":
				self.liste[i], self.liste[i - 1] = self.liste[i - 1], self.liste[i]
				trouve = True
			i += 1
