# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple


# Функция для вывода результатов на экран с фильтром по условию
def _print_result(msg, clause):
    print(msg)

    for x in[f for f in factories if clause(f)]:
        print(f'\t- {x.name}')


# Предприятие
Factory = namedtuple('Factory', 'name, inc')

cnt = int(input('Количество предприятий:'))

inc_total = 0
factories = [None for _ in range(0, cnt)]

i = 0
print()

while i < cnt:
    print(f'Предприятие {i + 1}:')

    name = input('Имя предприятия:')
    inc = [0 for _ in range(0, 4)]

    j = 0

    while j < 4:
        inc_ = float(input(f'Прибыль за квартал {j + 1}:'))

        inc[j] = inc_
        inc_total += inc_

        j += 1

    factories[i] = Factory(name, inc)

    i += 1
    print()

avg = round(inc_total / cnt, 2)

print(f'Средняя прибыль: {avg}')

_print_result('Прибыль больше среднего (или равна):', lambda f: sum(f.inc) >= avg)
_print_result('Прибыль меньше среднего:', lambda f: sum(f.inc) < avg)
