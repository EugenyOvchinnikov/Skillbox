# Функция меняет местами элементы по их индексам
def swap(my_list, first_index, second_index):
    my_list[first_index], my_list[second_index] = my_list[second_index], my_list[first_index]


origin_list = [1, 4, -3, 0, 10]
print('Изначальный список: ', origin_list)
# Сортировка пузырьком
n = int(len(origin_list))
swapped = False

for i in range(0, n - 1):
    swapped = False
    for j in range(0, n - 1 - i):
        if origin_list[j] > origin_list[j + 1]:
            swap(origin_list, j, j + 1)
            swapped = True
            if not swapped:
                break

print('Отсортированный список:', origin_list)