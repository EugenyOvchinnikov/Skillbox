import os.path


class FindFolder(Exception):
    pass


def gen_files_path(link: str, search: str):
    for links, dirs, files in list(os.walk(link)):
        for _dir in dirs:
            if _dir == search:
                raise FindFolder(f'Каталог {search} найден')
        for file in files:
            yield links + '\\' + file


if __name__ == '__main__':
    # path_search = input("Введите путь для поиска: ")
    path_search = 'C:\\Users\\john\\PycharmProjects'
    # folder_search = input("Какой каталог будем искать? ")
    folder_search = 'Module15'

    my_iter = gen_files_path(path_search, folder_search)

    try:
        while True:
            print(next(my_iter))
    except FindFolder as exc:
        print(exc)
    except StopIteration:
        print(f'Каталог {folder_search} не найден')
