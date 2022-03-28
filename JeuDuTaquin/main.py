# --------------------------------------------
# import
# --------------------------------------------
import Taquin

# --------------------------------------------
# code
# --------------------------------------------

print("h degressif",len('BBGHDBGGHDHGBDBDHHGBDBGHHDBBGGHDBDHGGBDD'))
print("sans poid",len('GBDBGGHDDBGGHDHDBBGHHGBDDB'))
taquin = Taquin.Taquin(3)
print(taquin.poids)
print(taquin.poids1)
print(taquin.poids2)
taquin.set_plateau([1,3,'x',5,7,6,4,2,0])
taquin.jeu()

