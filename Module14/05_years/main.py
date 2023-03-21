def check_years_three_identical_digit(first_year, second_year):
    if first_year > second_year:
        first_year, second_year = second_year, first_year

    for i in range(first_year, second_year + 1):
        first_digit = i // 1000
        second_digit = i // 100 % 10
        third_ditit = i // 10 % 10
        fourt_digit = i % 10
        if first_digit == second_digit == third_ditit != fourt_digit or first_digit == second_digit == fourt_digit != third_ditit \
            or first_digit == third_ditit == fourt_digit != second_digit or second_digit == third_ditit == fourt_digit != first_digit:
            print(i)


my_first_year = int(input('Введите первый год: '))
my_second_year = int(input('Введите второй год: '))
print(f'Годы от {my_first_year} до {my_second_year} с тремя одинаковыми цифрами: ')
check_years_three_identical_digit(my_first_year, my_second_year)



