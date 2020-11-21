#Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

number = int(input('Введите время в секундах: '))
hour = 0
minute = 0
second = 0

if number < 60:
    second = number

if 3600 > number >= 60:
    minute = number // 60
    second = number % 60

if number >= 3600:
    hour = number // 3600
    if 3600 > (number % 3600) >= 60:
        minute = (number % 3600) // 60
        second = (number % 3600) % 60

print(f'{hour:02} : {minute:02} : {second:02}')
