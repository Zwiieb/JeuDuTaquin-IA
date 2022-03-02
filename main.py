import Node

liste = [10,9,8,7,6,5,4,3,2]
tree = Node.Node(liste[0])
for i in range(1, len(liste)):
	print("Insertion de la valeur ", liste[i], " dans l'arbre :")
	tree = tree.insert(liste[i],1)
	tree.affiche()
droite = tree.get_droite()
gauche = tree.get_gauche()
print("noeud principal:",tree.get_valeur())
print("poids droite:",droite.poids())
print("poids gauche:",gauche.poids())
