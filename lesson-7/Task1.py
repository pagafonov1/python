# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random


def sort_bubble_desc(array):
    len_ = len(array)
    ind_last = len_ - 1

    i = 1
    j = ind_last

    last_chg = 0

    # Upgrade 1: введём отсортированную и неотсортированную части для меньшего числа сравнений.
    # Отсортированная часть слева, по правой идем в обратном порядке, последовательно сравнивая пары элементов -
    # пузырёк всплывает в отсортированную часть.
    while i < len_:
        while j >= i:
            if array[j] > array[j - 1]:
                last_chg = j
                array[j], array[j - 1] = array[j - 1], array[j]

            j -= 1

        # Upgrade 2: запоминаем индекс последней перестановки.
        # Если перестановок в неотсортированной части не было, значит, она уже отсортирована и из внешнего цикла
        # можно выходить.
        if last_chg == 0:
            break

        last_chg = 0
        j = ind_last
        i += 1


arr = [random.randint(-100, 100) for _ in range(20)]
print(f'Исходный массив: {arr}')

sort_bubble_desc(arr)
print(f'Отсортированный массив: {arr}')
