class Node:
	# constructeur
	def __init__(self, valeur, pere=None):
		# la valeur stockée
		self.__value = valeur

		# les liens avec les noeuds
		# lien avec le noeud père
		self.__parent = pere

		# Les deux noeuds fils
		# left => valeur plus petite
		self.__left = None
		# rigth => valeur plus grande
		self.__right = None


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
			print("valeur noeud      : ", self.__value)
	
		if valeur == self.__value:
			if trace >= 1:
				print("Valeur trouvée !")
			trouve = True
		elif valeur < self.__value:
			if self.__left != None:
				trouve = self.__left.search(valeur)
		elif self.__right != None:
			trouve = self.__right.search(valeur)
		return trouve

	# --------------------------------------------
	# Fonction d'insertion
	# fonction qui ajoute un noeud
	# --------------------------------------------
	def insert(self, valeur, trace=0):
		retour=self
		if trace >= 1:
			print("valeur à inserer :", valeur)
			print("Valeur du noeud  : ", self.__value, "\n")

		# test valeur en ajout et valeur du noeud
		if valeur < self.__value:
			# s'il n'y a pas de noeud à gauche on en créer un
			if self.__left is None:
				self.__left = Node(valeur,self.__parent)
			else:
				# on navigue vers le noeud de gauche
				self.__left=self.__left.insert(valeur, trace)
		# test valeur du noeud et valeur en ajout
		elif valeur > self.__value:
			# s'il n'y a pas de noeud à droite on en créer un
			if self.__right is None:
				self.__right = Node(valeur,self.__right)
			else:
				# on navigue vers le noeud de droite
				self.__right=self.__right.insert(valeur, trace)

		# equilibrage ?
		# gestion des fils None
		if self.__right:
			poids_right=self.__right.weight()+1
		else:
			poids_right=0
		
		if self.__left:
			poids_left=self.__left.weight()+1
		else:
			poids_left=0

		if trace>=1:
			print("Valeur du noeud : ", self.__value)
			print("Poids gauche = ",poids_right)
			print("Poids droit  = ",poids_left)
		
		if poids_right > poids_left+1:
			if trace >=1:
				print("Déséquibibre => rotation gauche")
			retour=self.rot_left()
				
		elif poids_right < poids_left+1:
			if trace >=1:
				print("Déséquibibre => rotation droite")
			retour = self.rot_right()

		return retour


	# --------------------------------------------
	# trouve le noeud avec la valeur la plus pres du noeud actuel
	# --------------------------------------------
	def close_of(self):

		# plus petit de gauche
		plus_proche_gauche = None

		# cherche la valeur la plus grande existant dans la branche de gauche
		if self.__left:
			if self.__left.__right:
				plus_proche_gauche = self.__left.__right
				while plus_proche_gauche.__right:
					plus_proche_gauche = plus_proche_gauche.__right
			else:
				plus_proche_gauche = self.__left

		# plus petit de droite
		plus_proche_droite = None

		# cherche la valeur la plus petite existant dans la branche de droite
		if self.__right:
			if self.__right.__left:
				plus_proche_droite = self.__right.__left
				while plus_proche_droite.__left:
					plus_proche_droite = plus_proche_droite.__left
			else:
				plus_proche_droite = self.__right

		# plus petit du noeud self

		# s'il manque des valeurs
		if plus_proche_droite is None and plus_proche_gauche is None:
			print(" pas de fils et self est :", self, self.value)
			return self
		if plus_proche_droite is None:
			res = plus_proche_gauche
		elif plus_proche_gauche is None:
			res = plus_proche_droite

		# sinon on compare la différence entre les valeurs trouvées et le noeud de base
		elif abs(self.value - plus_proche_droite.value) < abs(self.value - plus_proche_gauche.value) or abs(
				self.value - plus_proche_droite.value) == abs(self.value - plus_proche_gauche.value):
			res = plus_proche_droite
		else:
			res = plus_proche_gauche

		# retour de la réponse
		print("res:", res)
		return res

	# --------------------------------------------
	# fonction qui supprime un noeud
	# --------------------------------------------
	def remove(self, arbre, _x, trace):
		if trace == 1:
			print("x:", _x)
			print("value:", self.__value)

		# recherche du noeud
		if _x < self.__value:
			if trace == 1:
				print("navigation dans gauche")
			if self.__left is not None:
				Node.remove(self.__left, arbre, _x, trace)
			else:
				print("Le nombre n'est pas dans le graphe")
		elif _x > self.__value:
			if trace == 1:
				print("navigation dans droite")
			if self.__right is not None:
				Node.remove(self.__right, arbre, _x, trace)
			else:
				print("Le nombre n'est pas dans le graphe")

		# suppression du noeud
		elif _x == self.__value:
			if trace == 1:
				print("début suppression de ", _x)
			# si le noeud n'a pas de fils on le supprime en supprimant son accès
			if self.__right is None and self.__left is None:
				if trace == 1:
					print("pas enfant")
				if self.__parent.__left == self:
					self.__parent.__left = None
				elif self.__parent.__right == self:
					self.__parent.__right = None
			# s'il n'a pas de fils à droite on attribue sa branche de gauche à son parent
			elif self.__right is None:
				if trace == 1:
					print("pas a droite")
				if self.__parent.__right == self:
					self.__parent.__right = self.__left
				elif self.__parent.__left == self:
					self.__parent.__left = self.__left
				else:
					print("ERREUR")
			# s'il n'a pas de fils à gauche on attribue sa branche de droite à son parent
			elif self.__left is None:
				if trace == 1:
					print("pas a gauche")
				if self.__parent.__left == self:
					self.__parent.__left = self.__right
				elif self.__parent.__right == self:
					self.__parent.__right = self.__right
				else:
					print("ERREUR")
			# s'il a 2 fils
			else:
				temporaire = self
				newObj = self.close_of()
				self.__dict__.update(newObj.__dict__)
				print("tempo:", temporaire.value)
				test = temporaire.close_of()
				print("test:", test)
				print("tempo close:", temporaire.close_of().value)
				arbre.remove(arbre, temporaire.close_of().value, 0)

		# 2 return dans close of
		# manque la reattribution des branche de celui quon enleve(3)

	# --------------------------------------------
	# fonction qui test le poids(le nombre de fils) d'un noeud
	# --------------------------------------------
	def weight(self):
		res = 0
		if self.__left != None:
			res += (self.__left.weight() + 1)
		if self.__right != None:
			res += (self.__right.weight() + 1)
		return res


	# --------------------------------------------
	# --------------------------------------------
	def pprint(self, level=0):
		if self.__right:
			self.__right.pprint(level + 1)
		print(f"{' ' * 4 * level}{self.__value}")
		if self.__left:
			self.__left.pprint(level + 1)

			
	# --------------------------------------------
	# --------------------------------------------
	def rot_right(self,trace = 0):
		if trace >= 1:
			print("\nRotation droite :")
			self.AfficheNoeud()
		
		pivot=self.__left

		if trace >= 1:
			print("Le pivot : ",end="")
			pivot.AfficheNoeud()

			print("Affichage du sous-arbre qui subit cette rotation :")
			self.Affiche()
		
		# je vais avoir comme fils droit la gauche de mon fils droit
		self.__left=pivot.GetRight()
		# et mon fils droit va m'avoir comme fils gauche
		pivot.SetRight(self)

		if trace >= 1:
			print("\nRésultat de la rotation : ")
			pivot.Affiche()
			print("Fin de la rotation \n")
		return pivot

	# --------------------------------------------
	# --------------------------------------------
	def rot_left(self,trace=0):
		if trace >= 1:
			print("\nRotation gauche :")
			self.AfficheNoeud()
		
		pivot=self.__right

		if trace >= 1:
			print("Le pivot : ",end="")
			pivot.AfficheNoeud()

			print("Affichage du sous-arbre qui subit cette rotation :")
			self.Affiche()
		
		# je vais avoir comme fils droit la gauche de mon fils droit
		self.__right=pivot.GetLeft()
		# et mon fils droit va m'avoir comme fils gauche
		pivot.SetLeft(self)

		if trace >= 1:
			print("\nRésultat de la rotation : ")
			pivot.Affiche()
			print("Fin de la rotation \n")
		return pivot


			
	# --------------------------------------------
	# fonction qui affiche l'arbre dans la console
	# --------------------------------------------
	def Affiche(self, tab=0):
		if self.__left != None:
			self.__left.Affiche(tab + 1)
		print(" " * 4*tab, self.__value)
		if self.__right != None:
			self.__right.Affiche(tab + 1)

	# --------------------------------------------
	# fonction qui affiche l'arbre dans la console
	# --------------------------------------------
	def AfficheNoeud(self):
		print(self.__value)

	# --------------------------------------------
	# getter / setter
	# --------------------------------------------
	def SetLeft(self,noeud):
		self.__left=noeud

	def GetLeft(self):
		return self.__left

	def SetRight(self,noeud):
		self.__right=noeud

	def GetRight(self):
		return self.__right

	if 1:
		@property
		def value(self):
			return self.__value

		@value.setter
		def value(self, _x):
			self.__value = _x

		@property
		def parent(self):
			return self.__parent

		@parent.setter
		def parent(self, _x):
			self.__parent = _x

		@property
		def left(self):
			return self.__left

		@left.setter
		def left(self, _x):
			print("Affectation gauche")
			self.__left = _x

		@property
		def right(self):
			return self.__right

		@right.setter
		def right(self, _x):
			self.__right = _x

