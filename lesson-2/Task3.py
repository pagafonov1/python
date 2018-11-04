def rev(n, acc):
    q = int(n / 10)
    r = int(n % 10)

    if q == 0 and r == 0:
        return acc

    return rev(q, acc * 10 + r)


print(rev(abs(int(input('Введите число'))), 0))
