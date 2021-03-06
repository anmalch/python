'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т

'''


class Road:
    _length = 5000
    _width = 20

    def mass_of_asphalt(self, mass, thickness):
        return self._length * self._width * mass * 0.01 * thickness


mass = int(input('Enter the mass of asphalt(kg): '))
thickness = int(input('Enter blade thickness(cm): '))

r = Road()
print(f'Mass of asphalt is {r.mass_of_asphalt(mass, thickness)} kg')
