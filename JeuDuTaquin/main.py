# --------------------------------------------
# import
# --------------------------------------------
import Resolution
import Taquin


# --------------------------------------------
# code
# --------------------------------------------

# fonction qui donne la moyenne du nombre d'actions, d'evaluation, et de temps pour un taquin 3x3
def moyenne(nb, heuristique):
	action = 0
	evalu = 0
	tempss = 0
	taquins = [[2, 4, 1, 6, 7, 0, 'x', 3, 5], [0, 7, 'x', 5, 4, 2, 3, 6, 1], [3, 1, 4, 7, 0, 2, 5, 6, 'x'],
			   [6, 5, 7, 4, 1, 2, 'x', 0, 3], [1, 4, 0, 5, 6, 3, 7, 'x', 2], [3, 7, 'x', 0, 6, 4, 5, 2, 1],
			   [7, 5, 4, 1, 0, 2, 6, 3, 'x'], ['x', 2, 0, 3, 7, 1, 6, 5, 4], [4, 1, 0, 3, 'x', 5, 7, 6, 2],
			   [3, 1, 6, 5, 'x', 2, 7, 0, 4], [1, 2, 0, 3, 5, 7, 6, 'x', 4], [0, 4, 1, 'x', 3, 5, 2, 7, 6],
			   [0, 3, 4, 5, 2, 1, 'x', 7, 6], [6, 3, 'x', 2, 0, 4, 5, 7, 1], [3, 0, 4, 7, 6, 'x', 5, 1, 2],
			   [4, 2, 3, 'x', 6, 1, 5, 7, 0], ['x', 0, 3, 6, 4, 2, 1, 7, 5], [2, 1, 6, 4, 'x', 7, 3, 5, 0],
			   [0, 4, 5, 'x', 7, 6, 2, 1, 3], ['x', 5, 0, 6, 4, 3, 7, 1, 2], [3, 2, 5, 0, 'x', 1, 4, 6, 7],
			   [3, 7, 'x', 1, 6, 5, 4, 2, 0], [6, 3, 4, 5, 7, 1, 2, 0, 'x'], [0, 2, 5, 'x', 7, 6, 1, 4, 3],
			   [0, 1, 2, 7, 4, 5, 'x', 3, 6], [5, 2, 6, 7, 'x', 4, 3, 0, 1], ['x', 3, 4, 7, 0, 5, 2, 1, 6],
			   [7, 4, 5, 2, 6, 3, 0, 1, 'x'], [2, 5, 7, 'x', 6, 3, 0, 4, 1], [7, 5, 6, 2, 0, 4, 3, 'x', 1],
			   [7, 2, 4, 3, 1, 'x', 0, 6, 5], [5, 3, 'x', 4, 0, 7, 6, 1, 2], [3, 5, 'x', 6, 4, 1, 2, 0, 7],
			   [5, 2, 0, 6, 'x', 7, 4, 3, 1], [7, 0, 2, 'x', 5, 4, 6, 3, 1], [6, 5, 2, 4, 3, 0, 1, 7, 'x'],
			   [6, 3, 4, 2, 7, 'x', 1, 0, 5], ['x', 0, 2, 3, 6, 4, 1, 5, 7], [4, 6, 'x', 2, 0, 5, 7, 3, 1],
			   [1, 4, 'x', 6, 0, 7, 2, 5, 3], [4, 2, 'x', 1, 3, 7, 5, 0, 6], [2, 4, 0, 'x', 6, 5, 7, 1, 3],
			   [3, 1, 7, 6, 'x', 4, 0, 5, 2], [3, 0, 6, 2, 7, 5, 'x', 4, 1], [4, 2, 3, 5, 0, 6, 7, 'x', 1],
			   [7, 5, 4, 'x', 3, 0, 1, 6, 2], [1, 'x', 7, 4, 0, 2, 3, 5, 6], [1, 6, 7, 5, 2, 4, 'x', 0, 3],
			   [4, 1, 5, 7, 0, 2, 'x', 3, 6], ['x', 6, 5, 0, 2, 7, 1, 4, 3], [1, 4, 3, 2, 5, 6, 7, 0, 'x'],
			   [0, 1, 2, 3, 6, 7, 4, 5, 'x'], [5, 7, 3, 2, 6, 1, 0, 'x', 4], [3, 1, 6, 7, 2, 4, 0, 'x', 5],
			   ['x', 3, 4, 2, 1, 5, 6, 7, 0], [3, 'x', 5, 0, 1, 2, 7, 6, 4], ['x', 7, 6, 4, 1, 5, 3, 2, 0],
			   [3, 7, 'x', 5, 2, 6, 1, 4, 0], [7, 5, 6, 3, 2, 0, 1, 'x', 4], [6, 1, 'x', 7, 0, 5, 3, 2, 4],
			   ['x', 5, 4, 6, 0, 7, 2, 3, 1], [7, 'x', 4, 1, 2, 3, 5, 6, 0], [6, 1, 'x', 4, 0, 7, 2, 5, 3],
			   [3, 2, 5, 1, 7, 'x', 0, 4, 6], [1, 7, 4, 5, 6, 2, 'x', 3, 0], [7, 5, 4, 6, 2, 'x', 3, 0, 1],
			   [1, 'x', 2, 5, 0, 6, 7, 4, 3], [5, 'x', 0, 1, 2, 6, 4, 3, 7], [7, 6, 0, 'x', 2, 1, 4, 5, 3],
			   [6, 'x', 5, 0, 4, 1, 2, 3, 7], [6, 7, 0, 1, 3, 5, 4, 2, 'x'], [4, 2, 3, 6, 7, 0, 1, 5, 'x'],
			   [2, 1, 7, 3, 6, 5, 0, 'x', 4], [3, 5, 1, 2, 6, 'x', 0, 7, 4], [1, 3, 'x', 5, 2, 7, 6, 0, 4],
			   [3, 5, 'x', 1, 7, 4, 0, 2, 6], [3, 7, 4, 5, 2, 0, 6, 1, 'x'], [2, 3, 4, 0, 1, 6, 'x', 7, 5],
			   [1, 'x', 3, 4, 5, 2, 0, 6, 7], [1, 7, 'x', 6, 3, 2, 5, 4, 0], ['x', 3, 5, 1, 7, 6, 4, 2, 0],
			   [6, 2, 7, 'x', 5, 0, 3, 1, 4], [3, 0, 5, 1, 'x', 7, 6, 4, 2], [1, 6, 4, 5, 3, 0, 2, 'x', 7],
			   [0, 2, 6, 1, 'x', 7, 5, 3, 4], [0, 3, 2, 6, 'x', 5, 7, 1, 4], [6, 4, 5, 1, 2, 0, 3, 7, 'x'],
			   [2, 5, 3, 4, 7, 0, 6, 1, 'x'], [1, 5, 4, 'x', 0, 7, 6, 3, 2], [7, 'x', 2, 5, 4, 0, 3, 6, 1],
			   [1, 2, 3, 6, 5, 'x', 7, 0, 4], [2, 3, 0, 7, 4, 5, 1, 'x', 6], ['x', 4, 1, 6, 5, 0, 7, 2, 3],
			   [2, 0, 'x', 1, 7, 4, 3, 6, 5], [1, 2, 7, 4, 'x', 5, 3, 0, 6], [2, 7, 4, 'x', 1, 5, 0, 3, 6],
			   [7, 0, 3, 4, 6, 5, 1, 2, 'x'], [5, 4, 7, 0, 3, 6, 1, 'x', 2], [5, 'x', 2, 7, 0, 6, 3, 1, 4],
			   [0, 'x', 2, 4, 3, 5, 1, 7, 6]]
	for i in range(nb):
		print(i)
		taquin = Taquin.Taquin(3)
		taquin.set_heuristique(heuristique)
		taquin.set_plateau(taquins[i])
		r = Resolution.Resolution(taquin)
		t_min, nb_eval, temps = r.resolution()
		action += len(t_min.get_actions())
		evalu += nb_eval
		tempss += temps
	print()
	print("###################################")
	print("action moyen:", action / nb)
	print("eval moyen:", evalu / nb)
	print("temps moyen:", tempss / nb)
	print("###################################")


