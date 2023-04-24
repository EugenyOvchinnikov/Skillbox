import random


class Parent:
    def __init__(self, name, age, children_name_list):
        self.name = name
        self.age = age
        self.children_list = [Child(child_name, age - 16 - random.randint(0, age - 16)) for child_name in children_name_list]

    def print_state(self):
        print('\nРодитель {}, {} лет'.format(self.name, self.age))
        print('Дети:')
        print(*self.children_list, sep='\n')

    def feed_child(self, child_id):
        child = self.children_list[child_id]
        if child.hungry == 0:
            child.hungry += 1
            print('\nРебёнок', child.name, 'накормлен')
        else:
            print('\nРебёнок', child.name, 'не голоден')

    def calm_down_child(self, child_id):
        child = self.children_list[child_id]
        if child.calm == 0:
            child.calm += 1
            print('\nРебёнок', child.name, 'успокоен')
        else:
            print('\nРебёнок', child.name, 'не нервничает')


class Child:
    state_of_calm = {1: 'Спокоен', 0: 'Нервничает'}
    state_of_hunger = {1: 'Сыт', 0: 'Голоден'}

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


parent1 = Parent('Петя', 40, ['Вася', 'Коля'])
parent1.print_state()
parent1.feed_child(0)
parent1.feed_child(1)
parent1.calm_down_child(0)
parent1.calm_down_child(1)
parent1.print_state()