a = int(input('Введите  число a'))
b = int(input('Введите  число b'))
c = int(input('Введите  число c'))

if a == b or a == c or b == c:
    print('Нужно ввести разные числа')
else:
    if a < b:
        if a < c:
            print(f'Среднее: {b if b < c else c}')
        else:
            print(f'Среднее: {a}')
    else:
        if a < c:
            print(f'Среднее: {a if b < c else c}')
        else:
            print(f'Среднее: {b}')
