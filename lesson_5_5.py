'''
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

numbers = input('Введите набор чисел: ')
with open('fifth_file.txt', 'w') as f:
    f.write(numbers+'\n')
    num_list = numbers.split()
    sum_result = str(sum(map(int, num_list)))
    print(sum_result)
    f.write(f'Сумма чисел: {sum_result}')