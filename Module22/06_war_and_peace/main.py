import zipfile

sym_dict = {}
with zipfile.ZipFile("voyna-i-mir.zip") as archive:
    for filename in archive.filelist:
        with archive.open(filename) as file:
            for letter in file.read().decode():
                if letter not in sym_dict:
                    sym_dict[letter] = 0
                sym_dict[letter] += 1

res_file = open('res.txt', 'w', encoding="utf-8")

for letter, amount in sorted(sym_dict.items(), key=lambda x: -x[1]):
    res_file.write(str(f'{letter}, {amount} \n'))

res_file.close()