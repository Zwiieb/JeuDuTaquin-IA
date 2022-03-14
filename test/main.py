import Node
import random


# -------------------------------------------------------------

def DonneAlea(n):
	retour = []
	for i in range(n):
		retour.append(random.randint(1, 10 * n))
	return retour


# -------------------------------------------------------------

liste = [10,9,8,7,6,5,4,3,2]
#liste=DonneAlea(20)
print("Liste : ",liste)
tree = Node.creation_arbre(liste)
print(tree)
tree.remove(2,None,1)

tree.affiche()

'''
droite = tree.get_droite()
gauche = tree.get_gauche()
print("noeud principal:",tree.get_valeur())
print("poids droite:",droite.poids())
print("poids gauche:",gauche.poids())
'''

"""'
import Taquin

taquin = Taquin.Taquin(3)
taquin.afficher_grille()

print(taquin.liste, "\n")

taquin.mov_sud()

taquin.afficher_grille()

print('--------------------')
taquin.mov_est()
taquin.afficher_grille()
"""