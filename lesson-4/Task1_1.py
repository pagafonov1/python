# Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

# Определить, какое число в массиве встречается чаще всего

import random
import cProfile

# Функция поиска наиболее часто встречающегося значения в массиве.
# На каждой итерации запоминаем текущее значение и устанавливаем счетчик попаданий в 1.
# После чего запускаем еще одну итерацию по массиву, начиная со следущего элемента.
# Во внутренней итерации ищем значения, равные текущему элементу внешней. Встретив таковые, инкрементируем счетчик.
# После окончания внутренней итерации сравниваем значение счетчика с максимальным.

# "Task1_1.get_most_frequent(Task1_1.array_20)"
# 100 loops, best of 5: 21.2 usec per loop
# "Task1_1.get_most_frequent(Task1_1.array_200)"
# 100 loops, best of 5: 1.87 msec per loop
# "Task1_1.get_most_frequent(Task1_1.array_2000)"
# 100 loops, best of 5: 215 msec per loop

# cProfile.run('get_most_frequent(array_20)') 1    0.000    0.000    0.000    0.000 Task1_1.py:20(get_most_frequent)
# cProfile.run('get_most_frequent(array_200)') 1    0.004    0.004    0.004    0.004 Task1_1.py:23(get_most_frequent)
# cProfile.run('get_most_frequent(array_2000)') 1    0.244    0.244    0.244    0.244 Task1_1.py:23(get_most_frequent)

def get_most_frequent(array):
    len_ = len(array)

    result = 0
    occurs = 0

    i = 0

    while i < len_:
        current_result = array[i]
        current_occurs = 1

        j = i + 1

        while j < len_:
            if array[j] == current_result:
                current_occurs += 1
            j += 1

        if current_occurs > occurs:
            result = current_result
            occurs = current_occurs
        i += 1

    return result


# Перепишем реализацию поиска наиболее часто встречающегося элемента в массиве с использованием словаря:
# Проходим по массиву только один раз, текущий элемент считаем ключом словаря, количество попаданий - значением.
# Если в словаре уже имеется ключ, равный текущему элементу массива, инкрементируем его значение.
# Иначе добавляем в словарь значение 1 по ключу, равному текущему элементу.
# После заврешения обхода массива ищем максимальное значение в словаре.
# Ключ, по которому оно хранится - искомый результат.

# "Task1_1.get_most_frequent_dict(Task1_1.array_20)"
# 100 loops, best of 5: 5.74 usec per loop
# "Task1_1.get_most_frequent_dict(Task1_1.array_200)"
# 100 loops, best of 5: 40.4 usec per loop
# "Task1_1.get_most_frequent_dict(Task1_1.array_2000)"
# 100 loops, best of 5: 485 usec per loop
# "Task1_1.get_most_frequent_dict(Task1_1.array_20000)"
# 100 loops, best of 5: 4.6 msec per loop

# cProfile.run('get_most_frequent_dict(array_20)') 1    0.000    0.000    0.000    0.000 Task1_1.py:68(get_most_frequent_dict)
# cProfile.run('get_most_frequent_dict(array_200)') 1    0.000    0.000    0.000    0.000 Task1_1.py:69(get_most_frequent_dict)
# cProfile.run('get_most_frequent_dict(array_2000)') 1    0.000    0.000    0.000    0.000 Task1_1.py:70(get_most_frequent_dict)
# cProfile.run('get_most_frequent_dict(array_20000)') 1    0.004    0.004    0.004    0.004 Task1_1.py:71(get_most_frequent_dict)

def get_most_frequent_dict(array):
    dict_ = {}

    i = 0
    len_ = len(array)

    while i < len_:
        curr = array[i]

        if curr in dict_:
            dict_[curr] += 1
        else:
            dict_[curr] = 1

        i += 1

    result = greatest_v = -1

    for k, v in dict_.items():
        if v > greatest_v:
            result = k
            greatest_v = v

    return result


# Функция, тестирующая поведение обеих функциф поиска наиболее часто встречающегося значения в массиве:
# с использованием словаря и без него


def test_most_freq():
    array = [3, 25, 55, 25, 7, 54, 9, 25, 76, 25, 76, 25, 589, 64, 25, 59, 8, 9, 33, 25]

    assert get_most_frequent(array) == 25
    print('get_most_frequent is OK')

    assert get_most_frequent_dict(array) == 25
    print('get_most_frequent_dict is OK')


# Результат:

# Наблюдаем, что скорость роста времени выполнения алгоритма без использования словаря существенно выше
# за счёт порождения внутренней итерации на каждой внешней итерации по массиву.
# Что видно и в cProfile, который, в случае работы со словарём
# начинает уточнять результаты замеров лишь на 20 000 элементов.
# 21.2 usec -> 1.87 msec -> 215 msec против 5.74 usec -> 40.4 usec -> 485 usec -> 4.6 msec
# Алгоритм со словарём всегда выполняет только одну итерацию по массиву, в результате чего время выполнения растёт
# пропорционально размеру массива (примерно в 10 раз, т.к. на каждом шаге мы увеличивали массив в 10 раз).
# Но стоит иметь в виду, что прирост скорости удалось получить за счёт
# дополнительного расходя памяти для хранения словаря.


array_20 = [random.randint(0, 100) for _ in range(20)]
array_200 = [random.randint(0, 100) for _ in range(200)]
array_2000 = [random.randint(0, 100) for _ in range(2000)]
array_20000 = [random.randint(0, 100) for _ in range(20000)]

# test_most_freq()

# cProfile.run('get_most_frequent_dict(array_20000)')
