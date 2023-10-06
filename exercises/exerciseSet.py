# Para resolver este desafío, debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set.


countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()

# Escribe tu solución 👇

# Solución 1
new_set = countries | northAm | centralAm | southAm
print(new_set)

# Solución 2
new_set = countries.union(northAm, centralAm, southAm)
print(new_set)

# Solución 3
new_set.update(countries, northAm, centralAm, southAm)

print(new_set)