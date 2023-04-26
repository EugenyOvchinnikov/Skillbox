import random
import sys


class Warrior:
    def __init__(self, name: str):
        self.name = name
        self.health = 100

    def __str__(self):
        return '{} health {}'.format(self.name, self.health)


def attack(attacking: Warrior, victim: Warrior):
    """Функционал атаки"""
    print('{} attacks'.format(attacking))
    victim.health -= 20
    print(victim)
    if victim.health <= 0:
        print('{} wins!'.format(attacking))
        sys.exit()


warrior_1 = Warrior('Warrior_1')
warrior_2 = Warrior('Warrior_2')

while True:
    if random.choice((1, 2)) == 1:
        attack(warrior_1, warrior_2)
    else:
        attack(warrior_2, warrior_1)
