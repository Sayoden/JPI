#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 5 fait par Louis Iwinski")

n = int(input("Entrer une valeur entière : "))
compteur = 0
liste=[]
v = ""
while compteur < n :
    liste.append("*")
    for i in range(len(liste)):
        v += liste[i]
    print(v)
    v = ""
    compteur +=1
