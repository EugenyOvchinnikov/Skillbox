my_list = 'abcd'
my_tuple = (10, 20, 30, 40)

split = ((my_list[i], my_tuple[i]) for i in range(len(my_list)))

print(split)
print(*split, sep='\n')
