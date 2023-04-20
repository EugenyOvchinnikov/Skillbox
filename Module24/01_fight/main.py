import random
import sys


class Warrior:
    health = 100
    name: str

    def print_info(self):
        print('{}, health {}'.format(self.name, self.health))


def attack(attacking: Warrior, victim: Warrior):
    """Функционал атаки"""
    print(f'{attacking.name}, attacks')
    victim.health -= 20
    victim.print_info()
    if victim.health <= 0:
        print(f'{attacking.name}, wins!')
        sys.exit()


user_1 = Warrior()
user_1.name = 'Warrior_1'
user_2 = Warrior()
user_2.name = 'Warrior_2'

while True:
    if random.choice((1, 2)) == 1:
        attack(user_1, user_2)
    else:
        attack(user_2, user_1)
# TODO здесь писать код
