def get_multiple_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiple_digits(int(str_number[1:]))
    else:
        return first

result = get_multiple_digits(924)
print(result)