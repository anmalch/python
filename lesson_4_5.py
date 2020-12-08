'''Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

my_list = (el for el in range(100, 1001) if el % 2 == 0)

from functools import reduce

def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, list(my_list)))