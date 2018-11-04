n = max_n = res = max_res = 0


def cnt_sum(num, acc):
    q = int(num / 10)
    r = int(num % 10)

    if q == 0 and r == 0:
        return acc

    acc += r

    return cnt_sum(q, acc)


while True:
    n = int(input('Введите число (0 или отрицательное число для выхода): '))

    if n <= 0:
        break

    res = cnt_sum(n, 0)

    if res > max_res:
        max_n = n
        max_res = res

    print(f'Максимальное число по сумме цифр из введённых: {max_n} (сумма цифр: {max_res})')
