#!/usr/bin/python3
import random

print("Exercice n°19 fait par Lucas Goulois")

listecarte = [["trèfle", "carreau", "pique", "coeur"], "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi", "as"]

lstcarte1 = []
lstcarte2 = []

for i in range(0, 4):
    for x in range(1, 14):
        listetemp = [listecarte[0][i], listecarte[x]]
        lstcarte1.append(listetemp)
        lstcarte2.append(listetemp)

#Affichage des deux jeux de cartes
print("Affichage du premier jeu de carte:")
for a in range(0, len(lstcarte1)):
    print(lstcarte1[a][1],"de",lstcarte1[a][0])

print("Affichage du deuxième jeu de carte:")
for b in range(0, len(lstcarte2)):
    print(lstcarte2[b][1],"de",lstcarte2[b][0])

#Tirage des 10 cartes dans les jeux
listepioche1 = []
listepioche2 = []

while len(listepioche1) != 10:
    randompioche = random.randint(0, len(lstcarte1) - 1)
    pioche = lstcarte1[randompioche]
    if not listepioche1.__contains__(pioche):
        listepioche1.append(pioche)

while len(listepioche2) != 10:
    randompioche = random.randint(0, len(lstcarte2) - 1)
    pioche = lstcarte2[randompioche]
    if not listepioche2.__contains__(pioche):
        listepioche2.append(pioche)

print("Liste du tirage pour le jeu 1:")
print(listepioche1)

print("Liste du tirage pour le jeu 2:")
print(listepioche2)

#Trouver les cartes identiques
listecarteidem = []
for y in range(0, len(listepioche1)):
    for z in range(0, len(listepioche2)):
        if listepioche1[y] == listepioche2[z]:
            print(listepioche1[y][1],"de",listepioche1[y][0],"est dans les deux jeux")
    
