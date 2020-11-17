#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 7 fait par Louis Iwinski")

liste = [0]
somme = 0
x = 0
y = 1
n = int(input("Entrer en entier qui est entièrement positif : "))

for i in range(0,n-1) :
    liste.append(y)
    somme += x
    somme += y 
    x = y 
    y = somme 
    somme = 0 

print("La moyenne de ", n, " avec la suite de Fibonacci est de :", sum(liste)/n)
