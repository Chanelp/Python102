# Escribir en un archivo con r+
with open("./text.txt", "r+") as file:
    for line in file:
        print(line)
    file.write("\nIngles basico")
    file.write("\nLibro para aprender ignles >D")

# Sobre-escribir un archivo con w+
with open("./text.txt", 'w+') as file:
    for line in file:
        print(line)
    file.write("Sobreescribiendo todo!")