import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    max_height = 0  
    hauteur_list = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        hauteur_list.append(mountain_h)
        if mountain_h > max_height:  # vérifier si la hauteur actuelle est supérieure à la hauteur maximale
            max_height = mountain_h  # mettre à jour la hauteur maximale si nécessaire

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.
    res = hauteur_list.index(max_height)  # obtenir l'indice de la hauteur maximale
    print(res)  # imprimer l'indice de la hauteur maximale
