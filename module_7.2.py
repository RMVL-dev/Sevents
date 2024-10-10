
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding="utf-8")
    dict_to_return = {}
    index = 1
    for string in strings:
        dict_to_return[(index, file.tell())] = string
        file.write(string + "\n")
        print(f"byte = {file.tell()}")
        index += 1
    file.close()
    return dict_to_return


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
