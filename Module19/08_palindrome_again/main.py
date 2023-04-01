def check_for_palindrome(input_text):
    input_text_set = set()

    for word in input_text:
        if word in input_text_set:
            input_text_set.remove(word)
        else:
            input_text_set.add(word)

    return (True, False)[len(input_text_set) > 1]


text = input('Введите строку: ')

print(('Нельзя', 'Можно')[check_for_palindrome(text)], 'сделать палиндром')
