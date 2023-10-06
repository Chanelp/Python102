people = [
  {
    'name' : 'Pedro',
    'country': 'Colombia',
    'age' : 18,
    'course' : 'developer'
  },
  {
    'name' : 'Juan',
    'country': 'Perú',
    'age' : 17,
    'course' : 'UX'
  },
  {
    'name' : 'Carlos',
    'country': 'Chile',
    'age' : 31,
    'course' : 'Diseño'
  },
  {
    'name' : 'Ana Maria',
    'country': 'Colombia',
    'age' : 25,
    'course' : 'Tester'
  }
]


colombianos_mayores_edad = list(filter(lambda student:student['country'] == 'Colombia' and student['age'] > 17, people))
print("Los estudiantes colombianos que son mayores de edad --->")
print(colombianos_mayores_edad)

word = "Holanda"
print(word)
print(len(word))