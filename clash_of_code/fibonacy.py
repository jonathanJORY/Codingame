def fibonacci(n):
    """
    Générer une liste contenant la séquence Fibonacci jusqu'à l'indice n.

    :param n: Indice jusqu'à lequel générer la séquence.
    :return: Liste contenant la séquence Fibonacci.
    """
    # Initialiser la séquence avec les deux premiers nombres
    sequence = [0, 1]
    for i in range(2, n + 1):
        # Le nouveau nombre est la somme des deux précédents
        next_number = sequence[i - 1] + sequence[i - 2]
        # Ajouter le nouveau nombre à la séquence
        sequence.append(next_number)
    return sequence

# Lire les indices de début et de fin de la séquence à imprimer
x, y = map(int, input().split())

# Générer la séquence Fibonacci jusqu'à l'indice 'y'
fib_sequence = fibonacci(y)

# Imprimer les nombres de la séquence dans l'intervalle demandé
print(' '.join(map(str, fib_sequence[x:y+1])))
