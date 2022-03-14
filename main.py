# --------------------------------------------
# import
# --------------------------------------------
import random
import Taquin


# --------------------------------------------
# méthodes
# --------------------------------------------

def DonneAlea(n):
	retour = []
	for i in range(n):
		retour.append(random.randint(1, 10 * n))
	return retour


# -------------------------------------------------------------
"""
#test abr----------------------------------
#liste = [10,9,8,7,6,5,4,3,2]
liste=DonneAlea(20)
print("Liste : ",liste)
tree = Node.Node(liste[0])
for i in range(1, len(liste)):
	print("Insertion de la valeur ", liste[i], " dans l'arbre :")
	tree = tree.insert(liste[i])
	tree.affiche()
"""

taquin = Taquin.Taquin(3,1)
#print(taquin.liste, "\n")
taquin.afficher_grille()
print(taquin.cart(4))



'''
#test jeu taquin manuel
while taquin.bingo == False :
	choix = input("Quel est votre choix ? ")
	if choix == "haut":
		taquin.mov_nord()
		taquin.afficher_grille()
		taquin.check()
	if choix == "bas":
		taquin.mov_sud()
		taquin.afficher_grille()
		taquin.check()
	if choix == "gauche":
		taquin.mov_ouest()
		taquin.afficher_grille()
		taquin.check()
	if choix == "droite":
		taquin.mov_est()
		taquin.afficher_grille()
		taquin.check()
	
print("Réussie !!!!")
'''
