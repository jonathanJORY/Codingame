import sys

# Fonction pour trouver le voisin le plus proche sur la droite
def find_right_node(x, y, grid, width):
    for i in range(x + 1, width):
        if grid[y][i] == '0':
            return i, y
    return -1, -1

# Fonction pour trouver le voisin le plus proche en bas
def find_bottom_node(x, y, grid, height):
    for i in range(y + 1, height):
        if grid[i][x] == '0':
            return x, i
    return -1, -1

# Don't let the machines win. You are humanity's last hope...
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

# Lire la grille
grid = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(list(line))

# Parcourir la grille pour trouver chaque nœud et ses voisins
for y in range(height):
    for x in range(width):
        if grid[y][x] == '0':  # Si c'est un nœud
            # Trouver les voisins
            right_node_x, right_node_y = find_right_node(x, y, grid, width)
            bottom_node_x, bottom_node_y = find_bottom_node(x, y, grid, height)

            # Afficher les résultats
            print(f"{x} {y} {right_node_x} {right_node_y} {bottom_node_x} {bottom_node_y}")
