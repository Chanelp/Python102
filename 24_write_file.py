# Escribir en un archivo
with open("./text.txt", "r+") as file:
    for line in file:
        print(line)
    file.write("\nIngles basico")
    file.write("\nLibro para aprender ignles >D")

# Sobre-escribir en el archivo
with open("./text.txt", 'w+') as file:
    for line in file:
        print(line)
    file.write("Sobreescribiendo todo!")