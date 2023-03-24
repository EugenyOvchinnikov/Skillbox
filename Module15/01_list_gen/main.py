while True:
    number = int(input('Введите число: '))
    list_odd_numbers = []

    for i in range(1, number + 1, 2):
        list_odd_numbers.append(i)

    print(f'Список из нечётных чисел от 1 до {number}: {list_odd_numbers}')
