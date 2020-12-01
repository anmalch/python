number_month = int(input('Enter integer number: '))
month_list = [None, 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'fall', 'fall',
              'fall', 'winter']

if number_month > 12:
    print('Enter integer number =< 12')

else:
    print(month_list[number_month])


