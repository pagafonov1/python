year = int(input('Введите год'))

isLeapYear = year % 400 == 0 or (year % 100 > 0 and year % 4 == 0)

print('Год високосный' if isLeapYear else 'Год невисокосный')
