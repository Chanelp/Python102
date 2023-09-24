set_countries = {'col', 'rd', 'bol', 'mex', 'bra', 'rd'}
print(type(set_countries))
print(set_countries)

set_numbers = {13, 24, 35, 46, 57, 57}
print(set_numbers)

set_types = {1, False, 3.14, 'Keys'}
print(set_types)

set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('hii', True, 'abc', 12, 12))
print(set_from_tuples)

numbers = [1, 2, 3, 4, 5, 5, 6, 7]
set_from_list = set(numbers)
print(set_from_list)

unique_numbers = list(set_from_list)
print(unique_numbers)