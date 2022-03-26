# --------------------------------------------
# import
# --------------------------------------------
import Taquin

# --------------------------------------------
# code
# --------------------------------------------

taquin = Taquin.Taquin(2)

taquin.jeu()
print("etat initial")
print(taquin.get_etat_initial().afficher_plateau())
