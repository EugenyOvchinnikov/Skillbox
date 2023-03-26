def swap_by_index(my_list, first_index, second_index):
    my_list[first_index], my_list[second_index] = my_list[second_index], my_list[first_index]


def get_sort_list(my_list):
    n = int(len(my_list))

    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j + 1]:
                swap_by_index(my_list, j, j + 1)
                swapped = True
        if not swapped:
            break


first_class_list = list(range(160, 178, 2))
second_class_list = list(range(162, 183, 3))
general_list = first_class_list + second_class_list

get_sort_list(general_list)
print('Отсортированный список учеников', general_list)

