#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 2 fait par Louis Iwinski")

n = int(input("Entrer un entier : "))
a = 0
somme = 0

while 2**a < n :
    somme += 2**a
    a += 1 

print(somme)
    
    