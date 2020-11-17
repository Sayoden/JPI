#!/usr/bin/python3

print("Exercice n°17 fait par Lucas Goulois")

cpt = 0

x = int(input("Veuillez rentrer un entier: "))

for i in range(1, x):
    if x % i == 0:
        cpt += i
        print(cpt, i)

if cpt == x:
    print(True)
else:
    print(False)
