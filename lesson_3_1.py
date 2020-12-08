"""
 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
def division_func(var_1, var_2):
    if var_2 != 0:
        return '%.2f' % (var_1 / var_2)

    else:
        print('Zero division')

num_1 = float(input('Enter the first number: '))
num_2 = float(input('Enter the second non-zero number: '))

print(division_func(num_1, num_2))