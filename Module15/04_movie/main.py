films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', "Леон", \
         'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

quantity = int(input('Сколько фильмов хотите добавить? '))

my_list = []

for _ in range(quantity):
    film = input('Введите название фильма: ')
    if film in films:
        my_list.append(film)
    else:
        print(f'Ошибка: фильма {film} у нас нет :(')

print('Ваш список любимых фильмов:', end=' ')
print(*my_list, sep=', ')