# execute l'exemple du sujet du projet
def exemple_sujet():
	taquin = Taquin.Taquin(3)
	taquin.set_plateau([1, 3, 'x', 5, 7, 6, 4, 2, 0])
	taquin.jeu()


# donne simplement la resolution d'un taquin de taille modulable (fonctionne pour les 2x2, 3x3, 4x4
def resolution(taille):
	taquin = Taquin.Taquin(taille)
	r = Resolution.Resolution(taquin)
	r.resolution()


# lance un taquin jouable de taille modulable
def jeu(taille):
	taquin = Taquin.Taquin(taille)
	taquin.jeu()


def demo():
	print("moyenne :   		1")
	print("exemple_sujet : 	2")
	print("resolution :		3")
	print("jeu : 				4")
	choix = input("Quel est votre choix ? ")
	# pour ne pas crash quand l'utilisateur n'entre pas une valeur voulue
	if choix not in ['1', '2', '3', '4']:
		print("veuillez choisir une des propositions")
		demo()
	if choix == '1':
		nb = input('Combien de tests?')
		heu = input('quelle heuristique?')
		moyenne(int(nb), heu)
	elif choix == '2':
		exemple_sujet()
	elif choix == '3':
		taille = input('quelle taille?')
		resolution(int(taille))
	elif choix == '4':
		taille = input('quelle taille?')
		jeu(int(taille))


# lance la fonction de démonstration
demo()
