origin_list = [1, 4, -3, 0, 10]
new_list = []
end = len(origin_list)
step = int(input('Сдвиг: '))

new_list.extend(origin_list[end - step:end] + origin_list[0:end - step])

print('Изначальный список: ', origin_list)
print('Сдвинутый список: ', new_list)