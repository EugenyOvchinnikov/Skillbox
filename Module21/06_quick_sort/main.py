def get_three_lists(my_list, list_l, list_m, list_r):
    reference_elem = my_list[-1]
    for elem in my_list:
        if elem < reference_elem:
            list_l.append(elem)
        elif elem == reference_elem:
            list_m.append(elem)
        else:
            list_r.append(elem)

    return list_l, list_m, list_r


def qsort(arr):
    list_left = list()
    list_middle = list()
    list_right = list()
    if len(arr) <= 1:
        return arr
    get_three_lists(arr, list_left, list_middle, list_right)
    return qsort(list_left) + list_middle + qsort(list_right)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 4]
print(qsort(list1))

