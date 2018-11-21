# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

def find_substrs(s):
    len_ = len(s)

    result = list()
    cnt = 0

    for i in range(1, len_):
        j = 0
        k = len_ - i

        while j <= k:
            subs = s[j:j+i]
            h_subs = hash(subs)

            if h_subs not in result:
                result.append(h_subs)
                cnt += 1

            j += 1

    return cnt


c = find_substrs('papa')
print(f'Кол-во подстрок: {c}')
