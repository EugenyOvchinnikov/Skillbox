import json
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def get_new_dict(my_dict, my_key, meaning):
    if my_key in my_dict:
        my_dict[my_key] = meaning
        return 1

    for sub_dict in my_dict.values():
        if isinstance(sub_dict, dict):
            result = get_new_dict(sub_dict, my_key, meaning)
            if result:
                return 1


number_sites = int(input('Сколько сайтов: '))
site_list = dict()

for _ in range(number_sites):
    product_name = input('Введите название продукта для нового сайта: ')
    key_list = {'title': f'Куплю/продам {product_name} недорого',
                'h2': f'У нас самая низкая цена на {product_name}'}

    for i_key, i_value in key_list.items():
        get_new_dict(site, i_key, i_value)  # Создаём новый сайт из шаблона site
    site_list[product_name] = copy.deepcopy(site)  # Добавляем копию сайта в список для печати

    for key, value in site_list.items():
        print('Сайт для', key)
        print('site =', json.dumps(value, indent=8, ensure_ascii=False))
