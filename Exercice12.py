#!/usr/bin/python3

print("Exercice n°12 fait par Lucas Goulois")

lst = []
lst2 = []

val = 1
while val != 0:
    n = int(input("Veuillez rentrer un entier pour la liste 1. Si vous voulez terminer la liste, entrez 0: "))
    val = n
    if val != 0:
        lst.append(n)

val = 1

while val != 0:
    n = int(input("Veuillez rentrer un entier pour la liste 2. Si vous voulez terminer la liste, entrez 0: "))
    val = n
    if val != 0:
        lst2.append(n)

print("Calcul du 'bili-bili' de ces listes...")

lastvalue = 0
calcul = 0
for i in range(0, len(lst2)):
    lastvalue = lst2[i]
    for x in range(0, len(lst)):
        currentvalue = lst[x]
        calcul += lastvalue * currentvalue

newcalcul = 0
for y in range(0, len(str(calcul))):
    newcalcul += int(str(calcul)[y])

print(newcalcul)