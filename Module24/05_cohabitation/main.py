import random
import sys


class Home:
    food = 50
    money = 0

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return 'Дом по адресу: {}'.format(self.name)

    def get_state(self):
        return 'В доме по адресу: {} осталось {} еды и {} денег'.format(self.name, self.food, self.money)


class Human:
    state_of_hunger = 50

    def __init__(self, name: str, my_home: Home):
        self.name = name
        self.my_home = my_home

    def __str__(self):
        return f'{self.name}, степень сытости - {self.state_of_hunger}'

    def eat(self):
        if self.my_home.food > 0:
            self.state_of_hunger += 1
            self.my_home.food -= 1
            print('\nЧеловек {} поел, степень сытости {}'.format(self.name, self.state_of_hunger))
            print('В доме {} осталось {} еды'.format(self.my_home, self.my_home.food))
        else:
            print('Еды в доме нет!')

    def work(self, energy_consumption, perfomance):
        self.state_of_hunger -= energy_consumption
        self.my_home.money += perfomance
        print('\nЧеловек {} поработал, степень сытости {}'.format(self.name, self.state_of_hunger))
        print('В доме {} стало {} денег'.format(self.my_home, self.my_home.money))
        if self.state_of_hunger < 0:
            sys.exit('Человек {} умер!'.format(self.name))

    def play(self, energy_consumption):
        self.state_of_hunger -= energy_consumption
        print('\nЧеловек {} поиграл, степень сытости {}'.format(self.name, self.state_of_hunger))
        if self.state_of_hunger < 0:
            sys.exit('Человек {} умер!'.format(self.name))

    def buy_food(self):
        if self.my_home.money > 0:
            self.my_home.money -= 1
            self.my_home.food += 1
            print('\nЧеловек {} купил еду'.format(self.name))
            print('В доме {} стало {} еды и {} денег'.format(self.my_home, self.my_home.food, self.my_home.money))
        else:
            print('\nДенег на покупку еды нет')

    def live_one_day(self):
        energy_consumtion = random.randint(1, 21)   # Декремент уровня сытости
        perfomance = random.randint(1, 20)  # Инкремент денег
        dice = random.randint(1, 6)
        if self.state_of_hunger < 20:
            if self.my_home.food > 0:
                self.eat()
            elif self.my_home.money > 0:
                self.buy_food()
            else:
                self.work(energy_consumtion, perfomance)
        elif self.my_home.food < 10:
            if self.my_home.money > 0:
                self.buy_food()
            else:
                self.work(energy_consumtion, perfomance)
        elif self.my_home.money < 50:
            self.work(energy_consumtion, perfomance)
        elif dice == 1:
            self.work(energy_consumtion, perfomance)
        elif dice == 2:
            self.eat()
        else:
            self.play(energy_consumtion)


home1 = Home('Заречная 6')
vasya = Human('Вася', home1)
petya = Human('Петя', home1)

for day_number in range(1, 366):    # Пытаемся прожить 1 год
    print('\nДень', day_number)
    vasya.live_one_day()
    petya.live_one_day()

print('\nЧеловек', vasya, 'прожил 365 дней')
print('\nЧеловек', petya, 'прожил 365 дней\n')
print(home1.get_state())



