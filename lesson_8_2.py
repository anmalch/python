'''

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

param_1 = int(input('Enter number 1: '))
param_2 = int(input('Enter number 2: '))
try:

    if param_2 == 0:
        raise MyError('Zero division error')

except MyError as err:
    print(err)
else:
    print(f"{param_1 / param_2}")

