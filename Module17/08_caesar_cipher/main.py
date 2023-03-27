def get_index(my_sym, my_step, lst):
    index = lst.index(my_sym)
    if index + my_step > len(lst) - 1:
        index = index + step - len(lst)
    else:
        index += step
    return index


text = input('Введите сообщение: ').lower()
step = int(input('Введите сдвиг: '))

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

encrypted_text = ''

for sym in text:
    if sym in alphabet:
        encrypted_text += alphabet[get_index(sym, step, alphabet)]
    else:
        encrypted_text += sym

print(encrypted_text)
