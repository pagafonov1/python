# Определить, какое число в массиве встречается чаще всего

import random

SIZE = 15

array = [random.randint(0, 100) for _ in range(SIZE)]

print(f'Массив: {array}')

result = 0
occurs = 0

current_result = 0
current_occurs = 0

i = j = 0

while i < SIZE:
    current_result = array[i]
    current_occurs = 1

    j = i + 1

    while j < SIZE:
        if array[j] == current_result:
            current_occurs += 1

        j += 1

    if current_occurs > occurs:
        result = current_result
        occurs = current_occurs

    i += 1

print(f'Наиболее часто в массиве встречается число {result} ({occurs} раз).')
