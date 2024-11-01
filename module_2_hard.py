def password(n):
    pword = ''
    for i in range(1, n):
        for j in range(2, n):
            if j <= i:
                continue
            if n % (i + j) == 0:
                pword += str(i) + str(j)
    return pword

first_number = int(input('Введите число от 3 до 20: '))
if first_number < 3 or first_number > 20:
    print('Неверное число')
    exit()

result = password(first_number)
print('Ваш пароль:', result)