# print(0 / 0)
# print(result)
print('Errores en python')

suma = lambda x,y: x + y
assert suma(2,2) == 4

print('Error')

age = 12
if age < 18:
    raise Exception("No se admiten menores de edad! + 18")