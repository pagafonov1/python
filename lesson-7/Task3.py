# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой – не больше ее.

# Сделал со спойлером: поиск медианы без сортировки = незаконченный quicksort

import random


def qs_median(array):
    len_ = len(array)

    # Опорным считаем средний элемент
    pivot_ind = int(len_ / 2)
    pivot = array[pivot_ind]

    i = 0
    j = len_ - 1

    # Отслеживаем, переставляли ли опорный элемент. Если не переставляли,
    # значит, слева от него меньшие, справа - большие и он есть медиана.
    swapped_pivot = False

    while i < j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i == j == pivot_ind:
            return

        swapped_pivot = i == pivot_ind or j == pivot_ind

        if swapped_pivot:
            if array[i] == array[j]:
                return

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

        # Опорный элемени уехал с середины массива - дальше сортировать не интересно
        if swapped_pivot:
            break

    # Если переставляли опорный элемент, значит, в середине уже что-то другое и надо искать заново
    if swapped_pivot:
        qs_median(array)


# values = [3, 6, 28, 26, 27, 7, 21, 1, 26, 21, 32, 19, 13, 22, 37, 8, 49]
# values = [34, 28, 48]

sizes = [i for i in range(1, 10)]
values = [random.randint(1, 50) for _ in range(sizes[random.randint(0, len(sizes) - 1)] * 2 + 1)]
print(f'Исходный массив: {values}')

sorted_ = sorted(values)

qs_median(values)
print(f'Медиана: {values[int(len(values) / 2)]}')

print(f'Отсортированный массив для проверки: {sorted_}')
