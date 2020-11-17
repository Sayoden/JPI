#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 9 fait par Louis Iwinski")

from random import *

n =  randint(1,100)
nombre = int(input("Entrer un nombre : "))

while n != nombre:
    if nombre > n:
        print("Plus petit")
    elif nombre < n:
        print("Plus grand")
    nombre = int(input("Entrer un nombre : "))
print("C'est trouvé")
