def print_from_one_to_num(num):
    if num <= 0:
        return 1
    print_from_one_to_num(num - 1)
    print(num)


number = int(input('Введите число: '))
print_from_one_to_num(number)
