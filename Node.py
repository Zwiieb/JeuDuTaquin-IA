class Node:
	# constructeur
	def __init__(self, etat):
		# état actuel du plateau
		self.__etat = etat
		
		# Les deux noeuds fils
		# gauche => valeur plus petite
		self.__gauche = None
		# droite => valeur plus grande
		self.__droite = None
	
	# --------------------------------------------
	# méthodes
	# --------------------------------------------
	
	# --------------------------------------------
	# fonction qui cherche une valeur donnée dans l'arbre
	# --------------------------------------------
	def search(self, heuristique, trace=0):
		# par défaut, on n'a pas trouvé la valeur
		trouve = False
		
		# simplification de l'appellation de l'heuristique de l'état actuel
		valeur = self.__etat.get_heuristique()
		
		# gestion de la trace pour la console
		if trace > 0:
			print("\nvaleur recherchée :", heuristique)
			print("valeur en cours d'analyse :", self.__etat.get_heuristique())
		
		if heuristique == valeur:
			if trace > 0:
				print("Valeur trouvée !")
			trouve = True
		elif heuristique < valeur and self.__gauche:
			# on navigue dans la branche de gauche
			trouve = self.__gauche.search(heuristique, trace)
		elif self.__droite:
			# on navigue dans la branche de droite
			trouve = self.__droite.search(heuristique, trace)
		return trouve
	
	# --------------------------------------------
	# Fonction d'insertion
	# fonction qui ajoute un noeud
	# --------------------------------------------
	def inserer(self, valeur, trace=0):
		retour = self
		if trace >= 1:
			print("valeur à insérer :", valeur)
			print("Valeur du noeud  : ", self.__etat, "\n")
		
		# test valeur en ajout et valeur du noeud
		if valeur <= self.__etat:
			# s'il n'y a pas de noeud à gauche on en créer un
			if self.__gauche is None:
				self.__gauche = Node(valeur)
			else:
				# on navigue vers le noeud de gauche
				self.__gauche = self.__gauche.inserer(valeur, trace)
		# test valeur du noeud et valeur en ajout
		elif valeur > self.__etat:
			# s'il n'y a pas de noeud à droite on en créer un
			if self.__droite is None:
				self.__droite = Node(valeur)
			else:
				# on navigue vers le noeud de droite
				self.__droite = self.__droite.inserer(valeur, trace)
		
		# equilibrage ?
		if self.__droite:
			poids_right = self.__droite.profondeur_max() + 1
		else:
			poids_right = 0
		
		if self.__gauche:
			poids_left = self.__gauche.profondeur_max() + 1
		else:
			poids_left = 0
		
		if trace >= 1:
			print("Valeur du noeud : ", self.__etat)
			print("Poids gauche = ", poids_right)
			print("Poids droit  = ", poids_left)
		
		# regarde si les branches ont un écart supérieur à 1
		if poids_right > poids_left + 1:
			if trace >= 1:
				print("Déséquilibré => rotation gauche")
			retour = self.rot_gauche()
		
		elif poids_right + 1 < poids_left:
			if trace >= 1:
				print("Déséquilibre => rotation droite")
			retour = self.rot_droite()
		
		return retour
	
	# --------------------------------------------
	# Fonction qui retourne la valeur la plus petite de l'arbre
	# --------------------------------------------
	def donne_min(self):
		retour = self.__etat
		if self.__gauche != None:
			retour = self.__gauche.donne_min()
		return retour
	
	# --------------------------------------------
	# Fonction qui retourne la valeur la plus petite entre 2 taquins pour la fonction supprime
	# --------------------------------------------
	'''def plus_petit_que(self,autre_taquin):
		if self.__etat.get_heuristique() < autre_taquin.get_heuristique() and self.__etat.
	'''
	# --------------------------------------------
	# Fonction qui supprime une valeur de l'arbre
	# --------------------------------------------
	def supprime(self, valeur, trace=0):
		if trace > 0:
			print("Début de la méthode supprime, avec => ", valeur)
			print("On se trouve sur le noeud ", self)
		retour = self
		if valeur < self.__etat:
			if trace > 0:
				print("On part à gauche")
			self.__gauche = self.__gauche.supprime(valeur, trace)
		elif valeur > self.__etat:
			if trace > 0:
				print("On part à droite")
			self.__droite = self.__droite.supprime(valeur, trace)
		else:
			# On est sur le noeud qui possède la valeur a supprimer
			# Plusieurs cas possibles :
			# voir
			# https://www.delftstack.com/tutorial/data-structure/binary-search-tree-delete/
			
			# cas 1 : c'est une feuille !
			if trace > 0:
				print("On a trouvé ce que l'on cherche : ", self)
			if self.__gauche == None and self.__droite == None:
				if trace > 0:
					print("Pas d'enfants => on efface le noeud")
				retour = None
			# cas 2 : le noeud possède qu'une seule feuille
			elif self.__gauche == None:
				if trace > 0:
					print("Qu'une feuille à droite, on retourne=> ", self.__droite)
				retour = self.__droite
			elif self.__droite == None:
				if trace > 0:
					print("Qu'une feuille à gauche, on retourne=> ", self.__gauche)
				retour = self.__gauche
			else:
				# cas 3 : il y a des valeurs à droite et à gauche !
				if trace > 0:
					print("Deux feuilles")
				valeur_min = self.__droite.donne_min()
				if trace > 0:
					print("On cherche le min => ", valeur_min)
				self.__etat = valeur_min
				if trace > 0:
					print("On supprime la valeur min")
				self.__droite = self.__droite.supprime(valeur_min, trace)
		if trace > 0:
			print("Fin de la méthode supprime, on retourne=> ", retour)
		return retour
	
	# --------------------------------------------
	# Fonction qui retourne la valeur la plus petite de l'arbre
	# --------------------------------------------
	def donne_noeud_min(self):
		retour = self
		if self.__gauche != None:
			retour = self.__gauche.donne_min()
		return retour
	
	# --------------------------------------------
	# fonction qui test la branche la plus longue de l'abr
	# --------------------------------------------
	def profondeur_max(self):
		# attribution de 0 dans le cas ou il n'y a pas de fils
		poids_gauche = 0
		poids_droite = 0
		
		# récursivité pour compter le nombre de noeud de la branche la plus longue
		if self.__gauche:
			poids_gauche = (self.__gauche.profondeur_max() + 1)
		if self.__droite:
			poids_droite = (self.__droite.profondeur_max() + 1)
		
		# retourne la branche la plus longue entre celle de droite et celle de gauche
		return max(poids_droite, poids_gauche)
	
	# --------------------------------------------
	#   fonction de rotation d'arbre binaire à droite
	# --------------------------------------------
	def rot_droite(self, trace=0):
		if trace >= 1:
			print("\nRotation droite :")
			self.affiche_noeud()
		pivot = self.__gauche
		
		if trace >= 1:
			print("Le pivot : ", end="")
			pivot.affiche_noeud()
			
			print("Affichage du sous-arbre qui subit cette rotation :")
			self.affiche()
		
		# je vais avoir comme fils droit la gauche de mon fils droit
		self.__gauche = pivot.get_droite()
		# et mon fils droit va m'avoir comme fils gauche
		pivot.set_droite(self)
		
		if trace >= 1:
			print("\nRésultat de la rotation : ")
			pivot.affiche()
			print("Fin de la rotation \n")
		return pivot
	
	# --------------------------------------------
	#   fonction de rotation d'arbre binaire à gauche
	# --------------------------------------------
	def rot_gauche(self, trace=0):
		if trace >= 1:
			print("\nRotation gauche :")
			self.affiche_noeud()
		pivot = self.__droite
		
		if trace >= 1:
			print("Le pivot : ", end="")
			pivot.affiche_noeud()
			
			print("Affichage du sous-arbre qui subit cette rotation :")
			self.affiche()
		
		# je vais avoir comme fils droit la gauche de mon fils droit
		self.__droite = pivot.get_gauche()
		# et mon fils droit va m'avoir comme fils gauche
		pivot.set_gauche(self)
		
		if trace >= 1:
			print("\nRésultat de la rotation : ")
			pivot.affiche()
			print("Fin de la rotation \n")
		return pivot
	
	# --------------------------------------------
	# fonction qui affiche l'arbre dans la console
	# --------------------------------------------
	def affiche(self, etage=0):
		# on navigue à droite s'il existe
		if self.__droite:
			self.__droite.affiche(etage + 1)
		# on écrit laa valeur de l'heuristique du noeud
		print(' ' * 4 * etage, self.__etat.get_heuristique(), ": ", self.__etat, "/", self)
		# on navigue à gauche s'il existe
		if self.__gauche:
			self.__gauche.affiche(etage + 1)
	
	# --------------------------------------------
	# fonction qui affiche le noeud dans la console
	# --------------------------------------------
	def affiche_noeud(self):
		print(self.__etat.get_heuristique())
	
	# --------------------------------------------
	# getter / setter
	# --------------------------------------------
	def set_gauche(self, noeud):
		self.__gauche = noeud
	
	def get_gauche(self):
		return self.__gauche
	
	def set_droite(self, noeud):
		self.__droite = noeud
	
	def get_droite(self):
		return self.__droite
	
	def get_etat(self):
		return self.__etat
	
	def set_etat(self, x):
		self.__etat = x
