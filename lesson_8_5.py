'''
Продолжить работу над заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь
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
        self.type_of_printing = type_of_printing

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


w = OfficeEquipmentWarehouse()
p_1 = Printer('black', 'laser')
p_2 = Printer('grey', 'ink-jet')
p_3 = Printer('red', 'laser')
w.add(p_1)
w.add(p_2)
w.add(p_3)
s = Scanner('white', '6400 x 9600 dpi')
w.add(s)
c_1 = Copier('grey', '40 ppm')
c_2 = Copier('white', '30 ppm')
w.add(c_1)
w.add(c_2)
print(w.items)
print(f'Number of printers is {w.num_of(Printer)}. Number of scanners is {w.num_of(Scanner)}. '
      f' Number of copiers is {w.num_of(Copier)}.')
