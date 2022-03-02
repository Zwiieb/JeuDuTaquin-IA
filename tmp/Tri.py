def tri_insert(liste):
	for i in range(len(liste) - 1):
		print("1", i)
		while i + 1 > 0 and liste[i] > liste[i + 1]:
			liste[i], liste[i + 1] = liste[i + 1], liste[i]
			i -= 1
			print("2", i)
	return liste


liste = [8, 4, 3, 2, 9, 1, 2]
print(tri_insert(liste))
liste.sort()
print(liste)
