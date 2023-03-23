quantity_cards = int(input('Количество видеокарт: '))
list_cards = []
max_card_number = 0

for i in range(quantity_cards):
    list_cards.append(int(input(f'Видеокарта {i + 1}: ')))
    if list_cards[i] > max_card_number:
        max_card_number = list_cards[i] # Сразу находим максимальное значение

new_list_cards = []
for number in list_cards:
    if number != max_card_number:
        new_list_cards.append(number)

print(f'Старый список видеокарт: {list_cards}')
print(f'Новый список видеокарт: {new_list_cards}')


