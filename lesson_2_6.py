shop = []

for clothes_index in range(2):
    name = input('Введите наменование товара: ')
    colour = input('Введите цвет товара: ')
    size = input('Введите размер: ')
    price = input('Введите цену: ')
    is_available = bool(int(input('Наличие: ')))
    clothes = {'name': name, 'colour': colour, 'size': size, 'price': price, 'is_available': is_available}

    shop.append(clothes)

obj_shop = enumerate(shop)
print(list(obj_shop))

output = {}

for clothes in shop:
    for key, value in clothes.items():
        output.setdefault(key, []).append(value)
print(output)
