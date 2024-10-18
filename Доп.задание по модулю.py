students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = list(students)
students = sorted((students))
grades_list = dict(zip(students, grades))
x = input('Введите имя ученика: ')
def average(x):
    return (sum(grades_list.get(x))) / (len(grades_list.get(x)))
print('Средний балл ученика:', average(x))
