'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

'''

dic = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
}

with open('fourth.txt', 'r') as data_f, open('fourth_output.txt', 'w') as output_f:
    for content in data_f.readlines():

        for key, val in dic.items():
            content = content.replace(key, val)

        output_f.writelines(content)
