import os


def get_file_list(cur_path, _sum_files=0, _sum_directory=0, _total_size=0):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isfile(path):    # если файл, считаем количество и размер
            _sum_files += 1
            _total_size += os.path.getsize(path)
        else:
            _sum_directory += 1     # если каталог, считаем количество и идём внутрь каталога
            _sum_files, _sum_directory, _total_size = get_file_list(path, _sum_files, _sum_directory, _total_size)

    return _sum_files, _sum_directory, _total_size


folder_name = 'Module14'
abs_path = os.path.abspath(os.path.join('..', '..', folder_name))

sum_files, sum_directory, total_size = get_file_list(abs_path)
print('Размер каталога в (Кбайтах)', total_size / 1024)
print('Количество подкаталогов', sum_directory)
print('Количество файлов', sum_files)



