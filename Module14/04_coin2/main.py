def check_point_inner_circle(x, y, radius):
    if x ** 2 + y ** 2 <= radius ** 2:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
my_x = float(input('X: '))
my_y = float(input('Y: '))
my_radius = int(input('Введите радиус: '))

check_point_inner_circle(my_x, my_y, my_radius)
