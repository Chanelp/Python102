set_countries = {'col', 'rd', 'bol', 'mex', 'bra', 'rd'}
size = len(set_countries)
print(size)

print('bol' in set_countries)
print('pe' in set_countries)

# ADD
set_countries.add('pe')
print(set_countries)

# UPDATE
set_countries.update({'ecua', 'arg', 'rd'})
print(set_countries)

# REMOVE
set_countries.remove('pe')
print(set_countries)

set_countries.discard('hti')
print(set_countries)

# CLEAR
set_countries.clear()
print(set_countries)
print(len(set_countries))