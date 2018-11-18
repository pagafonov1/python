# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

# Скажу честно, сам написать не осилил. Нашел реализацию на C#, разобрался как она работает, переписал на питоне.

import random


def merge_sort(array):

    # Внутренняя функция, сливающая два локально упорядоченных массива
    def _merge(arr, left, right):
        ind_left = ind_right = ind_insert = 0

        len_left = len(left)
        len_right = len(right)

        # Сколько всего элементов надо вставить
        cnt = len_left + len_right

        next_val = 0

        # Сравниваем элементы двух массивов парами
        while cnt > 0:
            if ind_left >= len_left:
                next_val = right[ind_right]
                ind_right += 1
            elif ind_right >= len_right:
                next_val = left[ind_left]
                ind_left += 1
            elif left[ind_left] < right[ind_right]:
                next_val = left[ind_left]
                ind_left += 1
            else:
                next_val = right[ind_right]
                ind_right += 1

            arr[ind_insert] = next_val

            ind_insert += 1
            cnt -= 1

    len_ = len(array)

    # 1 элемент - упорядочен
    if len_ == 1:
        return

    # Делим массив пополам
    mid = int(len_ / 2)

    l_ = [array[i] for i in range(0, mid)]
    r_ = [array[i] for i in range(mid, len_)]

    merge_sort(l_)
    merge_sort(r_)

    _merge(array, l_, r_)


values = [round(random.uniform(0, 50), 3) for _ in range(0, 20)]
print(f'Исходный массив: {values}')

merge_sort(values)
print(f'Отсортированный массив: {values}')
