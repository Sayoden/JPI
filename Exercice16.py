#!/usr/bin/python3

print("Exercice n°16 fait par Lucas Goulois")

a = int(input("Entrez le premier nombre entier"))
b = int(input("Entez le deuxième nombre entier"))

def pgcd(a,b):
    if b == 0:
        return a
    else:
        reste = a % b
        return pgcd(b, reste)

if a > 0 and b > 0:
    if pgcd(a,b) == 1:
        print(True)
    else:
        print(False)
else:
    print("Les nombres doivent être positifs")