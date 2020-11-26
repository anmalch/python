#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.

my_list = [11, 8, 8, 6, 6, 5, 3, 3, 3]
user_num = int(input('Enter number: '))

i=0
while i < len(my_list) and user_num < my_list[i]:
    i = i + 1

my_list.insert(i, user_num)
print(my_list)
