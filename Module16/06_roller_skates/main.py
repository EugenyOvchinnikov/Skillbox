quan_skates = int(input('Количество коньков: '))
skates_list = []

for num_skate in range(quan_skates):
    num_skate_plus1 = num_skate + 1
    skates_list.append(int(input('Размер {0}-й пары: '.format(
        num_skate_plus1
    ))))

quan_people = int(input('\nКоличество людей: '))
people_list = []

for num_man in range(quan_people):
    num_man_plus1 = num_man + 1
    people_list.append(int(input('Размер ноги {0}-го человека: '.format(
        num_man_plus1
    ))))

quan_man_in_skate = 0
new_skates_list = skates_list[:]

for man_size in people_list:
    if man_size in new_skates_list:
        quan_man_in_skate += 1
        new_skates_list.remove(man_size)

print('\nНаибольшее количество людей, которые могут взять ролики: {0}'.format(
    quan_man_in_skate
))

