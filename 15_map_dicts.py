items = [
    {
        'product':'camisa',
        'price':100
    },
    {
        'product':'pantalon',
        'price':120
    },
    {
        'product':'tenis',
        'price':150
    }
]

prices = list(map(lambda item:item['price'], items))
print(prices)

# Adding a new atribute to the dict
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)