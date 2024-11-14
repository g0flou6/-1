data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum_structure(list_):
    sum = 0
    if isinstance(list_, int):
        sum += list_
    if isinstance(list_, str):
        sum += len(list_)
    if isinstance(list_, list):
        for i in list_:
            sum += sum_structure(i)
    if isinstance(list_, tuple):
        for i in list_:
            sum += sum_structure(i)
    if isinstance(list_, set):
        for i in list_:
            sum += sum_structure(i)
    if isinstance(list_, dict):
        for key, value in list_.items():
            sum += sum_structure(key)
            sum += sum_structure(value)
    return sum

result = sum_structure(data_structure)
print(result)