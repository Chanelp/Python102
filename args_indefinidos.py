# POSITIONAL ARGUMENTS
def sum_multiple(*args):
    return sum(args)

# KEYWORD ARGUMENTS
def personal_information(**kargs):
    for k, v in kargs.items():
        print(f"{k} > {v}")

personal_information(name="Chanel", lastname="Paredes", age=21)
print(sum_multiple(3, 5, 6, 8, 2, 1))