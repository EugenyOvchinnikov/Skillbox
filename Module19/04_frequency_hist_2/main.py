def get_freq_dict(text):
    text_dict = dict()
    for word in text:
        if word not in text_dict:
            text_dict[word] = 1
        else:
            text_dict[word] += 1

    return text_dict


def get_inverted_freq_dict(input_dict):
    inverted_input_dict = dict()
    for input_key in input_dict:
        word = input_key
        freq = input_dict[input_key]
        if freq not in inverted_input_dict:
            inverted_input_dict[freq] = [word]
        else:
            inverted_input_dict[freq].append(word)

    return inverted_input_dict


def print_dict(output_dict):
    for key in sorted(output_dict.keys()):
        print('{} : {}'.format(
            key,
            output_dict[key]
        ))


user_text = list(input('\nВведите текст: '))
freq_dict = get_freq_dict(user_text)
inverted_freq_dict = get_inverted_freq_dict(freq_dict)

print('\nОригинальный словарь частот:')
print_dict(freq_dict)
print('\nИнвертированный словарь частот:')
print_dict(inverted_freq_dict)

