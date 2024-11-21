class House:
    def __init__(self, name, num_floor):
        self.name = name
        self.num_floor = num_floor
    def go_to(self, new_floor):
        if new_floor > self.num_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)



h1 = House('Хрущёвка', 5)
h2 = House('Деревянный барак', 1)

print(f'Тип дома: {h1.name}; {h1.num_floor} этажей.')
print(f'Тип дома: {h2.name}; {h2.num_floor} этаж.')

h1.go_to(5)
h2.go_to(-2)
