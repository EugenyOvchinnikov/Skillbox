violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

quantity_songs = int(input('Сколько песен выбрать? '))
length_songs = 0

for number in range(1, quantity_songs + 1):
    song_name = str(input('Название {0}-й песни: '.format(
        number
    )))
    length_songs += violator_songs.get(song_name)

print('Общее время звучания песен: {:.2f} минуты'.format(
    length_songs
))
