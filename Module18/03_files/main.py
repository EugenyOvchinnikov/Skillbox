# file_name = str(input('Название файла:'))
# file_name = '@example.txt'
# file_name = 'example.ttx'
file_name = 'example.txt'
file_extension = ('.txt', '.docx')
special_symbol = ('@', '№', '$', '%', '^', '&', '*', '(', ')')

if file_name.startswith(special_symbol):
    print('Ошибка: название начинается недопустимым символом')
elif not file_name.endswith(file_extension):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
