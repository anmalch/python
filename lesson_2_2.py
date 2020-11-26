user_list = list(input('Введите элеметы списка: '))

for index in range(0, len(user_list) - 1, +2):
     user_list[index], user_list[index+1] = user_list[index+1], user_list[index]

print(user_list)
