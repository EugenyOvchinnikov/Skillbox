from collections.abc import Iterable


class Square:
    """ Класс итератор """
    __current_number = 0

    def __init__(self, number: int) -> None:
        self.__number = number

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> int:
        Square.__current_number += 1
        if Square.__current_number > self.__number:
            raise StopIteration
        else:
            return Square.__current_number ** 2


# функция-генератор
def squares():
    n = 1
    while True:
        yield n ** 2
        n += 1


if __name__ == '__main__':
    my_number = int(input('Введите число N: '))

    # Используем класс-итератор
    my_iter = Square(my_number)

    for i_elem in my_iter:
        print(i_elem, end=' ')

    # Используем функцию-генератор
    print()
    my_iter2 = squares()
    for _ in range(my_number):
        print(next(my_iter2), end=' ')

    # Генераторное выражение
    my_iter3 = (i ** 2 for i in range(1, my_number + 1))

    print()
    for i_elem in my_iter3:
        print(i_elem, end=' ')
