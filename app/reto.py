import utils
import read_csv as csv
import charts

def run():
  data = csv.read_csv("./app/data.csv")
  names, values = utils.get_world_population_percentage(data)
  charts.generate_pie_chart(names, values)

if __name__ == "__main__":
	run()