def get_sum_list(*args):
    summa = 0
    for arg in args:
        if isinstance(arg, list):
            summa += get_sum_list(*arg)
        else:
            summa += arg

    return summa


# list1 = [1, 2, 3, 4, 5]
# list2 = [[[1, 2, [3]], [1], 3]]
#
# print(get_sum_list(list1), get_sum_list(list2), sep='\n')
