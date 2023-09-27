# Dictionary Comprehensions using Conditionals

import random

countries = ['col', 'mex', 'bol', 'arg']
population1 = { country:random.randint(1, 50) for country in countries}
print(population1)

result = {country:population for (country, population) in population1.items() if population > 20}
print(result)

# En el diccionario la llave no se puede repetir
text = 'Murcielago hola'
unique = {l:l.upper() for l in text if l in 'aeiou'}
print(unique)