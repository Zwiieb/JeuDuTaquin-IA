# --------------------------------------------
# import
# --------------------------------------------
import random
import Taquin
import Node


# --------------------------------------------
# méthodes
# --------------------------------------------

def donne_alea(n):
	retour = []
	for i in range(n):
		retour.append(random.randint(1, 10 * n))
	return retour


def resolution(taquin):
	abr = Node.Node(taquin)
	a2 = Node.Node(taquin)
	abr.affiche()
	a2.affiche()
	print(abr.get_valeur().get_heuristique())
	print(abr.search(abr.get_valeur().get_heuristique(), 1))


# while abr.get_valeur().


def creation_arbre(liste, trace=0):
	if trace > 0:
		print("Liste : ", liste)
	tree = Node.Node(liste[0])
	for i in range(1, len(liste)):
		if trace > 0:
			print("Insertion de la valeur ", liste[i], " dans l'arbre :")
		tree = tree.inserer(liste[i])
		if trace > 0:
			tree.affiche()
	return tree


# -------------------------------------------------------------


# --------------------------------------------		
# test abr
# --------------------------------------------

# liste = [10,9,8,7,6,5,4,3,2]
# liste = donne_alea(20)
# tree = creation_arbre(liste)

# --------------------------------------------
# test taquin
# --------------------------------------------

# création du jeu
taquin = Taquin.Taquin(3)
t2 = Taquin.Taquin(4)

# création du noeud racine de l'abr
abr = Node.Node(taquin)

# insert le jeu de taquin t2 dans l'abr
abr.inserer(t2)

# affiche l'abr d'heuristique du taquin
abr.affiche()

# copie de l'état initial pour la fin
etat_initial = taquin.get_liste().copy()


# affichage du plateau
taquin.afficher_plateau()

# --------------------------------------------
# test jeu taquin manuel
# --------------------------------------------

# taquin.jeu()
