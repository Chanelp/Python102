# UNION -> En un solo conjunto une todos los elementos sin repetir de ambos conjuntos
set_a = {'col', 'mex', 'bol'}
set_b = {'bol', 'pe'}
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# INTERSECCION -> Muestra el o los elementos en comun de ambos conjuntos
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# DEFERENCIA -> Es una extraccion o resta de los elementos del conjunto b dentro del conjunto a
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

# DIFERENCIA SIMETRICA -> Crear un conjunto a partir de los elementos de cada conjunto sin los que se repiten en ambos
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)