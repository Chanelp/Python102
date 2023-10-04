# Iterables
for n in range(1, 4):
    print(n)

my_iterador = iter(range(1, 4))
print(next(my_iterador))
print(next(my_iterador))
print(next(my_iterador))
print(next(my_iterador)) # Genera StopIteration