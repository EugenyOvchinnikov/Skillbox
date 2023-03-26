guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')

    status_guest = str(input('Гость пришёл или ушёл? '))
    if status_guest == "Пора спать":
        break

    name_guest = str(input('Имя гостя: '))

    if status_guest == "ушёл":
        if guests.count(name_guest) > 0: # есть ли такой гость на вечеринке
            guests.remove(name_guest)
            print(f'Пока, {name_guest}!')
        else:
            print(f'Гостя {name_guest}, на вечеринке нет')
    elif status_guest == "пришёл" and len(guests) < 6:
        guests.append(name_guest)
    elif status_guest == "пришёл" and len(guests) == 6:
        print(f'Прости, {name_guest}, но мест нет.')

    print()

print('Вечеринка закончилась, все легли спать.')
