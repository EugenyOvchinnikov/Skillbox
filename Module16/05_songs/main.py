violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

quantity_songs = int(input('Сколько песен выбрать? '))
lengt_songs = 0
new_list =[]

for number in range(quantity_songs):
    number_plus1 = number + 1
    song_name = str(input('Название {0}-й песни: '.format(
        number_plus1
    )))
    for song in violator_songs:
        if song[0] == song_name:
            new_list.append(song)
            lengt_songs += song[1]

round(lengt_songs, 2)
print('Общее время звучания песен: {0} минуты'.format(
    lengt_songs
    ))