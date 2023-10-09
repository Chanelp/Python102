file = open("./text.txt")

for line in file:
    print(file.readline())

file.close()

# Open and close de file 
with open("./text.txt") as file:
    for line in file:
        print(line)