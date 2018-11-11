# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

from collections import deque

dec_values = dict()

for z in range(0, 10):
    dec_values[str(z)] = z

dec_values['A'] = 10
dec_values['B'] = 11
dec_values['C'] = 12
dec_values['D'] = 13
dec_values['E'] = 14
dec_values['F'] = 15

keys = list(dec_values.keys())


# Меньшее из чисел добиваем нулями.
# Возвращаем модифицированные коллекции и длину.
def _prepend_zeros(hex1, hex2):
    len1 = len(hex1)
    len2 = len(hex2)

    if len1 != len2:
        delta = abs(len1 - len2)
        zeros = [str(0)] * delta

        if len1 < len2:
            hex1 = deque(hex1)
            hex1.extendleft(zeros)
            len1 += delta
        else:
            hex2 = deque(hex2)
            hex2.extendleft(zeros)

    return hex1, hex2, len1


# Внутренний метод, обощающий расчёты в столбик.
# Параметры:
#   - x и y - символьные значения, числовые соответствия которым будем искать в словаре с ключами от 0 до F
#   - in_the_head - текущее значение в уме
#   - i - текущий шаг
#   - op - функция от x и y, представляющая желаемое действие над числами (сложение или умножение)
#   - acc - аккумулятор, хранящий результаты между вызовами
# Значение, которое запомнили в уме и аккумулятор возвращаем вызывающему коду.
def _do_calc(x, y, in_the_head, i, op, acc):
    k = op(dec_values[x], dec_values[y]) + in_the_head
    in_the_head = 0

    if k <= 15:
        acc.appendleft(keys[k])
    else:
        acc.appendleft(keys[k % 16])
        in_the_head = dec_values[keys[int(k / 16)]]

    # Прошли весь массив, но ещё осталось значение в уме
    if i == 0 and in_the_head > 0:
        acc.appendleft(str(in_the_head))

    return acc, in_the_head


# Сложение столбиком
def sum_(hex1, hex2):
    hex1, hex2, len_ = _prepend_zeros(hex1, hex2)

    res = deque()

    i = len_ - 1
    in_the_head = 0

    while i >= 0:
        res, in_the_head = _do_calc(hex1[i], hex2[i], in_the_head, i, lambda x, y: x + y, res)

        i -= 1

    return res


# Умножение столбиком
def mult(hex1, hex2):
    hex1, hex2, len_ = _prepend_zeros(hex1, hex2)

    summands = []

    j = q = len_ - 1

    while j >= 0:
        i = q

        # Считаем промежуточные результаты со сдвигом на разряд влево
        res = deque([str(0)] * (q - j))
        in_the_head = 0

        while i >= 0:
            res, in_the_head = _do_calc(hex1[i], hex2[j], in_the_head, i, lambda x, y: x * y, res)

            i -= 1

        summands.append(res)

        j -= 1

    j = 0
    q = len(summands) - 1

    # Складываем промежуточные результаты
    while j < q:
        next_ = j + 1
        summands[next_] = sum_(summands[j], summands[next_])

        j += 1

    result = summands[q]

    # Убираем лишние нули
    while result[0] == '0':
        result.popleft()

    return result


n1 = input('Введите число 1:').upper()
n2 = input('Введите число 2:').upper()

print(f'Сумма: {sum_(n1, n2)}, произведение: {mult(n1, n2)}')
