def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
# print_params(a, b) Нельзя вызвать данную функцию с разным кол-вом аргументов
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

print('-----------------')

values_list = ['bam', 16, True]
values_dict = {'a': True, 'b': 5, 'c': 'city'}
print_params(*values_list)
print_params(**values_dict)

print('-----------------')

values_list_2 = ['crocodile', 133.7]
print_params(*values_list_2, 13)

