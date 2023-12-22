import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
emplacement_x = initial_tx
emplacement_y = initial_ty
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    if emplacement_x < light_x and emplacement_y < light_y:
        print("SE")
        emplacement_x += 1
        emplacement_y += 1

    elif emplacement_x < light_x and emplacement_y > light_y:
        print("NE")
        emplacement_x += 1
        emplacement_y -= 1
    
    elif emplacement_x > light_x and emplacement_y > light_y:
        print("NW")
        emplacement_x -= 1
        emplacement_y -= 1

    elif emplacement_x > light_x and emplacement_y < light_y:
        print("SW")
        emplacement_x -= 1
        emplacement_y += 1

    elif emplacement_x > light_x and emplacement_y == light_y:
        print("W")
        emplacement_x -= 1

    elif emplacement_x < light_x and emplacement_y == light_y:
        print("E")
        emplacement_x += 1

    elif emplacement_x == light_x and emplacement_y < light_y:
        print("S")
        emplacement_y += 1

    elif emplacement_x == light_x and emplacement_y > light_y:
        print("N")
        emplacement_y -= 1

