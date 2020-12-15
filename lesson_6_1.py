"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния красный -7 секунд, желтый — 2 секунды, зеленый — на ваше усмотрение (9с).
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    __color = 'red'

    def running(self, user_color='red'):
        if self.__color == user_color:
            print(f'traffic light already shows {self.__color}')
            return
        elif (self.__color == 'red' or self.__color == 'green') and user_color == 'yellow':
            time.sleep(7)
            self.__color = 'yellow'
            print(f'traffic light shows {self.__color}')
            return
        elif self.__color == 'yellow' and user_color == 'green':
            time.sleep(2)
            self.__color = 'green'
            print(f'traffic light shows {self.__color}')
            return
        elif self.__color == 'yellow' and user_color == 'red':
            time.sleep(2)
            self.__color = 'red'
            print(f'traffic light shows {self.__color}')
            return


a = TrafficLight()
a.running('yellow')
a.running('green')
a.running('yellow')
a.running('red')
