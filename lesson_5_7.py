"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
 Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
 Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

"""
import json

list_profit = []
list_name_profit = []
d = {}

with open('seven.txt', 'r') as obj_f:
    for line in obj_f.readlines():
        print(line)

with open('seven.txt', 'r') as obj_f:
    for line in obj_f.readlines():
        name, property_type, earnings, costs = line.split()
        profit = int(earnings) - int(costs)
        d[name] = profit
        if profit < 0:
            print(f'{name} получила убыток {abs(profit)}')
        if profit >= 0:
            print(f'{name} имеет прибыль {profit}')
            list_profit.append(profit)

average_profit = sum(list_profit) / len(list_profit)
print(f'Средняя прибыль: {average_profit}')

output_list = [d, {'average_profit': average_profit}]

with open('senen_json.json', 'w') as json_f:
    json.dump(output_list, json_f)

