def input_int_in_range(start, end, user_text):
    while True:
        try:
            n = int(input(user_text))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        else:
            if start <= n <= end:
                return n
            print("Введённое число вне диапазона: [%d, %d]" % (start, end))


quantity_cases = int(input('Количество контейнеров: '))
list_cases = []

for _ in range(quantity_cases):
    case = input_int_in_range(1, 200, "Введите вес контейнера: ")
    list_cases.append(case)

new_case = input_int_in_range(1, 200, "Введите вес нового контейнера: ")

for i_case in range(quantity_cases):
    if list_cases[i_case] < new_case:
        list_cases.insert(i_case, new_case)
        print(f'Номер, который получит новый контейнер: {i_case + 1}')
        break
else:
    list_cases.append(new_case)
    print(f'Номер, который получит новый контейнер: {quantity_cases + 1}')

# print(list_cases)