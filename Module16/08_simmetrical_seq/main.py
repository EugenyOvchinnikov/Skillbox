numbers = int(input('Количество чисел: '))
user_list = []
reverse_list = []
for _ in range(numbers):
    user_list.append(int(input('Число: ')))

print('Последовательность: ', user_list)

for i in range(len(user_list)):
    reverse_list = user_list[i:]
    reverse_list.reverse()
    if user_list[i:] == reverse_list:
        print('Нужно приписать чисел: ', i)
        reverse_list = user_list[:i]
        reverse_list.reverse()
        print(reverse_list)
        break
