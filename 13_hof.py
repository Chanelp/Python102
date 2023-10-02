def increment(x):
    return x + 1

def higher_order_funct(x, funct):
    return x + funct(x)

result = higher_order_funct(3, increment)
print(result)

# Higher order function using lambdas
increment_v2 = lambda x:x+1
hof_v2 = lambda x, funct:x+funct(x)

result2 = hof_v2(4, increment_v2)
print(result2)