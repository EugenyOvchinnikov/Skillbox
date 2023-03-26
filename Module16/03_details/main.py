shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

part_name = str(input('Название детали: '))
count_parts = 0
cost_parts = 0

for i_part in shop:
    if i_part[0] == part_name:
        count_parts += 1
        cost_parts += i_part[1]

print('Количество деталей - ', count_parts)
print('Общая стоимость - ', cost_parts)
