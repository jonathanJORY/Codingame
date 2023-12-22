import sys
import math

boost_available = True
last_checkpoint_x = None
last_checkpoint_y = None
acceleration_after_checkpoint = False

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# game loop
while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    opponent_distance = distance(x, y, opponent_x, opponent_y)

    # Logique pour ajuster la poussée en fonction de l'angle et de la distance au prochain checkpoint
    if abs(next_checkpoint_angle) > 90:
        thrust = "0"
    elif abs(next_checkpoint_angle) > 75:
        thrust = "75"
    elif next_checkpoint_dist > 10000 and boost_available:
        thrust = "BOOST"
        boost_available = False
    else:
        # Si nous sommes assez proches du prochain checkpoint, commençons à freiner
        if next_checkpoint_dist < 1500:  # La distance peut être ajustée selon la physique du jeu
            thrust = "30"
        elif next_checkpoint_dist < 800:  # Freinez davantage si vous êtes très proche
            thrust = "10"
        else:
            thrust = "100"  # Autrement, maintenez la poussée maximale

    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + thrust)
