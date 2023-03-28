import random
first_list = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_list = [round(random.uniform(5, 10), 2) for _ in range(20)]

winner_list = [(first_list[x]) if first_list[x] > second_list[x] else second_list[x] for x in range(20)]

print('Первая команда: ', first_list)
print('Вторая команда: ', second_list)
print('Победители тура :', winner_list)
