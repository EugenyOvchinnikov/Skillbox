def tpl_sort(origin_tuple):
    list_int = list(i_elem for i_elem in origin_tuple if type(i_elem) == int)

    if len(list_int) != len(origin_tuple):
        print('Один или несколько элементов кортежа не является целым числом')
        return origin_tuple
    else:
        return tuple(sorted(list_int))


# tpl = (6, 3, -1, 8, 4, 10, -5)
# tpl = (6, 3, -1, 8, 4, 10.5, -5)
# tpl = (6, 3, -1, 8, 4, "10", -5)
#
# print(tpl_sort(tpl))
