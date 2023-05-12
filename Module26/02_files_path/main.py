import os.path


class FindFolder(Exception):
    pass


def gen_files_path(link: str, search: str):
    for links, dirs, files in list(os.walk(link)):
        for file in files:
            if links.split('\\')[-1] == search:
                raise FindFolder('каталог найден')
            else:
                yield links + '\\' + file


if __name__ == '__main__':
    # path_search = input("Введите путь для поиска: ")
    path_search = 'C:\\Users\\john\\PycharmProjects'
    # folder_search = input("Какой каталог будем искать? ")
    folder_search = 'Module155'

    my_iter = gen_files_path(path_search, folder_search)

    try:
        while True:
            print(next(my_iter))
    except FindFolder as exc:
        print(exc)
    except StopIteration:
        print('каталог не найден')
