"""
calcul de l'approximation de Pi en utilisant la série de Madhava-Leibniz pour les premiers n termes. 
Le résultat est ensuite arrondi à cinq décimales après la virgule avant d'être imprimé.
"""



print(f"{sum((-1) ** i / (2 * i + 1) for i in range(int(input()))) * 4:.5f}")

# ou

n = int(input())

approximation = 0
sign = 1

for i in range(1, 2 * n, 2):
    approximation += sign * (1 / i)
    sign *= -1


pi_approximation = 4 * approximation

print(f"{pi_approximation:.5f}")

