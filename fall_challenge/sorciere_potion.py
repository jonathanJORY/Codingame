"""Vous devez programmer une IA pour jouer à un jeu où vous contrôlez une sorcière dans un magasin de potions.
Le but du jeu est de gagner plus de rubis que votre adversaire en préparant des potions.
Chaque potion nécessite certains ingrédients (avec 4 types différents),
et chaque sorcière commence avec 10 ingrédients de chaque type.
Les potions sont représentées par des commandes qui ont un identifiant unique (id),
une liste de delta (qui sont les quantités d'ingrédients consommés, représentées par des nombres négatifs),
et un prix en rubis que la potion rapporte une fois préparée.
Il y a un maximum de 5 commandes disponibles à chaque tour et de nouvelles commandes apparaissent
pour remplacer celles qui ont été prises. La partie se termine quand une sorcière a préparé 2 potions ou après 100 tours"""


import sys

# Initialize inventory with 3 ingredients of type 0
inv = [3, 0, 0, 0]
max_inventory_size = 10  # Maximum inventory size for all ingredients
score = 0

def inventory_balance(inv, target_balance):
    # Return True if inventory is balanced according to the target balance
    return all(inv[i] >= target for i, target in enumerate(target_balance))

def can_cast_spell(inv, spell_deltas, max_per_ingredient=6):
    # Check if we can cast this spell without going negative on any ingredient, not exceeding inventory space,
    # and not having more than max_per_ingredient of any single type
    new_inv = [inv[i] + spell_deltas[i] for i in range(4)]
    return all(
        0 <= new_inv[i] <= max_inventory_size and 
        new_inv[i] <= max_per_ingredient for i in range(4)
    ) and sum(new_inv) <= max_inventory_size
# Game loop
while True:
    action_count = int(input())  # Number of available actions
    brewable_potions = []
    castable_spells = []

    balanced_target = [2, 2, 2, 2]
    
    for i in range(action_count):
        inputs = input().split()
        action_id, action_type = int(inputs[0]), inputs[1]
        deltas = list(map(int, inputs[2:6]))
        price = int(inputs[6])
        castable = inputs[9] != "0"

        # Collect brewable potions
        if action_type == "BREW" and all(inv[j] >= -deltas[j] for j in range(4)):
            brewable_potions.append((price, action_id, deltas))
        
        # Collect castable spells if we have enough ingredients and space in inventory
        if action_type == "CAST" and castable and can_cast_spell(inv, deltas):
            castable_spells.append((action_id, deltas))
    
    inv = list(map(int, input().split()))  # Read new inventory from the game
    score = int(input().split()[4]) # Read new score from the game

    # Brewing the most expensive potion
    if brewable_potions:
        brewable_potions.sort(reverse=True)
        best_potion = brewable_potions[0]
        print(f"BREW {best_potion[1]}")
    else:
        # Sort spells by their ability to balance our inventory towards the target
        castable_spells.sort(key=lambda spell: sum((inv[i] + spell[1][i]) * (1 if inv[i] < balanced_target[i] else -1) for i in range(4)), reverse=True)
        for spell in castable_spells:
            if can_cast_spell(inv, spell[1]):
                print(f"CAST {spell[0]}")
                break
        else:
            # Rest to refresh all spells if no castable spells are available or inventory is full
            print("REST")
