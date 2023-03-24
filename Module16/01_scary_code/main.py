master_list = [1, 5, 3]
first_slave_list = [1, 5, 1, 5]
second_slave_list = [1, 3, 1, 5, 3, 3]

master_list.extend(first_slave_list)
quantity_5 = master_list.count(5)

for _ in range(quantity_5):
    master_list.remove(5)

master_list.extend(second_slave_list)
quantity_3 = master_list.count(3)

print('Количество цифр 5 при первом объединении: ', quantity_5)
print('Количество цифр 3 при втором объединении: ', quantity_3)
print('Итоговый список: ', master_list)
