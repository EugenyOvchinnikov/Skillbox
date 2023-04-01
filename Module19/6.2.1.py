small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
item = input('Введите название товара: ')

if item not in big_storage:
    print('Такого товара нет')
else:
    print('{} - {} штук.'.format(
        item,
        big_storage.get(item)
    ))
