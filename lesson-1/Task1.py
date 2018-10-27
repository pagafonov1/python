num = abs(int(input('Введите 3-х значное число')))

h = int(num / 100)
t = int(num / 10 % 10)
u = int(num % (100 * h + 10 * t))

s = h + t + u
p = h * t * u

print(f'Сумма: {s}, Произведение: {p}')
