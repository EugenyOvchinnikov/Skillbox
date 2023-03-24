origin_word = []
origin_word.extend(input('Введите слово: '))

reverse_word = origin_word[::-1]

if origin_word == reverse_word:
    print('Слово является полиндромом')
else:
    print('Слово не является полиндромом')