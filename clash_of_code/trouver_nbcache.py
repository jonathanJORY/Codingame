"""Ce code prend en entrée les entiers A et B, 
puis utilise la stratégie optimale pour calculer le nombre maximum de suppositions 
nécessaires pour deviner le nombre caché. La fonction bit_length() est utilisée pour calculer 
le logarithme en base 2 de la longueur de l intervalle. Le code affiche ensuite ce nombre maximum de suppositions."""
# Lecture des entiers A et B

A = int(input())
B = int(input())

# Calcul du nombre de suppositions nécessaires
# La stratégie optimale consiste à diviser l'intervalle en deux à chaque supposition
# Ainsi, le nombre maximum de suppositions est le logarithme en base 2 de la longueur de l'intervalle, arrondi à l'entier supérieur
maximum_guesses = (B - A).bit_length()

# Affichage du nombre maximum de suppositions
print(maximum_guesses)

