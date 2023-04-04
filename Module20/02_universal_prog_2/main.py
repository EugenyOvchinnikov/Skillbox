def is_prime(my_number):
    if my_number < 2:
        return False
    for iterator in range(2, my_number // 2 + 1):
        if my_number % iterator == 0:
            return False
    return True


def crypto(obj):
    # list_values_of_prime_index = []
    # for i, value in enumerate(obj):
    #     if is_prime(i):
    #         list_values_of_prime_index.append(value)
    # return list_values_of_prime_index
    return [value for i, value in enumerate(obj) if is_prime(i)]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))
