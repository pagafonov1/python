# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу

MATRIX_X = 5
MATRIX_Y = 4

matrix = [[0, 0, 0, 0, 0] for _ in range(MATRIX_Y)]

i = 0
j = 0

while i < MATRIX_Y:
    print(f'Вводим строку {i + 1}')

    while j < MATRIX_X - 1:
        val = int(input(f'Введите число {j + 1}:'))

        matrix[i][j] = val
        matrix[i][MATRIX_X - 1] += val

        j += 1

    j = 0
    i += 1

    print('')


i = 0

while i < MATRIX_Y:
    print(matrix[i])
    i += 1
