#!/usr/bin/python3

print("Exercice n°4 fait par Lucas Goulois")

n = int(input("Entrez un entier: "))
lst = []
cpt = 0
lastvalue = 0

for i in range(1, n + 1):
    lst = []
    cpt += 1
    for x in range(1, n + 1):
        value = x
        if lastvalue == cpt:
            value = cpt
            lst.append(value)
        else:
            lst.append(value)
        lastvalue = value
    print(lst)


