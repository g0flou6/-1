class StepValueError(ValueError):
    def __init__(self, message):
        self.message = message

class Iterator:
    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = self.start
        if self.step == 0:
            raise StepValueError('Шаг не может быть равен 0!')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        pointer = self.pointer
        if self.step > 0:
            if pointer > self.stop:
                raise StopIteration()
        elif self.step < 0:
            if pointer < self.stop:
                raise StopIteration()
        self.pointer += self.step
        return pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print(f'{exc.message}')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end= ' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()