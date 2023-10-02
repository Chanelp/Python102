# Map aplica a cualquier objeto iterable
numbers = [2, 4, 6, 8]
numbers_v2 = list(map(lambda x:x*2, numbers))
print(numbers_v2)

n1 = [3, 5, 7, 9]
n2 = [2, 4, 6, 8]
both = list(map(lambda x, y: x * y, n1, n2))
print(both)