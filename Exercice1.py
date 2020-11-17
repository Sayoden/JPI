#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 1 fait par Louis Iwinski")

import math
x = str(input("Entrer un paramètre(hauteur/rayon/volume)"))
c = 0

if x == "hauteur" :
    r = float(input("Entrer un rayon en cm:"))
    v = float(input("Entrer un volume en cm^3:"))
    c = ((v / (3.14 *(r**2))))
    print(c,"cm")

elif x == "volume" :
    r = float(input("Entrer un rayon en cm:"))
    h = float(input("Entrer une hauteur en cm:"))
    c = (3.14 * (r**2) * h)
    print(c,"cm^3")
    
elif x == "rayon" :
    h = float(input("Entrer une hauteur en cm:"))
    v = float(input("Entrer un volume en cm^3:"))
    c = math.sqrt((v/(3.14 * h)))
    print(c,"cm")

else :
    print("Vous ne pouvez indiquer le rayon , la hauteur ou le volume")