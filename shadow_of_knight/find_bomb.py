import sys

# Lire les données d'initialisation
W, H = [int(i) for i in input().split()]
N = int(input())  # Le nombre maximal de sauts autorisés
X, Y = [int(i) for i in input().split()]  # La position initiale

# Définir les limites initiales
left = 0
right = W - 1
top = 0
bottom = H - 1

# Boucle de jeu principale
while True:
    BOMB_DIR = input()  # La direction de la bombe par rapport à la position actuelle

    # Ajuster les limites en fonction de la direction de la bombe
    if "U" in BOMB_DIR:
        bottom = Y - 1
    elif "D" in BOMB_DIR:
        top = Y + 1

    if "L" in BOMB_DIR:
        right = X - 1
    elif "R" in BOMB_DIR:
        left = X + 1

    # Calculer la prochaine position en divisant la zone de recherche en deux
    X = left + (right - left) // 2
    Y = top + (bottom - top) // 2

    # Sauter à la nouvelle position
    print(X, Y)
