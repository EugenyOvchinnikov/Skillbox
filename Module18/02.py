import re
# string = str(input('Введите строку: '))
# string = 'я есть строка.'
# string = 'а б.'
string = 'б.'

string_list = re.split('[ .]', string)

max_length = 0
max_word = ''

for word in string_list:
    if len(word) > max_length:
        max_length = len(word)
        max_word = word

print('Самое длинное слово «{}»'.format(max_word))
print('Длина этого слова {} символов.'.format(max_length))
