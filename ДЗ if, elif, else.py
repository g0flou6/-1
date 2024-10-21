first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if second == first == third:
    print(3)
elif second == first != third or second != first == third or first != second == third:
    print(2)
else:
    print(0)
