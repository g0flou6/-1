def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    return inner_function()


test_function()
# print(inner_function()) этот код выдаёт ошибку, так как данная функция находится в локальной области видимости
