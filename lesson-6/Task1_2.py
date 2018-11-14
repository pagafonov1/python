# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.

import random
import sys


def calc_size(x, acc):
    acc += sys.getsizeof(x)

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                acc += calc_size(key, 0) + calc_size(value, 0)
        elif not isinstance(x, str):
            for item in x:
                acc += calc_size(item, 0)

    return acc


# Задача 2, урок 3
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5
# Т.к. именно в этих позициях первого массива стоят четные числа.
# Windows 10 64-bit, Python 3.7.1

SIZE = 10

array = [random.randint(0, 100) for _ in range(SIZE)]
result_array = [0 for _ in range(SIZE)]

i = 0
next_insert_position = 0

# Считаем, сколько заняли переменные, проинициализированные в начале работы
_consumed = sys.getsizeof(SIZE) + calc_size(array, 0) + calc_size(result_array, 0)\
                                + sys.getsizeof(i) + sys.getsizeof(next_insert_position)

while i < SIZE:
    a = array[i] % 2

    # + результат проверки на четность
    _consumed += sys.getsizeof(a)

    if a == 0:
        result_array[next_insert_position] = i
        next_insert_position += 1

    i += 1

i = SIZE - 1

while i >= 0:
    cur = result_array[i]

    # + переменная, в которую записывам текущее значение
    _consumed += sys.getsizeof(cur)

    if cur > 0:
        break

    # Если дошли до 0-го элемента, делаем повторную проверку по исходному массиву
    # Так как не можем быть уверены, хранится ли там 0 как индекс четного элемента
    # (напр., при исходном массиве, [2, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    # либо в массиве вообще не оказалось четных элементов, напр. [5, 3, 3, 3, 3, 3, 3, 3, 3, 3]

    b = cur % 2

    # + снова результат проверки на четность
    _consumed += sys.getsizeof(b)

    if i > 0 or b > 0:
        del result_array[i]

    i -= 1

print(f'Исходный массив: {array}')
print(f'Индексы четных элементов: {result_array}')

print(f'Поиск индексов четных элементов: израсходовано {_consumed} байт.')
