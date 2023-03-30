def get_total_quantity_and_cost(my_store):  # сумма количества номенклатуры по всем складам и общая стоимость
    total_quantity = 0
    total_cost = 0

    for i_dict in my_store:
        total_quantity += i_dict['quantity']
        total_cost += i_dict['quantity'] * i_dict['price']

    return total_quantity, total_cost


def get_ruble(number):  # склонение рубля от стоимости
    if 5 <= number <= 20:
        return 'рублей'
    elif number % 10 == 1:
        return 'рубль'
    elif number % 10 in (2, 3, 4):
        return 'рубля'
    else:
        return 'рублей'


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for item in goods:
    res = get_total_quantity_and_cost(store[goods[item]])
    print('{} - {} штук, стоимость {} {}'.format(
        item,
        res[0],
        res[1],
        get_ruble(res[1])
    ))
