def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        oth_matrix = []
        for j in range(m):
            oth_matrix.append(value)
        matrix.append(oth_matrix)
    return matrix

result1 = get_matrix(3, 4, 11)
result2 = get_matrix(5, 6, 4)
result3 = get_matrix(2, 8, 1)
print(result1)
print(result2)
print(result3)