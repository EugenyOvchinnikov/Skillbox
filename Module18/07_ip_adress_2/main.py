def ip_adress_check(my_ip):
    ip_adress_list = my_ip.split('.')
    if len(ip_adress_list) < 4:
        print('Адрес — это четыре числа, разделённые точками')
        return False
    else:
        for group in ip_adress_list:
            try:
                n = int(group)
            except ValueError:
                print(group, 'это не целое число')
                return False
            if n > 255:
                print(group, 'превышает 255')
                return False
    return True


while True:
    ip_adress = str(input('Введите IP: '))
    if ip_adress_check(ip_adress):
        print('IP-адрес корректен.')
        break
