#!/usr/bin/python3

print("Exercice n°8 fait par Lucas Goulois")

n = int(input("Veuillez rentrer un entier avec la base 10: "))

base11 = [0,1,2,3,4,5,6,7,8,9,'A']
reste = 0
quotien = n
lst = []
lstfinal = []
cpt = 0

#On fait comme pour le binaire...

if n == 0:
    print(0)
else:
    while quotien != 0:
        reste = quotien % 11
        quotien = quotien // 11
        lst.append(base11[reste])
    for i in range(len(lst)):
        lstfinal.append(lst[len(lst) - 1 - i])

print(lstfinal)