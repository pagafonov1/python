FROM_CHAR = 32
TO_CHAR = 127

i = FROM_CHAR
ch = ''

while i <= TO_CHAR:
    ch = chr(i)

    print(f'{i}={ch}', end='')

    i += 1

    if (i - FROM_CHAR) % 10 > 0:
        print('DEL' if i > TO_CHAR else ', ', end='')
    else:
        print('')
