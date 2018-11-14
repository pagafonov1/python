# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.

import sys

# Задача 2 из урока 1 - произвести побитовые операции над числами
# Выясняем, что для хранения цельночисленного ненулевого значения python использует 28 байт памяти.
# Таким образом можем посчиать вручную количество израсходованной памяти:
# Задействуемм числа 5, 6 и 2, поскольку всеони попадают в диапазон заранее размещённых в памяти чисел,
# получаем 84 байта + 28 * 4 для результатов.
# Windows 10 64-bit, Python 3.7.1

# ps Пока писал, появились сомнения. имеет ли смысл вообще такая проверка в данном случае?
# Учитывая, что числв известного диапазона заранее размещены в памяти, сколько бы мы к ним не обрашались, дополнительной
# памяти на размещение числа израсходовано не будет. И еще, когда мы объявляем переменные a = 5, b = 4,
# создаются новые ссылки на заранее размещенные значения, но ведь и сама ссылка тоже должна занимать какое-то место?

andRes = 5 & 6
orRes = 5 | 6
xorRes = 5 ^ 6
shiftLeft5 = 5 << 2

print(f'Побитовые операции над числами 5 и 6: {sys.getsizeof(5) * 3 + sys.getsizeof(5) * 4} байт.')



