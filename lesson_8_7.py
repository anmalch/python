'''
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''


class ComplexNumber:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x


number_1 = ComplexNumber(3 + 5j)
number_2 = ComplexNumber(8 + 7j)
print(number_1 + number_2)
print(type(number_1 - number_2))
print(number_1 - number_2)
print(type(number_1 - number_2))