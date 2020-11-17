#!/usr/bin/python3

print("Exercice n°3 fait par Lucas Goulois")

n = int(input("Entrez un entier: "))
lst = []

for i in range(1, n + 1):
    lst = []
    for x in range(i, n + 1):
        lst.append(x)
        cpt = 1
    if len(lst) != n:
        while len(lst) != n:
            lst.append(cpt)
            cpt += 1
    print(lst)


