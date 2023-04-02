# number = int(input('Введите количество пар слов: '))
# synonym_dict = dict()
#
# for _ in range(number):
#     input_str = str(input('Введите пару: '))
#     synonym_list = input_str.split(' - ')
#     synonym_dict[synonym_list[0]] = synonym_list[1]
synonym_dict = {
    'Привет': 'Здравствуйте',
    'Печально': 'Грустно',
    'Весело': 'Радостно',
}

while True:
    word = str(input('Введите слово: '))
    if word not in synonym_dict and word not in synonym_dict.values():
        print('Такого слова в словаре нет')
    elif word in synonym_dict:
        print('Синоним :', synonym_dict[word])
        break
    else:
        print('Синоним :', list(synonym_dict.keys())[list(synonym_dict.values()).index(word)])
        break
