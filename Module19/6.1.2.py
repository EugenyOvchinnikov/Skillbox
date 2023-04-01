user_list = input('Введите информацию через пробел: ')

user_info = user_list.split()

user_dict = dict()

user_dict['Имя'] = user_info[0]
user_dict['Фамилия'] = user_info[1]
user_dict['Oценки'] = []

for i_grade in user_info[2:]:
    user_dict['Oценки'].append(int(i_grade))

for i_info in user_dict:
    print(i_info, '-', user_dict[i_info])