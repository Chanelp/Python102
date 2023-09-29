def find_volume(length=2, width=1, depth=1):
    return length * width * depth, width, "Encontrando volumen"

result = find_volume(width=9)
print(result)