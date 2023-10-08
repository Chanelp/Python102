try:
    print(1/2)

    assert 1 == 1, 'Uno no es igual a uno'

    age = 12
    if age < 18:
        raise Exception("No se admiten menores de edad! + 18")
    
except ZeroDivisionError as error:
    print(error)
    
except AssertionError as error:
    print(error)
    
except Exception as error:
    print(error)

print("Hi")