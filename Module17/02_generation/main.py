number = int(input('Введите целое число: '))

user_list = [(1 if x % 2 == 0 else x % 5) for x in range(number)]

print(user_list)
