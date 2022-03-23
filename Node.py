import Taquin


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
	def inserer(self, taquin, trace=0):
		retour = self
		# heuristique du noeud en cours d'ajout
		h_en_ajout = taquin.get_heuristique()
		# heuristique du noeud en cours d'analyse
		h_analyse = self.__etat.get_heuristique()
		if trace >= 1:
			print("valeur à insérer :", h_en_ajout)
			print("Valeur du noeud  : ", h_analyse, "\n")
		
		# test valeur en ajout et valeur du noeud
		if h_en_ajout <= h_analyse:
			# s'il n'y a pas de noeud à gauche on en créer un
			if not self.__gauche:
				if trace > 0:
					print("on créer a gauche")
				self.__gauche = Node(taquin)
			else:
				# on navigue vers le noeud de gauche
				if trace > 0:
					print("on navigue a gauche")
				self.__gauche = self.__gauche.inserer(taquin, trace)
		# test valeur du noeud et valeur en ajout
		elif h_en_ajout > h_analyse:
			# s'il n'y a pas de noeud à droite on en créer un
			if not self.__droite:
				if trace > 0:
					print("on créer a droite le noeud:", h_en_ajout)
				self.__droite = Node(taquin)
			else:
				if trace > 0:
					print("on navigue a droite")
				# on navigue vers le noeud de droite
				self.__droite = self.__droite.inserer(taquin)
		
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
			print("Valeur du noeud : ", self.__etat.get_heuristique())
			print("Poids droit  = ", poids_droite)
			print("Poids gauche = ", poids_gauche)
		
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
	# Fonction qui retourne la valeur la plus petite de l'arbre
	# --------------------------------------------
	def donne_min(self):
		retour = self.__etat.get_heuristique()
		if self.__gauche:
			retour = self.__gauche.donne_min()
		return retour
	
	# --------------------------------------------
	# Fonction qui supprime une valeur de l'arbre
	# --------------------------------------------
	def supprime(self, valeur, trace=0):
		retour = self
		if valeur < self.__valeur:
			self.__gauche = self.__gauche.supprime(valeur, trace)
		elif valeur > self.__valeur:
			self.__droite = self.__droite.supprime(valeur, trace)
		else:
			# cas 1 : c'est une feuille !
			if self.__gauche is None and self.__droite is None:
				retour = None
			# cas 2 : le noeud possède qu'une seule feuille
			elif self.__gauche is None:
				retour = self.__droite
			elif self.__droite is None:
				retour = self.__gauche
			else:
				# cas 3 : il y a des valeurs à droite et à gauche !
				valeur_min = self.__droite.donne_min()
				self.__valeur = valeur_min
				self.__droite = self.__droite.supprime(valeur_min, trace)
		
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
		print(f"{' ' * 4 * etage}{self.__etat.get_heuristique()}")
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
