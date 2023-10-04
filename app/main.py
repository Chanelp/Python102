import utils

data = [{
		'Country': 'Colombia',
		'Population': 500
	},
	{
		'Country': 'Bolivia',
		'Population': 300
	}
	]

def run():
	print(utils.get_population())


	country = input("Type country: ")
	country =  country.capitalize()

	result = utils.population_by_country(data, country)
	print(result)

# Este if nos da la posibilidad de manejar el archivo como un script, desde la terminal.
if __name__ == "__main__":
	run()