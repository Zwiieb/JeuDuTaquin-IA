class Node:

	def __init__(self, _value):
		self.__value = _value
		self.__parent = None
		self.__left = None
		self.__right = None

	# méthodes
	def search(self, _x, trace):
		res = False
		if trace == 1:
			print("x:", _x)
			print("value:", self.__value)
		# la valeur est trouvée
		if _x == self.__value:
			res = True
		# si la valeur n'est pas trouvée on navigue dans l'arbre à sa recherche
		if _x < self.__value:
			if self.__left is not None:
				res = Node.search(self.__left, _x, trace)
		elif _x > self.__value:
			if self.__right is not None:
				res = Node.search(self.__right, _x, trace)
		return res

	def insert(self, _val, trace):
		if trace == 1:
			print("_val:", _val)
			print("__value", self.__value, "\n")

		# test valeur en ajout et valeur du noeud
		if _val < self.__value:
			# s'il n'y a pas de noeud à gauche on en créer un
			if self.__left is None:
				self.__left = Node(_val)
				# le noeud actuel devient le noeud parent
				self.__left.__parent = self
			else:
				# on navigue vers le noeud de gauche
				Node.insert(self.__left, _val, trace)
		# test valeur en ajout et valeur du noeud
		elif self.__value < _val:
			# s'il n'y a pas de noeud à droite on en créer un
			if self.__right is None:
				self.__right = Node(_val)
				# le noeud actuel devient le noeud parent
				self.__right.__parent = self
			else:
				# on navigue vers le noeud de droite
				Node.insert(self.__right, _val, trace)

	def remove(self, _x, trace):
		if trace == 1:
			print("x:", _x)
			print("value:", self.__value)

		# recherche du noeud
		if _x < self.__value:
			if trace == 1:
				print("navigation dans gauche")
			if self.__left is not None:
				Node.remove(self.__left, _x, trace)
			else:
				print("Le nombre n'est pas dans le graphe")
		elif _x > self.__value:
			if trace == 1:
				print("navigation dans droite")
			if self.__right is not None:
				Node.remove(self.__right, _x, trace)
			else:
				print("Le nombre n'est pas dans le graphe")

		# suppression du noeud
		elif _x == self.__value:
			if trace == 1:
				print("début suppression")
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

	# getter / setter
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
			self.__left = _x

		@property
		def right(self):
			return self.__right

		@right.setter
		def right(self, _x):
			self.__right = _x


def display(node):
	if node is not None:
		return node.value, display(node.left), display(node.right)


liste = [8, 4, 3, 2, 9, 1, 2]

# création de l'arbre binaire
tree = Node(liste[0])
for i in range(1, len(liste)):
	tree.insert(liste[i], 0)

print("display :", display(tree))
print("search :", tree.search(3, 0), "\n")
print("remove \n")
tree.remove(3, 0)
print("display :", display(tree))
print("search :", tree.search(3, 0), "\n")
