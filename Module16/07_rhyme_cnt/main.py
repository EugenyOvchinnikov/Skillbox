quan_people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый {0}-й человек'.format(
    number
))

man_list = list(range(1, quan_people + 1))

start_number = 0

while len(man_list) != 1:
    print('\nТекущий круг людей: ', man_list)
    print('Начало счёта с номера ', man_list[start_number])
    del_number = (start_number + number - 1) % len(man_list)
    print('Выбывает человек под номером ', man_list[del_number])
    man_list.pop(del_number)
    start_number = del_number % len(man_list)

print('Остался человек под номером ', man_list[0])