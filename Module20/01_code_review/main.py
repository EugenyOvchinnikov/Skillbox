students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def get_interests_and_surnames_length(my_dict):
    interests = set()
    length = 0
    for i_student in my_dict:
        interests = interests | set(my_dict[i_student].get('interests'))
        length += len(my_dict[i_student].get('surname'))
    return interests, length


pairs_list = list()
for id_student in students:
    pairs_list.append((id_student, students[id_student].get('age')))
print('Список пар "ID-студента - возраст": {}'.format(
    pairs_list
))

interests_list = get_interests_and_surnames_length(students)[0]
surnames_length = get_interests_and_surnames_length(students)[1]

print('Полный список интересов всех студентов: {}'.format(
    interests_list
))
print('Общая длина всех фамилий студентов: {}'.format(
    surnames_length
))
