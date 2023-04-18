zen_file = open('zen.txt', 'r')

new_list = list()

for i_line in zen_file:
    new_list.append(i_line)

new_list.reverse()

zen_file.close()

print(''.join(new_list))

