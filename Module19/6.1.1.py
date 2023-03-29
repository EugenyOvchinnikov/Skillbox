# Результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
num = int(input('Введите число: '))

quad_dict = {index: index ** 2 for index in range(1, num + 1)}

print(quad_dict)