site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key_in_dict(my_dict, key, depth):
    result = None
    if key in my_dict and (depth is None or depth >= 1):
        return my_dict[key]
    if depth is not None and depth >= 1:
        for sub_dict in my_dict.values():
            if isinstance(sub_dict, dict):
                result = find_key_in_dict(sub_dict, key, depth - 1)
            if result:
                break
    elif depth is None:
        for sub_dict in my_dict.values():
            if isinstance(sub_dict, dict):
                result = find_key_in_dict(sub_dict, key, depth)
            if result:
                break

    return result


user_key = input('Введите искомый ключ: ')

choice = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if choice == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
else:
    max_depth = None

if max_depth == 0:
    value = None
else:
    value = find_key_in_dict(site, user_key, max_depth)
print('Значение ключа: ', value)
