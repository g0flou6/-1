info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings: list):
    with open(file_name, 'w', encoding= 'utf-8') as file:
        for string in strings:
            file.write(f'{string}\n')

    with open(file_name, 'r', encoding= 'utf-8') as read_file:
        strings_positions = {}
        while True:
            line_num = 0
            position = read_file.tell()
            line = read_file.readline()
            if not line:
                break
            strings_positions[line_num, position] = line
            line_num += 1
        return strings_positions



result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
