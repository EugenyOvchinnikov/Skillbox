numbers_file = open('numbers.txt', 'r')

total_sum = 0

for i_line in numbers_file:
    total_sum += sum([int(s) for s in i_line.split() if s.isdigit()])

numbers_file.close()
answer_file = open('answer.txt', 'w')
answer_file.write(str(total_sum))
answer_file.close()
