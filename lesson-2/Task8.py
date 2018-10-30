def count_digit(num, digit, acc):
    q = int(num / 10)
    r = int(num % 10)

    if q == 0 and r == 0:
        return acc

    if r == digit:
        acc += 1

    return count_digit(q, digit, acc)


cnt = int(input('Задайте количество вводимых чисел'))
dig = input('Задайте цифру, которую будем искать')

DIGITS_START = 48
DIGITS_END = 57

res = i = curr = 0

if len(dig) > 1:
    print('Нужно ввести цифру от 0 до 9')
else:
    code = ord(dig)

    if code < DIGITS_START or code > DIGITS_END:
        print('Нужно ввести цифру от 0 до 9')
    else:
        while i < cnt:
            curr = int(input(f'Введите число {i + 1}'))

            res += count_digit(curr, int(dig), 0)
            i += 1

        print(f'Цифра {dig} встретилась {res} раз среди {cnt} чисел.')
