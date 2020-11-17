#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 13 fait par Louis Iwinski")

i = 0
m_a_c=str(input("Entrez une phrase: "))
m_a_c = m_a_c.replace(" ","")
longueur=len(m_a_c)
m_a_c = m_a_c.upper()

t = 1
t = int(t)

a = ""
m_c = ""

for i in range(longueur):
    p = ord(m_a_c[i])
    if p >= 65 or p <= 90:
        p = p + t
        if p > 91:
            p = p - 26
        if p <65:
            p = p+26
    m_c = m_c + chr(p)
print(m_c)