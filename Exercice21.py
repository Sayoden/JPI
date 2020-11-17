#!/usr/bin/python3
import random

print("Exercice n°21 fait par Lucas Goulois")

n = int(input("Veuillez rentrer le nombre d'éléments dans le tableau: "))
lst = ["b", "w", "r"]

bleu = ""
white = ""
red = ""

for i in range(1, n + 1):
    rand = random.randint(0,2)
    value = lst[rand]

    if value == "b":
        bleu += "b"
    elif value == "w":
        white += "w"
    else:
        red += "r"

print(bleu,white,red)
