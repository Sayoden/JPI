#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 18 fait par Louis Iwinski")

n = 1
liste = []
l_2 = []
l_3 = []
while n != 0:
    n = int(input("Entrer une valeur pour l'insérer dans une liste (0 pour arrêter):"))
    liste.append(n)
    
for i in range (0,len(liste)-1) :
    if liste[i]==2 or liste[i]==3 or liste[i]==5 or liste[i]==7 : 
        l_2.append(liste[i]) 
    elif liste[i]%2==0 or liste[i]%3==0 or liste[i]%5==0 or liste[i]%7==0 :
        l_3.append(liste[i])
    else :
        l_2.append(liste[i])
print (l_2 + l_3)