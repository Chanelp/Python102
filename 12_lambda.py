def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1

result = increment(14)
print(result)

result = increment_v2(21)
print(result)

full_name = lambda firtsName, lastName : f'The full name is {firtsName.title()} {lastName.title()} :)'
print(full_name('chanel', 'paredes'))