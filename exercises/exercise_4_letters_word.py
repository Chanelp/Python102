def filter_by_length(words):
   # Escribe tu solución 👇
   mas_de_4 = list(filter(lambda word:len(word) > 3, words))
   return mas_de_4

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)