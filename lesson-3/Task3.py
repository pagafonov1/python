# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

SIZE = 10

array = [random.randint(0, 100) for _ in range(SIZE)]

print(f'Исходный массив: {array}')

ind_min = ind_max = 0
val_min = val_max = array[0]

i = 1

while i < SIZE:
    curr = array[i]

    if curr < val_min:
        ind_min = i
        val_min = curr
    elif curr > val_max:
        ind_max = i
        val_max = curr

    i += 1

array[ind_min] = val_max
array[ind_max] = val_min

print(f'После перестановки: {array}')
