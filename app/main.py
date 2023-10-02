import utils

print(utils.get_population())

data = [{
	'Country': 'Colombia',
	'Population': 500
},
{
	'Country': 'Bolivia',
	'Population': 300
}
]

country = input("Type country: ")
result = utils.population_by_country(data, country)
print(result)