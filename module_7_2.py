info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings: list):
    file = open(file_name, 'a', encoding= 'utf-8')
    for string in strings:
        file.write(f'{string}\n')
    file.close()

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



print(custom_write('test.txt', info))