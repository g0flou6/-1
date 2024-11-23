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

    def __eq__(self, other):
        return self.num_floor == other.num_floor

    def __lt__(self, other):
        return self.num_floor < other.num_floor
    def __le__(self, other):
        return self.num_floor <= other.num_floor

    def __gt__(self, other):
        return self.num_floor > other.num_floor
    def __ge__(self, other):
        return self.num_floor >= other.num_floor

    def __ne__(self, other):
        return self.num_floor != other.num_floor

    def __add__(self, value):
        self.num_floor += value
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        self.num_floor -= value
        return self
    def __isub__(self, value):
        return self.__sub__(value)
    def __rsub__(self, value):
        return self.__sub__(value)

h1 = House('Хрущёвка', 5)
h2 = House('Деревянный барак', 1)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 - 4
print(h1)
print(h1 == h2)

h1 += 4
print(h1)

h2 = 4 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)










