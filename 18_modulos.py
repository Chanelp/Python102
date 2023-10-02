# Para preguntar por el sistema operativo
import sys
print(sys.path)

# Para manejo de horas y fechas
import time
timestamp = time.time()

local = time.localtime()
result = time.asctime(local)
print(result)

# Para manejo de listas
import collections
numbers = [1, 1, 2, 3, 4, 1, 45, 34, 34, 3, 1, 1, 8]
counter = collections.Counter(numbers)
print(counter)

# Para expresiones regulares
import re
about = "Mi numero de telefono de 142 134 531, el codigo de mi pais es 01 y mi numero de la suerte es 333"
result_re = re.findall('[0-9]+', about)
print(result_re)