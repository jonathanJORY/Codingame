"""
Répétez le mot-clé jusqu'à ce qu'il atteigne la longueur du message.
Message : CODINGAME
Mot-clé : APPLEAPPL

Additionnez le message et le mot-clé lettre par lettre en attribuant des valeurs entières aux lettres de 0 à 25 dans l'ordre alphabétique 
(c'est-à-dire A=0, B=1, C=2, etc.)."""
*l,k=open(0).read().split()
a,b,*l=map(int,l)
k*=a
for i,j in zip(l,k):print(end=chr(65+(i-ord(j)+65)%26))

"""renvoyer la moyenne des valeurs ascii des entrées"""
s=[ord(a) for a in input()]
print(sum(s)//len(s))

"""
Mettre en majuscule la première lettre de chaque mot et en minuscule les lettres suivantes."""

import sys
s = input()
# Diviser la chaîne en mots
mots = s.split()
# Appliquer les modifications à chaque mot
resultat = ' '.join([mot.capitalize() for mot in mots])
print(resultat)

""" Calculer l'air d'un trapeze"""

a = int(input())
b = int(input())
h = int(input())

# Calculer l'aire du trapèze
aire_trapeze = 0.5 * (a + b) * h

# Afficher l'aire avec une décimale
print(format(aire_trapeze, ".1f"))