def multiply_numbers(numbers):
    # Escribe tu solución 👇
    new_list = list(map(lambda x:x*2, numbers))
    return new_list

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)