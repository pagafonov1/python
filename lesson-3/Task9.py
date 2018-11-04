# Найти максимальный элемент среди минимальных элементов столбцов матрицы

import random

MATRIX_X = 5
MATRIX_Y = 4

matrix = [[random.randint(0, 100) for _ in range(MATRIX_X)] for _ in range(MATRIX_Y)]

min_column = 0
max_min_column = 0

i = 0
j = 1

while i < MATRIX_X:
    min_column = matrix[0][i]

    while j < MATRIX_Y:
        current = matrix[j][i]

        if current < min_column:
            min_column = current

        j += 1

    if min_column > max_min_column:
        max_min_column = min_column

    j = 1
    i += 1

i = 0
while i < MATRIX_Y:
    print(matrix[i])
    i += 1

print(f'Наибольший среди наименьших элементов столбцов матрицы: {max_min_column}')
