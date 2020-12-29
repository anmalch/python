'''
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

salary_dict = {'Слон': 18900, 'Кот': 23000, 'Пес': 19000, 'Мышь': 43000, 'Баран': 34000, 'Заяц': 12000, 'Лис': 17000,
               'Бык': 54000, 'Белка': 43000, 'Петух': 39000, 'Пингвин': 51000, 'Рыбка': 78000}

with open('third_salary.txt', 'w') as f:
    for name, salary in salary_dict.items():
        f.write(f'{name} {salary}\n')

# кто из сотруднико иммет оклад меньше 20000
name_result = []
for name, salary in salary_dict.items():
    if int(salary) < 20000:
        name_result.append(name)
print(f'Сотрудники имеют оклад меньше 20000 {name_result}')

# средняя величина дохода сотрудников
salary_list = list(salary_dict.values())
average_salary = (sum(salary_list)) / len(salary_list)
print(f'Средняя доход сотрудников: {round(average_salary, 2)}')
