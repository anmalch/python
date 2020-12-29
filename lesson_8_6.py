'''

Продолжить работу над заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''
class OfficeEquipmentWarehouse:
    items = []

    def add(self, item):
        self.items.append(item)

    def num_of(self, type_of_item):
        return sum(1 for item in self.items if type(item) == type_of_item)


class OfficeEquipment:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return '<' + self.__str__() + '>'

    def __str__(self):
        return type(self).__name__ + ' ' + self.color


class Printer(OfficeEquipment):
    def __init__(self, color, type_of_printing):
        super().__init__(color)
        if type_of_printing == 'laser' or type_of_printing == 'ink-jet':
            self.type_of_printing = type_of_printing
        else:
            raise InvalidDataError(type_of_printing)



    def __str__(self):
        return super().__str__() + ' ' + self.type_of_printing


class Scanner(OfficeEquipment):
    def __init__(self, color, resolution):
        super().__init__(color)
        self.resolution = resolution

    def __str__(self):
        return super().__str__() + ' ' + self.resolution


class Copier(OfficeEquipment):
    def __init__(self, color, speed):
        super().__init__(color)
        self.speed = speed

    def __str__(self):
        return super().__str__() + ' ' + self.speed

class InvalidDataError(Exception):

    def __init__(self, error_str):
        self.error_str = error_str


try:
    #p = Printer('black', 'las')
    p_1 = Printer('black', 'laser')
    p_2 = Printer('grey', 'ink-jet')
    p_3 = Printer('red', 'laser')
except InvalidDataError as err:
    print(f"You entered incorrect data")

else:

    w= OfficeEquipmentWarehouse()

    w.add(p_1)
    w.add(p_2)
    w.add(p_3)
    print(f'Number of printers is {w.num_of(Printer)}.')


