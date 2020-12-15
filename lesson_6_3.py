'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
 (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

'''


class Worker:
    name = None
    surname = None
    position = None
    _income = {'wage': 0, 'bonus': 0}


class Position(Worker):

    def __init__(self, dict_income):
        super().__init__()
        self._income = dict_income

    def get_full_name(self):
        print(f'{self.name} {self.surname}, {self.position}')

    def get_total_income(self):
        print(int(self._income['wage']) + int(self._income['bonus']))


p = Position({'wage': 400, 'bonus': 90})
p.name, p.surname, p.position = 'Jon', 'Snow', 'manager'
p.get_full_name()
p.get_total_income()
