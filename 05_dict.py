import random

# Dictionary Comprehension
dict = {}
for i in range(1, 5):
    dict[i] = i * 2

print(dict)

dict2 = {i : i * 2 for i in range(1, 5)}
print(dict2)

# EJEMPLO con paises
countries = ['col', 'bol', 'rd', 'pr']
population = {country:random.randint(50, 99) for country in countries}
print(population)

# Unir listas con ZIP
names = ['Ana', 'Juan', 'Lina', 'Lucas']
ages = [19, 22, 29, 26]

people = {name:age for (name, age) in zip(names, ages)}
print(people)

people = {names[i]:ages[i] for i in range(len(names))}
print(people)