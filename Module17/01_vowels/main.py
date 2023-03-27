def if_vowel_word(test_word):
    vowel_list = ["а", "е", "ё", "и", "о", "у", "ы" "э", "ю", "я"]
    if test_word in vowel_list:
        return True
    else:
        return False


my_string = str(input('Введите текст:'))

vowel_word_string = [word for word in my_string if if_vowel_word(word)]

print('Список гласных букв: ', vowel_word_string)
print('Длина списка: ', len(vowel_word_string))
