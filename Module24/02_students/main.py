import random


class Student:
    def __init__(self, name, group_number, scores):
        self.name = name
        self.group_number = group_number
        self.scores = scores

    def __str__(self):
        return f'{self.name} {self.group_number} {self.scores} {self.get_gpa()}'

    def get_gpa(self):
        return sum(self.scores) / len(self.scores)


student_list = list()

for i in range(10):
    student_name = 'student' + str(i + 1)
    student_group_number = random.randint(400, 500)
    student_scores = [random.randint(1, 5) for _ in range(5)]
    student_list.append(Student(student_name, student_group_number, student_scores))

sorted_student_list = sorted(student_list, key=lambda x: x.get_gpa())
print(*sorted_student_list, sep='\n')
