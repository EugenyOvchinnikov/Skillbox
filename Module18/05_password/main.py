def check_passwd(my_passwd):
    ascii_en_up = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    numbers_list = [number for number in range(10)]
    count_ascii_en_up_symbol = 0  # счётчик прописных букв
    count_number = 0  # счётчик цифр

    if len(my_passwd) < 8:
        return False
    else:
        for char in my_passwd:
            if char in ascii_en_up:
                count_ascii_en_up_symbol += 1
            elif char in numbers_list:
                count_number += 1
        if count_ascii_en_up_symbol < 1 and count_number < 3:
            return False
        else:
            return True


while True:
    passwd = str(input('Введите пароль: '))
    if check_passwd(passwd):
        print('Это надёжный пароль.')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
