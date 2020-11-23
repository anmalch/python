# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numbers=input('Введите целое положительное число: ')
i = 0
max_number = 0

while i < len(numbers):
    number = int(numbers[i])
    if number > max_number:
        max_number = number
    i = i + 1

print(max_number)




