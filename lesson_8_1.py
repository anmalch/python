"""
Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def parse_to_number(cls, date):
        day = int(date.date_str[0:2])
        month = int(date.date_str[3:5])
        year = int(date.date_str[6:])
        return day, month, year

    @staticmethod
    def validate_date(date):
        day, month, year = Date.parse_to_number(date)
        if 0 <= day <= 31 and 1 <= month <= 12 and year > 0 and \
                date.date_str[2] == '-' and date.date_str[5] == '-':
            print('Date entered correctly')
        else:
            print('Date entered incorrectly!')


d = Date('01-12-1986')
day, month, year = Date.parse_to_number(d)
print(f'day: {day}, month: {month}, year: {year}')
Date.validate_date(d)
