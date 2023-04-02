def solution():
    array_1 = [1, 5, 10, 20, 40, 80, 100]

    array_2 = [6, 7, 20, 80, 100]

    array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

    set_1 = set(array_1)
    set_2 = set(array_2)
    set_3 = set(array_3)

    array_intersection_123 = []
    for number in array_1:
        if number in array_2 and number in array_3:
            array_intersection_123.append(number)

    array_difference1_23 = []
    for number in array_1:
        if number not in array_2 and number not in array_3:
            array_difference1_23.append(number)

    print('Задача 1:')
    print('Решение без множеств:', array_intersection_123)
    print('Решение с множествами: {}'.format(
        set_1 & set_2 & set_3
    ))

    print('\nЗадача 2:')
    print('Решение без множеств:', array_difference1_23)
    print('Решение с множествами: {}'.format(
        set_1 - set_2 - set_3
    ))


solution()
