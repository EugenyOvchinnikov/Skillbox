names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
even_names_list = []

for i in range(0, len(names_list), 2):
    even_names_list.append(names_list[i])

print('Первый день:', even_names_list)
