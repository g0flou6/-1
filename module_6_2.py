class Vehicle:
    __COLOR_VARIANTS = ['чёрный', 'синий', 'фиолетовый','белый', 'красный']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)
        self.colors = Vehicle.__COLOR_VARIANTS

    def get_model(self):
        print(f'Модель: {self.__model}.')

    def get_horsepower(self):
        print(f'Мощность: {self.__engine_power}.')

    def get_color(self):
        print(f'Цвет транспорта: {self.__color}.')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}.')

    def set_color(self, new_color):
        lower_color = new_color.lower()
        if lower_color in self.colors:
            self.__color = lower_color
        else:
            print(f'Нельзя сменить цвет на {lower_color}.')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Максим', 'Toyota Supra MK4', 324, 'синий')

vehicle1.print_info()
vehicle1.set_color('КраСНЫй')
vehicle1.set_color('ЗЕЛЁНЫЙ')
vehicle1.owner = 'Олеся'
vehicle1.print_info()

