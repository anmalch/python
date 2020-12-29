'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''


class InvalidStringError(Exception):

    def __init__(self, error_str):
        self.error_str = error_str


user_list = []


def validate_string(user_str):
    if user_str.isdigit():
        return int(user_str)
    else:
        raise InvalidStringError(user_str)


while True:
    user_str = input('Enter element: ')

    try:
        user_str = validate_string(user_str)
    except InvalidStringError as err:
        print(f"You entered a string '{err.error_str}'. Try again!")
    else:
        user_list.append(user_str)
        print(f'{user_list}')
    if user_str == ' ':
        print("End of the program")
        break
