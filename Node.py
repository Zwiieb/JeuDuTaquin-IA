class Node:
	# constructeur
	def __init__(self, valeur, pere=None):
		# la valeur stockée
		self.__valeur = valeur
		
		# les liens avec les noeuds
		# lien avec le noeud père
		self.__pere = pere
		
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
	
	def search(self, valeur, trace=0):
		# par défaut, on n'a pas trouvé la valeur
		trouve = False
		
		# gestion de la trace pour lde debug
		if trace >= 1:
			print("\nvaleur recherchée : ", valeur)
			print("valeur noeud      : ", self.__valeur)
		
		if valeur == self.__valeur:
			if trace >= 1:
				print("Valeur trouvée !")
			trouve = True
		elif valeur < self.__valeur:
			if self.__gauche:
				trouve = self.__gauche.search(valeur, trace)
		elif self.__droite:
			trouve = self.__droite.search(valeur, trace)
		return trouve
	
	# --------------------------------------------
	# Fonction d'insertion
	# fonction qui ajoute un noeud
	# --------------------------------------------
	def insert(self, valeur, trace=0):
		retour = self
		if trace >= 1:
			print("valeur à insérer :", valeur)
			print("Valeur du noeud  : ", self.__valeur, "\n")
		
		# test valeur en ajout et valeur du noeud
		if valeur < self.__valeur:
			# s'il n'y a pas de noeud à gauche on en créer un
			if self.__gauche is None:
				self.__gauche = Node(valeur, self.__pere)
			else:
				# on navigue vers le noeud de gauche
				self.__gauche = self.__gauche.insert(valeur, trace)
		# test valeur du noeud et valeur en ajout
		elif valeur > self.__valeur:
			# s'il n'y a pas de noeud à droite on en créer un
			if self.__droite is None:
				self.__droite = Node(valeur, self.__droite)
			else:
				# on navigue vers le noeud de droite
				self.__droite = self.__droite.insert(valeur, trace)
		
		# equilibrate ?
		if self.__droite:
			poids_droite = self.__droite.profondeur_max() + 1
		else:
			poids_droite = 0
		
		if self.__gauche:
			poids_gauche = self.__gauche.profondeur_max() + 1
		else:
			poids_gauche = 0
		
		if trace >= 1:
			print("Valeur du noeud : ", self.__valeur)
			print("Poids gauche = ", poids_droite)
			print("Poids droit  = ", poids_gauche)
		
		# regarde si les branches ont un écart supérieur à 1
		if poids_droite > poids_gauche + 1:
			if trace >= 1:
				print("Déséquilibré => rotation gauche")
			retour = self.rot_gauche()
		
		elif poids_droite + 1 < poids_gauche:
			if trace >= 1:
				print("Déséquilibre => rotation droite")
			retour = self.rot_droite()
		
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
		if self.__droite:
			self.__droite.affiche(etage + 1)
		print(f"{' ' * 4 * etage}{self.__valeur}")
		if self.__gauche:
			self.__gauche.affiche(etage + 1)
	
	# --------------------------------------------
	# fonction qui affiche le noeud dans la console
	# --------------------------------------------
	def affiche_noeud(self):
		print(self.__valeur)
	
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
	
	def get_valeur(self):
		return self.__valeur
	
	def set_valeur(self, x):
		self.__valeur = x
	
	def get_pere(self):
		return self.__pere
	
	def set_pere(self, x):
		self.__pere = x
