class Node:
	# constructeur
	def __init__(self, valeur, pere=None):
		# la valeur stockée
		self.__valeur = valeur

	# les liens avec les noeuds
		# lien avec le noeud père
		self.__pere = pere

	# Les deux noeuds fils
		# left => valeur plus petite
		self.__gauche = None
		# right => valeur plus grande
		self.__droite = None

	# --------------------------------------------
	# méthodes
	# --------------------------------------------

	# On recherche une valeur donnée dans l'arbre

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
				trouve = self.__gauche.search(valeur)
		elif self.__droite:
			trouve = self.__droite.search(valeur)
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
		# gestion des fils None
		if self.__droite:
			poids_right = self.__droite.weight() + 1
		else:
			poids_right = 0

		if self.__gauche:
			poids_left = self.__gauche.weight() + 1
		else:
			poids_left = 0

		if trace >= 1:
			print("Valeur du noeud : ", self.__valeur)
			print("Poids gauche = ", poids_right)
			print("Poids droit  = ", poids_left)

		if poids_right > poids_left + 1:
			if trace >= 1:
				print("Déséquilibré => rotation gauche")
			retour = self.rot_left()

		elif poids_right + 1 < poids_left:
			if trace >= 1:
				print("Déséquilibre => rotation droite")
			retour = self.rot_right()

		return retour

	# --------------------------------------------
	# trouve le noeud avec la valeur la plus pres du noeud actuel
	# --------------------------------------------
	def close_of(self):

		# plus petit de gauche
		plus_proche_gauche = None

		# cherche la valeur la plus grande existant dans la branche de gauche
		if self.__gauche:
			if self.__gauche.__droite:
				plus_proche_gauche = self.__gauche.__droite
				while plus_proche_gauche.__droite:
					plus_proche_gauche = plus_proche_gauche.__droite
			else:
				plus_proche_gauche = self.__gauche

		# plus petit de droite
		plus_proche_droite = None

		# cherche la valeur la plus petite existant dans la branche de droite
		if self.__droite:
			if self.__droite.__gauche:
				plus_proche_droite = self.__droite.__gauche
				while plus_proche_droite.__gauche:
					plus_proche_droite = plus_proche_droite.__gauche
			else:
				plus_proche_droite = self.__droite

		# plus petit du noeud self

		# s'il manque des valeurs
		if plus_proche_droite is None and plus_proche_gauche is None:
			print(" pas de fils et self est :", self, self.get_value())
			return self
		if plus_proche_droite is None:
			res = plus_proche_gauche
		elif plus_proche_gauche is None:
			res = plus_proche_droite

		# sinon on compare la différence entre les valeurs trouvées et le noeud de base
		elif abs(self.get_value() - plus_proche_droite.value) < abs(
				self.get_value()() - plus_proche_gauche.GetValue()()) or abs(
			self.get_value() - plus_proche_droite.value) == abs(self.get_value() - plus_proche_gauche.value):
			res = plus_proche_droite
		else:
			res = plus_proche_gauche

		# retour de la réponse
		print("res:", res)
		return res

	# --------------------------------------------
	# fonction qui test le poids(le nombre de fils) d'un noeud
	# --------------------------------------------
	def weight(self):
		res = 0
		if self.__gauche:
			res += (self.__gauche.weight() + 1)
		if self.__droite:
			res += (self.__droite.weight() + 1)
		return res

	# --------------------------------------------
	#   fonction de rotation d'arbre binaire à droite
	# --------------------------------------------
	def rot_right(self, trace=0):
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
		self.__gauche = pivot.get_right()
		# et mon fils droit va m'avoir comme fils gauche
		pivot.set_right(self)

		if trace >= 1:
			print("\nRésultat de la rotation : ")
			pivot.Affiche()
			print("Fin de la rotation \n")
		return pivot

	# --------------------------------------------
	#   fonction de rotation d'arbre binaire à gauche
	# --------------------------------------------
	def rot_left(self, trace=0):
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
		self.__droite = pivot.get_left()
		# et mon fils droit va m'avoir comme fils gauche
		pivot.set_left(self)

		if trace >= 1:
			print("\nRésultat de la rotation : ")
			pivot.Affiche()
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
	# fonction qui affiche l'arbre dans la console
	# --------------------------------------------
	def affiche_noeud(self):
		print(self.__valeur)

	# --------------------------------------------
	# getter / setter
	# --------------------------------------------
	def set_left(self, noeud):
		self.__gauche = noeud

	def get_left(self):
		return self.__gauche

	def set_right(self, noeud):
		self.__droite = noeud

	def get_right(self):
		return self.__droite

	def get_value(self):
		return self.__valeur

	def set_value(self, _x):
		self.__valeur = _x

	def get_parent(self):
		return self.__pere

	def set_parent(self, _x):
		self.__pere = _x
