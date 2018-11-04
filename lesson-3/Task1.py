# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9

# Начало и конец диапазона чисел
RANGE_START = 2
RANGE_END = 99

# Начало и конец диапазона чисел, на кратность которым будем проверять первый диапазон
DIV_START = 2
DIV_END = 9

result = [0 for _ in range(2, 10)]

i = RANGE_END
j = DIV_END

while i >= RANGE_START:
    while j >= DIV_START:
        if i % j == 0:
            result[j - 2] += 1

        j -= 1

    i -= 1
    j = DIV_END

i = 0

while i < DIV_END - 1:
    print(f'Элементов, кратных {i + 2}: {result[i]}')
    i += 1
