"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
import self as self
from abc import abstractmethod


class Clothes:
    @property
    @abstractmethod
    def clothes_name(self):
        pass

    @property
    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
    @property
    def clothes_name(self):
        return 'coat'

    @property
    def cloth_consumption(self):
        c = self.size / 6.5 + 0.5
        return c


class Suit(Clothes):

    def __init__(self, high):
        self.high = high
    @property
    def clothes_name(self):
        return 'suit'

    @property
    def cloth_consumption(self):
        s = 2 * self.high + 0.3
        return s

coat = Coat(30)
print(coat.clothes_name)
c = coat.cloth_consumption
print(c)
suit = Suit(20)
print(suit.clothes_name)
s = suit.cloth_consumption
print(s)
print (c+s)

