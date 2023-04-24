class Water:
    name = 'Вода'

    def __add__(self, other):
        match other:
            case Air():
                return Storm()
            case Fire():
                return Steam()
            case Earth():
                return Dirt()


class Air:
    name = 'Воздух'

    def __add__(self, other):
        match other:
            case Fire():
                return Lightning()
            case Earth():
                return Dust()


class Fire:
    name = 'Огонь'

    def __add__(self, other):
        match other:
            case Earth():
                return Lava()


class Earth:
    name = 'Земля'


class Storm:
    name = 'Щторм'

    def __str__(self):
        return self.name


class Steam:
    name = 'Пар'

    def __str__(self):
        return self.name


class Dirt:
    name = 'Грязь'

    def __str__(self):
        return self.name


class Lightning:
    name = 'Молния'

    def __str__(self):
        return self.name


class Dust:
    name = 'Пыль'

    def __str__(self):
        return self.name


class Lava:
    name = 'Лава'

    def __str__(self):
        return self.name


print(Water() + Fire())
print(Fire() + Earth())
print(Fire() + Dust())