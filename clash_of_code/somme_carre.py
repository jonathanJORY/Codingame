"""prend en entrée les entiers, calcule la somme des nombres donnés, trouve le carré de cette somme, puis imprime le résultat."""


print(sum(int(input()) for _ in range(int(input()))) ** 2)

