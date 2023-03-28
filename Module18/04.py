text_line = 'Кажется, я забыл выключить утюг.'
text_list = text_line.split()

for i, word in enumerate(text_list):
    text_list[i] = word[0:1].upper() + word[1:]

new_text_line = ' '.join(text_list)

print('Результат:', new_text_line)