def form_next_tour(current_tour, next_tour):
    from operator import itemgetter

    current_tour_file = open(current_tour, 'r')

    members_list = list()
    passing_score = int(current_tour_file.readline())

    for i_line in current_tour_file:    # Вывод участников с баллом больше проходного в список
        current_score = int(i_line.split()[-1])     # баллы текущего участника
        if current_score > passing_score:
            members_list.append(i_line.split())

    current_tour_file.close()

    members_list.sort(key=itemgetter(2), reverse=True)  # Сортируем по убыванию баллов

    next_tour_file = open(next_tour, 'w')
    next_tour_file.write(str(len(members_list)) + '\n')   # Выводим количество прошедших участников

    for value in members_list:
        current_str = '{}. {} {}'.format(
            str(value[1][0]),   # Имя
            str(value[0]),  # Фамилия
            str(value[2]))  # баллы
        next_tour_file.write(current_str + '\n')

    next_tour_file.close()


form_next_tour('first_tour.txt', 'second_tour.txt')