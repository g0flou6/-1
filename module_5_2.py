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

    def __len__(self):
        return self.num_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_floor}.'



h1 = House('Хрущёвка', 5)
h2 = House('Деревянный барак', 1)

print(h1)
print(h2)

print(len(h1))
print(len(h2))