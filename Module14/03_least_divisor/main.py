def get_minimal_divider(number):
    minimal_divider = number
    for i in range(number - 1, 1, -1):
        if number % i == 0:
            minimal_divider = i

    return minimal_divider


my_number = int(input('Введите число: '))
print(f'Наименьший делитель, отличный от единицы: {get_minimal_divider(my_number)}')