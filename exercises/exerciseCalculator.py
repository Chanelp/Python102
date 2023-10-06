def calculator(fA, fB, option):
    if option == '+':
        print('The adition is equal to: ', fA + fB)
    elif option == '-':
        print('The substraction is equal to: ', fA - fB)
    elif option == '*':
        print('The multiplication is equal to: ', fA * fB)
    elif option == '/':
        print('The division is equal to: ', fA / fB)

numA = int(input('Choose a number: '))
numB = int(input('Choose another one: '))

list_options = ('+', '-', '*', '/')
option = str(input(f'Choose operator with symbol: \n{list_options} --> '))

calculator(numA, numB, option)