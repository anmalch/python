user_string = input('Enter string: ')

user_list = user_string.split(' ')

for i in range(len(user_list)):
    print(f'{i + 1}. {user_list[i][:10]}')
