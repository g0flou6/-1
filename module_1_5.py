immutable_var = 11, 'abc', 99, 'var'
print(immutable_var)
#immutable_var[1] = 'def' Кортеж неизменяемый тип данных, поэтому при изменении кортежа появляется ошибка
mutable_list = [22, 'def', 256, 'dog']
mutable_list.append(True)
mutable_list.remove(22)
print(mutable_list)