#!/usr/bin/python3
print("C'est le groupe A1")
print("Exercice 14 fait par Louis Iwinski")

i = 0
m_c = str(input("Entrez une phrase: "))
t = 1
t = int(t)
l = len(m_c)

a = ""
m_r = ""

for i in range(l):
    p = ord(m_c[i])
    if p >= 65 or p <= 90:
        p = p - t
    m_r = m_r + chr(p)
print(m_r)