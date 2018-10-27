ch1 = input('Введите символ 1')
ch2 = input('Введите символ 2')

pos1 = ord(ch1)
pos2 = ord(ch2)

if pos1 < 97 or pos1 > 122 or pos2 < 97 or pos2 > 122:
    print('Оба символа должны быть строчными лат. буквами')
else:
    dis = pos2 - pos1

    if dis < 0:
        dis = pos1 - pos2

    pos1 -= 96
    pos2 -= 96

    print(f'Порядковый номер {ch1}: {pos1}, порядковый номер {ch2}: {pos2}, расстояние: {dis}')
