import sys

# Fonction pour générer une représentation de points pour un nombre spécifié sur une tuile de domino.
def generate_dots(number):
    # Dictionnaire contenant les représentations des points pour les nombres de 0 à 6.
    representations = {
        0: ['   ', '   ', '   '],
        1: ['   ', ' * ', '   '],
        2: ['*  ', '   ', '  *'],
        3: ['*  ', ' * ', '  *'],
        4: ['* *', '   ', '* *'],
        5: ['* *', ' * ', '* *'],
        6: ['* *', '* *', '* *']
    }

    # Récupère la représentation correspondante du nombre dans le dictionnaire, ou retourne une valeur par défaut si le nombre n'est pas valide.
    return representations.get(number, ['???', '???', '???']) 

# Cette section du code est générée automatiquement et aide à lire les données d'entrée selon les spécifications du problème.
# Lecture des nombres du haut et du bas de la tuile de domino à partir de l'entrée standard.
top_number, bottom_number = [int(i) for i in input("Entrer deux nombre d'1 à 6 séparer d'un espace").split()]

# Affichage du dessus de la tuile de domino.
print("+---+")

# Utilisation de la fonction generate_dots pour obtenir et afficher la représentation en points du nombre supérieur.
for line in generate_dots(top_number):
    print("|" + line + "|")

# Affichage de la ligne médiane de la tuile de domino.
print("+---+")

# Utilisation de la fonction generate_dots pour obtenir et afficher la représentation en points du nombre inférieur.
for line in generate_dots(bottom_number):
    print("|" + line + "|")

# Affichage du bas de la tuile de domino.
print("+---+")
