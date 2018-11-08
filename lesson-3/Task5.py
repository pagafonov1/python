# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 15

array = [random.randint(-50, 50) for _ in range(SIZE)]

result = 0
result_index = 0

i = 0

while i < SIZE:
    current = array[i]

    if current >= 0:
        i += 1
        continue

    if result == 0 or current > result:
        result = current
        result_index = i

    i += 1

print(f'Массив: {array}')
print('В массиве нет отрицательных чисел' if result == 0
      else f'Максимальный отрицательный элемент: {result} располагается по индексу {result_index}')
