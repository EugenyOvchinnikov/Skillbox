def compression(line):
    compressed_line = ''
    counter = 0
    for i, char in enumerate(line):
        counter += 1
        if len(line) - 1 == i or char != line[i + 1]:
            compressed_line += char + str(counter)
            counter = 0
    return compressed_line


text = input('Введите строку: ')
encoded = compression(text)
print(encoded)
