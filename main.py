# --------------------------------------------
# import
# --------------------------------------------
import random
import Taquin
import Node

# --------------------------------------------
# code
# --------------------------------------------
# création d'un jeu de taquin ayant une disposition aléatoire
taquin = Taquin.Taquin(3)

# création du noeud racine de l'abr
abr = Node.Node(taquin)

# affiche l'abr d'heuristique du taquin
abr.affiche()

# copie de l'état initial pour la fin
etat_initial = taquin.get_liste().copy()

# --------------------------------------------
# test jeu taquin manuel
# --------------------------------------------

taquin.jeu()
