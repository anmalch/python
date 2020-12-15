"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self):
        return 'Машина повернула на право'

    def show_speed(self):
        return f'Скорость машины: {self.speed}'


class TownCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police=False)

    def show_speed(self):
        if self.speed >= 60:
            return "Вы превысили скорость"
        else:
            return f'Скорость машины: {self.speed}'


class SportCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police=False)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police=False)

    def show_speed(self):
        if self.speed >= 40:
            return "Вы превысили скорость"
        else:
            return f'Скорость машины: {self.speed}'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


twcar = TownCar('VW', 'grey', 70, False)
spcar = SportCar('Audi', 'red', 120, False)
wcar = WorkCar('Kamaz', 'orange', 50, False)
polcar = PoliceCar('BMW', 'white', 50, True)

print(f'Town car: {twcar.name} {twcar.color} {twcar.speed} {twcar.is_police}')
print(f'Sport car: {spcar.name} {spcar.color} {spcar.speed} {spcar.is_police}')
print(f'Work car: {wcar.name} {wcar.color} {wcar.speed} {wcar.is_police}')
print(f'Police car: {polcar.name} {polcar.color} {polcar.speed} {polcar.is_police}')
print(twcar.go())
print(spcar.stop())
print(wcar.turn())
print(wcar.show_speed())
print(twcar.show_speed())
print(spcar.show_speed())
