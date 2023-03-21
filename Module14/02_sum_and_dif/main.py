def get_summ_of_digit(number):
    summ_of_digit = 0

    while number:
        summ_of_digit += number % 10
        number //= 10

    return summ_of_digit


def get_quantity_of_digit(number):
    quantity_of_digit = 0

    while number:
        quantity_of_digit += 1
        number //= 10

    return quantity_of_digit


my_number = int(input('Введите целое положительное число: '))
print(f'Сумма чисел: {get_summ_of_digit(my_number)}')
print(f'Количество цифр: {get_quantity_of_digit(my_number)}')
print(f'Разность суммы и количества цифр: {get_summ_of_digit(my_number) - get_quantity_of_digit(my_number)}')