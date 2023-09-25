# List Comprehension
numbers = []

for element in range(1, 12):
    if element % 2 == 0:
        numbers.append(element * 2)

print(numbers)

numbers_v2 = [n * 2 for n in range(1, 11) if n % 2 == 0]
print(numbers_v2)

# EJEMPLO CON DIAS DE LA SEMANA QUE CONTENGAN A
days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
newlist = []

for d in days:
  if "a" in d:
    newlist.append(d)

print(newlist) #["martes", "sabado"]

# Con list Comprehension
list2 = [d for d in days if "a" in d]
print(list2)