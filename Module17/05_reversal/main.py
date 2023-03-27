# string = str(input('Введите строку: '))
# string = "hqwehrty"
# string = "hh"
string = "hhqwerh"

first_h = string.index('h')
last_h = -string[::-1].index('h') - 1

print('Развёрнутая последовательнось между первым и последним h:', string[last_h - 1:first_h:-1])
