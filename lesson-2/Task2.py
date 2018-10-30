n = int(input('Введите число'))

even = odd = 0

d = 10

q = r = v = 0

while True:
    q = int(n / d)
    r = int(int(n / int((d / 10))) % 10)

    if q == 0 and r == 0:
        break

    if r % 2 == 0:
        even += 1
    else:
        odd += 1

    d *= 10

print(f'Кол-во чётных: {even}, кол-во нечётных: {odd}')
