import Node

liste = [8, 4, 2, 3, 9, 1, 5]
tree = Node.Node(liste[0])
for i in range(1, len(liste)):
    tree.insert(liste[i], 0)

tree.Affiche()
# on peut remarquer que cet arbre est désiquilibré
# il faudrait procéder à un rééquilibrage ...
# voir ci-dessous pour une explication de comment faire
# https://perso.univ-lemans.fr/~lbarra/L2-SPI/CoursAlgoSPI_4_AVLEquilibrage_etd.pdf


for i in range(1,10):
	print("recherche de la valeur ", i," : ",tree.search(i,0))