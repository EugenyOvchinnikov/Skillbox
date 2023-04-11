nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def get_simple_list(my_list, new_list=None):
    if new_list is None:
        new_list = list()
    for elem in my_list:
        if isinstance(elem, list):
            get_simple_list(elem, new_list)
        else:
            new_list.append(elem)

    return new_list


print('Ответ:', get_simple_list(nice_list))
