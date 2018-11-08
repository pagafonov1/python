# Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import cProfile

# STEP = 20
# "Task2.find_prime_eratosphenes(25)" 100 loops, best of 5: 71.4 usec per loop
# "Task2.find_prime_eratosphenes(75)" 100 loops, best of 5: 1.01 msec per loop
# "Task2.find_prime_eratosphenes(125)" 100 loops, best of 5: 3.3 msec per loop
# "Task2.find_prime_eratosphenes(175)" 100 loops, best of 5: 8.06 msec per loop
# cProfile.run('find_prime_eratosphenes(25)') 5/1    0.000    0.000    0.000    0.000 Task2.py:25(eratosphenes_inner)
# cProfile.run('find_prime_eratosphenes(75)') 19/1    0.001    0.000    0.001    0.001 Task2.py:26(eratosphenes_inner)
# cProfile.run('find_prime_eratosphenes(125)') 35/1    0.003    0.000    0.003    0.003 Task2.py:26(eratosphenes_inner)
# cProfile.run('find_prime_eratosphenes(175)') 52/1    0.007    0.000    0.007    0.007 Task2.py:27(eratosphenes_inner)

# STEP = 100
# "Task2.find_prime_eratosphenes(25)" 100 loops, best of 5: 35.7 usec per loop
# "Task2.find_prime_eratosphenes(75)" 100 loops, best of 5: 342 usec per loop
# "Task2.find_prime_eratosphenes(125)" 100 loops, best of 5: 897 usec per loop
# "Task2.find_prime_eratosphenes(175)" 100 loops, best of 5: 1.87 msec per loop
# cProfile.run('find_prime_eratosphenes(25)') 1    0.000    0.000    0.000    0.000 Task2.py:24(eratosphenes_inner)
# cProfile.run('find_prime_eratosphenes(75)') 4/1    0.000    0.000    0.000    0.000 Task2.py:23(eratosphenes_inner)
# cProfile.run('find_prime_eratosphenes(125)') 7/1    0.001    0.000    0.001    0.001 Task2.py:22(eratosphenes_inner)
# cProfile.run('find_prime_eratosphenes(175)') 11/1    0.002    0.000    0.002    0.002 Task2.py:20(eratosphenes_inner)

def find_prime_eratosphenes(i):
    # Шаг, с которым будем достраивать список, если i-тое простое число ещё не найдено
    STEP = 20

    def eratosphenes_inner(i, sieve, hits):
        len_ = len(sieve)

        # Сохраняем последнее значение списка, на случай, если придется расширять
        last_val = sieve[len_ - 1]

        for j in sieve:
            if sieve[j] == 0:
                continue

            k = j + j

            while k < len_:
                if sieve[k] > 0:
                    sieve[k] = 0

                    # Считаем вычеркнутые непростые числа
                    hits += 1

                k += j

        # Помним, что 0 и 1 - не простые числа!
        if len_ - hits >= i + 2:
            return [q for q in sieve if q != 0]
        else:
            # Достраиваем список начиная с last_val + 1, на STEP элементов и начинаем сначала
            sieve.extend([z for z in range(last_val + 1, last_val + 1 + STEP)])
            return eratosphenes_inner(i, sieve, hits)

    sieve = [i for i in range(0, STEP)]
    sieve[1] = 0

    return eratosphenes_inner(i, sieve, 0)[i - 1]


# Функция поиска простых чисел без решета Эратосфена

# "Task2.find_prime(25)" 100 loops, best of 5: 35.9 usec per loop
# "Task2.find_prime(75)" 100 loops, best of 5: 222 usec per loop
# "Task2.find_prime(125)" 100 loops, best of 5: 541 usec per loop
# "Task2.find_prime(175)" 100 loops, best of 5: 955 usec per loop

# Количество вызовов append равно порядковый номер простого числа, которое ищем - 1
# cProfile.run('find_prime(25)') 24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('find_prime(75)') 74    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('find_prime(125)') 124    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('find_prime(175)') 174    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

def find_prime(i):
    # Первое простое число - всегда 2
    if i == 1:
        return 2

    primes = [2]

    # Начинаем с 3 поиск следующих простых чисел
    j = 3

    while True:
        # Каждое следующее число сначала считаем кандидатом в простые
        is_candidate = True

        # Проходим по массиву уже найденных простых чисел, если наш кандидат кратен любому из них, значит,
        # он не является простым числом
        for p in primes:
            if j % p == 0:
                is_candidate = False
                break

        # Не кратно никакому из уже найденных простых чисел, значит, простое - добавляем в массив
        if is_candidate:
            primes.append(j)

            # Нашли i-тое простое число - выходим
            if len(primes) == i:
                break

        j += 1

    return primes[i - 1]


# cProfile.run('find_prime_eratosphenes(175)')

# При неизвестном заранее диапазоне, в котором будет производиться поиск простого числа, лучше показывает себя алгоритм
# без применения решета Эратосфена. Причина данного поведения в том, что с решетом приходится достраивать список, если
# искомое число не было найдено и повторять процедуру с начала списка.
# Впрочем, при увеличении шага расширения списка (пробовал с шагом 20 и 100), время выполнения алгоритма с применением
# решета также ощутимо снижается.
# Таким образом, задача - подобрать размер шата таким образом, чтобы соблюсти баланс между
# скоростью работы и малым количеством расширений с одной стороны и количеством выполненной лишней работы
# (например, если мы ищем 100-е простое число, а шаг поставили в 10 000, скорее всего,
# много расчётов будет произведено впустую) с другой.
