#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 11 fait par Louis Iwinski")

import math
n = int(input("Entrer un nombre "))
liste = [[1],[1,1]]
print(liste[0])
print(liste[1])
 
for i in range(2,n+1):
    liste.append([1]) 
    for j in range(1, i):
        liste[i].append(liste[i-1][j-1] + liste[i-1][j])
    liste[i].append(1)
    print(liste[i])