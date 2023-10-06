# En un diccionario, contar cuantas veces aparece una vocal en una cadena de texto
text = 'Un murcielago estuvo rondando por el bosque'
contar = {l: text.count(l) for l in text if l in 'aeiou'}
print(contar)