import csv

def read_csv(path):
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      total = 0

      for row in reader:
        total += int(row[1])
        
   return total

if __name__ == "__main__":
    response = read_csv('./app/gastos.csv')
    print(response)