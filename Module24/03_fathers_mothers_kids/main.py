import random


class Parent:
    def __init__(self, name, age, children_name_list):
        self.name = name
        self.age = age
        self.children_dict = {child_name: Child(child_name, age - 16 - random.randint(0, age - 16)) for child_name in children_name_list}

    def print_state(self):
        print('\nРодитель {}, {} лет'.format(self.name, self.age))
        print('Дети:')
        print(*self.children_dict.values(), sep='\n')

    def feed_child(self, child_name: str):
        """Покормить ребёнка"""
        child = self.children_dict[child_name]
        if child.hungry == 0:
            child.hungry += 1
            print('\nРебёнок', child.name, 'накормлен')
        else:
            print('\nРебёнок', child.name, 'не голоден')

    def calm_down_child(self, child_name: str):
        """Успокоить ребёнка"""
        child = self.children_dict[child_name]
        if child.calm == 0:
            child.calm += 1
            print('\nРебёнок', child.name, 'успокоен')
        else:
            print('\nРебёнок', child.name, 'не нервничает')


class Child:
    state_of_calm = {0: 'Нервничает', 1: 'Спокоен'}
    state_of_hunger = {0: 'Голоден', 1: 'Сыт'}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = random.randint(0, 1)
        self.calm = random.randint(0, 1)

    def __str__(self):
        return 'Ребёнок {}, {} лет, {}, {}'.format(
            self.name,
            self.age,
            self.state_of_calm[self.calm],
            self.state_of_hunger[self.hungry])


petya = Parent('Петя', 40, ['Вася', 'Коля'])
petya.print_state()
petya.feed_child('Вася')
petya.feed_child('Коля')
petya.calm_down_child('Вася')
petya.calm_down_child('Коля')
petya.print_state()
