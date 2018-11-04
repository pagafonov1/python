n = int(input('Введите число шагов:'))

s = c = 1
i = 0

while i < n:
    c *= -0.5
    s += c
    i += 1

print(f'Сумма: {s}')
