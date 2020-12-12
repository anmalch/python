"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.

"""
import re

with open('second_file.txt', 'w') as f:
    f.writelines(['Мороз и солнце!\n', 'День чудесный!\n', 'Ещё ты дремлешь, друг прелестный?\n'])

with open('second_file.txt', 'r') as f:
    lines = f.readlines()
    for i_str, val in enumerate(lines, start=1):
        split = re.split('[ !,?\n]+', val.strip('[ !,?\n]+'))
        num_words = len(split)
        print(f'В {i_str} строке {num_words} слов/слова')