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


def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_products = list(map(add_taxes, items))

print("OLD DICT")
print(items)

print('NEW DICT')
print(new_products)