from random import choice
import sys


class Warrior:
    def __init__(self, name: str):
        self.name = name
        self.health = 100

    def __str__(self):
        return '{} health {}'.format(self.name, self.health)

    def attack(self, attacking):
        print('{} attacks'.format(self.name))
        attacking.health -= 20
        print(attacking)
        if attacking.health <= 0:
            print('{} wins!'.format(self.name))
            sys.exit()


warrior_1 = Warrior('Warrior_1')
warrior_2 = Warrior('Warrior_2')

while True:
    if choice((1, 2)) == 1:
        warrior_1.attack(warrior_2)
    else:
        warrior_2.attack(warrior_1)
