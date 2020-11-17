#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 10 fait par Louis Iwinski")

x = int(input("Entrer un entier"))
liste = []
while (x>0):
    f = x % 10
    x = x // 10
    liste.append(f)
print(liste)
