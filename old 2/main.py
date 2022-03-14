import Node

liste = [1, 2, 5, 4, 3,6,7,8]
tree = Node.Node(liste[0])
for i in range(1, len(liste)):
	print("Insertion de la valeur ",liste[i]," dans l'arbre :")
	tree=tree.insert(liste[i])
	tree.Affiche()
print("poid",tree.right.weight() - tree.left.weight())

#print("Comparaison des affichages !")
#tree.Affiche()
#tree.pprint()

# on peut remarquer que cet arbre est désiquilibré
# https://perso.univ-lemans.fr/~lbarra/L2-SPI/CoursAlgoSPI_4CoursAlgoSPI_4_AVLEquilibrage_etd_AVLEquilibrage_etd.pdf


for i in range(1,10):
	print("recherche de la valeur ", i," : ",tree.search(i,0))