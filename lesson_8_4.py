'''
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

'''
class OfficeEquipmentWarehouse:  # Склад
    pass


class OfficeEquipment:  # Оргтехника
    def __init__(self, color):
        self.color = color


class Printer(OfficeEquipment):
    def __init__(self, color, type_of_printing):
        super().__init__(color)
        self.type_of_printing = type_of_printing


class Scanner(OfficeEquipment):
    def __init__(self, color, resolution):
        super().__init__(color)
        self.resolution =resolution


class Copier(OfficeEquipment):
    def __init__(self, color, speed):
        super().__init__(color)
        self.speed = speed




p = Printer('black', 'laser')
print(f'Color of a printer: {p.color}, type of printing: {p.type_of_printing}')

s = Scanner('white', '6400 x 9600 dpi')
print(f'Color of a scanner: {s.color}, resolution of a scanner : {s.resolution}')

c = Copier('grey', '40 ppm')
print(f'Color of a copier: {c.color}, speed of a copier {c.speed}')