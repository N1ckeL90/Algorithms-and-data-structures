# 2.Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака
a = 5 | 6
b = 5 & 6
c = 5 ^ 6
d = 5 << 2
e = 5 >> 2
print(f'ИЛИ: {a} ({bin(a)})')
print(f'И: {b} ({bin(b)})')
print(f'Исключающее ИЛИ: {c} ({bin(c)})')
print(f'Побитовый сдвиг влево числа 5 на 2 знака: {d} ({bin(d)})')
print(f'Побитовый сдвиг вправо числа 5 на 2 знака: {e} ({bin(e)})')
