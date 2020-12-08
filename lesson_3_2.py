'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

'''
def user_date(name, surname, birth_year, city, email, phone):
    if email.endswith('@mail.ru'):
        print(f'name - {name}; surname - {surname}; birth_year - {birth_year}; city - {city}; email -{email}; phone - {phone}')
    else:
        print('Некорректно введен email')
#user_date(name="Jon", surname="Snow", birth_year=1986, city="Winterfell", email="j.snow@mail.ru", phone=12345)

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
birth_year = int(input('Введите дату вашего рождения: '))
city = input('Введите город проживания: ')
email = input('Введите Email: ')
phone = int(input('Введите номер телефона: '))
