words_ones = ['', 'первый', 'второй', 'третий', 'четвёрый', 'пятый',
              'шестой', 'седьмой', 'восьмой', 'девятый']

words_teens = ['', 'одиннадцатый', 'двенадцатый', 'тринадцатый',
               'четырнадцатый', 'пятнадцатый', 'шестнадцатый',
               'семнадцатый', 'восемнадцатый', 'девятнадцатый']

words_tens = ['', '', 'двадцать', 'тридцать', 'сорок',
              'пятьдесят', 'шестьдесят', 'семьдесят',
              'восемьдесят', 'девяносто']

words_dozens = ['', 'десятый', 'двадцатый', 'тридцатый', 'сороковой',
                'пятидесятый', 'шестидесятый', 'семидесятый', 'восьмидесятый',
                'девяностый']


def chislo_slovami(num):
    if 10 < num < 20:
        return words_teens[num - 10]

    if not num % 10:
        return words_dozens[num // 10]

    ones_word = words_ones[num % 10]
    tens_word = words_tens[num // 10]

    return (tens_word + ' ' + ones_word).strip()


number = int(input('Введите количество заказов: '))
orders_dict = dict()

input_list = ['Иванов Пепперони 1', 'Петров Де-Люкс 2', 'Иванов Мясная 3',
              'Иванов Мексиканская 2', 'Иванов Пепперони 2', 'Петров Интересная 5']

for i in range(number):
    # order_list = (input(f'{chislo_slovami(i + 1).capitalize()} заказ: ')).split(' ')
    order_list = input_list[i].split(' ')
    customer = order_list[0]
    pizza_name = order_list[1]
    quantity = int(order_list[2])

    if customer not in orders_dict:
        orders_dict[customer] = {pizza_name: quantity}
    elif pizza_name not in orders_dict[customer]:
        orders_dict[customer][pizza_name] = quantity
    else:
        orders_dict[customer][pizza_name] += quantity

print()
for customer in sorted(orders_dict.keys()):
    print(f'{customer}:')
    for pizza_name in sorted(orders_dict[customer].keys()):
        print(f'     {pizza_name}: {orders_dict[customer][pizza_name]}')