# --------------------------------------------
# import
# --------------------------------------------
import Resolution
import Taquin

# --------------------------------------------
# code
# --------------------------------------------
# création d'un jeu de taquin ayant une disposition aléatoire
taquin = Taquin.Taquin(2)
# taquin.creer_hasard()
taquin.placement([2, 0, 'x', 1])
print("La taquin créé initialement : ")

resolution = Resolution.Resolution(taquin)
resolution.resolution()
# --------------------------------------------
# test jeu taquin manuel
# --------------------------------------------
# taquin.jeu()
