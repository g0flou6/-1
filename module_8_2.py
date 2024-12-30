def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result = result + i
        except TypeError as exc:
            print(f'Некорректный тип данных для подсчёта суммы: {i}.')
            incorrect_data = incorrect_data + 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        filtered_nums = 0
        for i in numbers:
            if type(i) is int or type(i) is float:
                filtered_nums += 1
            else:
                pass
        avg = result[0] / filtered_nums
        return avg
    except ZeroDivisionError:
        avg = 0
        return avg
    except TypeError:
        print('В numbers записан некорректный тип данных!')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')