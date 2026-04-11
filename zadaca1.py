"""
Napisati program koji generira kvadratnu matricu dimenzija 7x7.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na rubovima matrice.
"""
import random
r = 7
s = 7
matrica = []

for i in range(r):
    red = []
    for j in range(s):
        unos = random.randint(1,9)
        red.append(unos)
    matrica.append(red)

for red in matrica:
    print(red)

zbroj = 0

for j in range(s):
    zbroj += matrica[0][j]
    zbroj += matrica[r-1][j]

for i in range(1, r-1):
    zbroj += matrica[i][0]
    zbroj += matrica[i][s-1]

print("Zbroj elemenata na rubovima:", zbroj)