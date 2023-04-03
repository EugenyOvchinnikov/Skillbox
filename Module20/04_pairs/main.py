import random

# Variant 1
my_list = [random.randint(1, 10) for _ in range(10)]
new_list = [(my_list[i], my_list[i + 1]) for i in range(0, len(my_list), 2)]

# Variant 2
my_list1 = list()
for _ in range(10):
    my_list1.append(random.randint(1, 10))

new_list1 = list()
for i in range(0, len(my_list1), 2):
    new_list1.append((my_list1[i], my_list1[i + 1]))

# Variant 3
my_list2 = list()
while len(my_list2) < 10:
    my_list2 += [random.randint(1, 10)]

new_list2 = list(zip(my_list2[::2], my_list2[1::2]))

print(my_list)
print(new_list, '\n')

print(my_list1)
print(new_list1, '\n')

print(my_list2)
print(new_list2)