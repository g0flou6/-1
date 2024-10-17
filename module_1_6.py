my_dict = {'Maxim': 2003, 'Dmitryi': 2001, 'Kirill': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Dmitryi'])
print('Not existing value:', my_dict.get('Alexey'))
my_dict.update({'Olesya': 2000, 'Olga': 1998})
print('Deleted value:', my_dict.pop('Maxim'))
print('Modified dictionary:', my_dict)

my_set = {1, 6.9, 3, 5, 'Str', 1, 'Str', 5, 6.9}
print('Set:', my_set)
my_set.update({'Boat', (6, 8, 7)})
my_set.remove(6.9)
print('Modified set:', my_set)
