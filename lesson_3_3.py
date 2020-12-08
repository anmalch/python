'''
Реализовать функцию my_func(),
которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
'''


def my_func(var_1, var_2, var_3):
    iter_obj = [var_1, var_2, var_3]

    min_i = 0
    min_num = iter_obj[min_i]

    for i in range(len(iter_obj)):
        if min_num > iter_obj[i]:
            min_num = iter_obj[i]
            min_i = i

    iter_obj.pop(min_i)
    return sum(iter_obj)
    # return sum(iter_obj) - min(iter_obj) - решение в одну строчку


print(my_func(2, 2, 2))
