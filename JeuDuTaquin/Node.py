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
	# Fonction d'insertion
	# fonction qui ajoute un noeud
	# --------------------------------------------
	def inserer(self, valeur):
		# valeurs par défaut pour le retour
		retour = self
		# test valeur en ajout et valeur du noeud
		if valeur <= self.__etat:
			# s'il n'y a pas de noeud à gauche on en créer un
			if self.__gauche is None:
				self.__gauche = Node(valeur)
			else:
				# on navigue vers le noeud de gauche
				self.__gauche = self.__gauche.inserer(valeur)
		# test valeur du noeud et valeur en ajout
		elif valeur > self.__etat:
			# s'il n'y a pas de noeud à droite on en créer un
			if self.__droite is None:
				self.__droite = Node(valeur)
			else:
				# on navigue vers le noeud de droite
				self.__droite = self.__droite.inserer(valeur)
		
		# équilibrage ?
		# s'il y a une branche à droite on récupère sa profondeur
		if self.__droite:
			poids_right = self.__droite.profondeur_max() + 1
		else:
			poids_right = 0
		# s'il y a une branche à gauche on récupère sa profondeur
		if self.__gauche:
			poids_left = self.__gauche.profondeur_max() + 1
		else:
			poids_left = 0
		
		# regarde si les branches ont un écart de profondeur supérieur à 1
		# et fait une rotation pour équilibrer au besoin
		if poids_right > poids_left + 1:
			retour = self.rot_gauche()
		
		elif poids_right + 1 < poids_left:
			retour = self.rot_droite()
		# il y a un retour pour garder la référence de la branche qui a appelée la fonction
		# (sinon on la perd avec les récurrences)
		return retour
	
	# --------------------------------------------
	# Fonction qui retourne la valeur la plus petite de l'arbre
	# --------------------------------------------
	def donne_min(self):
		# valeurs par défaut pour le retour
		retour = self.__etat
		# on va autant à gauche qu'on le peut
		if self.__gauche is not None:
			retour = self.__gauche.donne_min()
		return retour
	
	# --------------------------------------------
	# Fonction qui supprime une valeur de l'arbre
	# --------------------------------------------
	# retourne un pointeur sur un noeud pour la gestion de l'effacement d'un fils.
	# De plus retourne une valeur booléenne indiquant s'il y a eu suppression
	def supprime(self, valeur):
		# valeurs par défaut pour le retour
		flag_suppression = False
		retour = self
		
		#print("Entrée dans supprime avec self=",self," et valeur = ",valeur)
		
		if valeur < self.__etat:
			#print("La valeur est plus petite donc on va à gauche")
			
			# on navigue à gauche
			if self.__gauche != None:
				self.__gauche, flag_suppression = self.__gauche.supprime(valeur)
		elif valeur > self.__etat:
			#print("La valeur est plus petite donc on va à droite")

			# on navigue à droite
			if self.__droite != None:
				self.__droite, flag_suppression = self.__droite.supprime(valeur)
		else:
			#print("La valeur est =")

			# On est sur le noeud qui possède la valeur à supprimer
			if self.__etat == valeur:
				# c'est bien la valeur à effacer !
				flag_suppression = True
				
				# cas 1 : c'est une feuille !
				if self.__gauche is None and self.__droite is None:
					# Pas d'enfants donc on efface le noeud
					retour = None
				# cas 2 : le noeud possède qu'une seule feuille
				elif self.__gauche is None:
					# Qu'une feuille à droite, on retourne la branche de droite
					retour = self.__droite
				elif self.__droite is None:
					# Qu'une feuille à droite, on retourne la branche de gauche
					retour = self.__gauche
				else:
					# cas 3 : il y a des valeurs à droite et à gauche !
					# Deux feuilles
					valeur_min = self.__droite.donne_min()
					# on cherche le min
					self.__etat = valeur_min
					# on supprime la valeur min
					self.__droite, trouve = self.__droite.supprime(valeur_min)
			else:
				#print("Pas la valeur que l'on cherche !")
				if self.__gauche != None:
					#print("On va regarder à gauche")
					self.__gauche, flag_suppression = self.__gauche.supprime(valeur)
				# On regarde maintenant si on a effacé la valeur. Sinon c'est qu'elle se trouve à droite
				if not flag_suppression:
					#print("Pas trouvé à gauche. On va regarder à droite !")
					if self.__droite != None:
						self.__droite, flag_suppression = self.__droite.supprime(valeur)
		# fin de la méthode on renvoie 'retour'
		return retour, flag_suppression
	
	# --------------------------------------------
	# Fonction qui retourne la valeur la plus petite de l'arbre
	# --------------------------------------------
	def donne_noeud_min(self):
		# valeurs par défaut pour le retour
		retour = self
		if self.__gauche is None:
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
	def rot_droite(self):
		# attribution de la valeur pivot
		pivot = self.__gauche
		
		# je vais avoir comme fils droit la gauche de mon fils droit
		self.__gauche = pivot.get_droite()
		# et mon fils droit va m'avoir comme fils gauche
		pivot.set_droite(self)
		
		# retour du pivot pour ne pas perdre le premier self.__gauche
		return pivot
	
	# --------------------------------------------
	#   fonction de rotation d'arbre binaire à gauche
	# --------------------------------------------
	def rot_gauche(self):
		# attribution de la valeur pivot
		pivot = self.__droite
		
		# je vais avoir comme fils droit la gauche de mon fils droit
		self.__droite = pivot.get_gauche()
		# et mon fils droit va m'avoir comme fils gauche
		pivot.set_gauche(self)
		
		# retour du pivot pour ne pas perdre le premier self.__gauche
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
