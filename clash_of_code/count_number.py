# Lire l'entrée, qui est une chaîne de 8 caractères binaires (1 et 0)
byte = input()

# Compter le nombre de '1' dans la chaîne
count_ones = byte.count('1')

# Doubler ce nombre
result = count_ones * 2

# Afficher le résultat
print(result)

# ou

count = 0
stringlist = "101110000111"
for string in stringlist:
    count += string.count("1")

print(count*2)