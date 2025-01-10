first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zip_list = zip(first, second)

first_result = (len(x[0]) - len(x[1]) for x in zip_list if len(x[0]) != len(x[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))


print(list(first_result))
print(list(second_result))