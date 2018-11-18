# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.

import sys

# Урок 2, задание 5
# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
# Windows 10 64-bit, Python 3.7.1

FROM_CHAR = 32
TO_CHAR = 127

i = FROM_CHAR
ch = ''

_consumed = sys.getsizeof(FROM_CHAR) + sys.getsizeof(TO_CHAR) + sys.getsizeof(i) + sys.getsizeof(ch)

while i <= TO_CHAR:
    ch = chr(i)

    msg = f'{i}={ch}'

    _consumed += sys.getsizeof(ch) + sys.getsizeof(msg)

    print(msg, end='')

    i += 1

    # Считаем рузальтаты всех проверок
    a = i - FROM_CHAR
    b = a % 10
    c = b > 0

    _consumed += sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c)

    # if (i - FROM_CHAR) % 10 > 0:
    if c:
        d = i > TO_CHAR
        if d:
            del_ = 'DEL'
            _consumed + sys.getsizeof(del_)
            print(del_, end='')
        else:
            print(', ', end='')
    else:
        print('')

    # Строковый литерал считаем один раз
    _consumed += sys.getsizeof(', ')

print()
print(f'Печать ASCII таблицы группами по 10 символов: израсходовано {_consumed} байт.')
