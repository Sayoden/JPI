#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 6 fait par Louis Iwinski")

n = int(input("Entrer une valeur pour les étoiles"))
liste = []
for i in range(1,n*2,2) :
    liste.append("*")
    print(" "*n + i*"*")
    n = n-1