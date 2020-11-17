#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 23 fait par Louis Iwinski")

print("UTILISATION DE CM^3")
a = float(input("Saisir le volume du sac:"))
liste = [[]]
objet_p = ""
while objet_p != "fin" :
    objet_p = input("Saisir l'objet que vous voulez mettre dans votre sac: (tapez fin pour ne plus rien mettre)")
    if objet_p != "fin" :
        volume_o = int(input("Saisir le volume de l'objet:"))
        liste.append([objet_p, volume_o])
for i in range(1, len(liste)):
    if a - liste[i][1]  >= 0 :
        liste[0].append(liste[i])
        a -= liste[i][1]

print("Les objets qui peuvent êtres contenus dans le sac sont {}".format(liste[0]))