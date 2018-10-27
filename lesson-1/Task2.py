# andRes = 4. Побитовая операция and вычисляет логическое И для пары бит.
# Представляем 5 и 6 в двоичном виде (101 и 110 соответственно).
# Результатом логического И для кажой пары бит будет: 0 И 1 = 0, 1 И 0 = 0, 1 И 1 = 1
# Получаем 100, переводим результат в десятичную систему счисления - получаем 4.
# Таким образом, 5 & 6 = 4
andRes = 5 & 6

# orRes = 7. Побитовая операция or вычисляет логическое ИЛИ для пары бит.
# Представляем 5 и 6 в двоичном виде (101 и 110 соответственно).
# Результатом логического ИЛИ для кажой пары бит будет: 0 ИЛИ 1 = 1, 1 ИЛИ 0 = 1, 1 ИЛИ 1 = 1
# Получаем 111, переводим результат в десятичную систему счисления - получаем 7.
# Таким образом, 5 | 6 = 7
orRes = 5 | 6

# xorRes = 3. Побитовая операция xor вычисляет исключающее ИЛИ для пары бит (один и только один бит из пары равен 1).
# Представляем 5 и 6 в двоичном виде (101 и 110 соответственно).
# Результатом исключающего ИЛИ для кажой пары бит будет: 0 ИИЛИ 1 = 1, 1 ИИЛИ 0 = 1, 1 ИИЛИ 1 = 0
# Получаем 011, переводим результат в десятичную систему счисления - получаем 3.
# Таким образом, 5 & 6 = 3
xorRes = 5 ^ 6

# Оператор << сдвигает биты своего операнда влево на указанное количество позиций.
# Освободившиеся места заполняются нулями.
# Таким образом, для 101 (00101) результатом будет 10100 (20 в десятичной системе счисления)
# Аналогичный результат можно получить, вычислив 5 * (2 * 2) = 20, т. к. основание двоичной системы счисления - 2.
shiftLeft5 = 5 << 2

# Оператор << сдвигает биты своего операнда влево на указанное количество позиций.
# Пустые места в нашем случае заполнятся нулями (т.к. операнд - положительное число, соотв., старший бит также равен 0)
# Таким образом, для 101 результатом будет 001
# Аналогично, поскольку работаем с двоичной системой, можем выполнить деление на (2 в степени 2) = 5 / 4 = 1
shiftRight5 = 5 >> 2

print(f'И: {andRes}, ИЛИ: {orRes}, ИИЛИ: {xorRes}, Сдвиг влево: {shiftLeft5}, Сдвиг вправо: {shiftRight5}')