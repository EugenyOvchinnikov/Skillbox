ascii_en = [chr(i) for i in range(ord('a'), ord('z') + 1)]

text_file = open('text.txt', 'r')
text = text_file.read().lower()

count_en_letter = 0
letters_list = list()
letters_dict = dict()

for letter in text:     # Считаем общее количество английских букв в тексте
    if letter in ascii_en:
        count_en_letter += 1
        letters_list.append(letter)

text_file.close()

for sym in letters_list:    # Делаем частотный анализ
    if sym not in letters_dict:
        letters_dict[sym] = 1 / count_en_letter
    else:
        letters_dict[sym] += 1 / count_en_letter

letters_dict = dict(sorted(letters_dict.items(), key=lambda x: (-x[1], x[0])))  # Сортировка

analysis_file = open('analysis.txt', 'w')

for key in letters_dict:
    current_str = f'{key} - {round(letters_dict[key], 3)}'
    analysis_file.write(current_str + '\n')

analysis_file.close()
