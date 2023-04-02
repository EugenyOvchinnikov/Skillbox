def is_prime(my_number):
    k = 0
    for iterator in range(2, my_number // 2 + 1):
        if my_number % iterator == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False


while True:
    number = int(input('Введите число: '))
    print(is_prime(number))