# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках практического задания первых трех уроков.
from sys import getsizeof


# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака
def log_operations():
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
    print(getsizeof(a))  # 28 байт (размер остальных переменных будет такой же)
    return


if __name__ == "__main__":
    log_operations()
# Временная сложность алгоритма - O(1). Оптимизирование не нужно
# Пространственная сложность - O(1).
# Количество памяти, которое было выделено - 224 байта
# Можно уменьшить количество используемой памяти использую только 1 переменную, выводя результат после каждого действия.
# В этом случае было бы выделено 112 байт, т.е. в 2 раза меньше
# Версия Python 3.10.0. Разрядность системы - 64 бит.

# def log_operations(): # оптимизация по памяти
#     a = 5 | 6
#     print(f'ИЛИ: {a} ({bin(a)})')
#     a = 5 & 6
#     print(f'И: {a} ({bin(a)})')
#     a = 5 ^ 6
#     print(f'Исключающее ИЛИ: {a} ({bin(a)})')
#     a = 5 << 2
#     print(f'Побитовый сдвиг влево числа 5 на 2 знака: {a} ({bin(a)})')
#     a = 5 >> 2
#     print(f'Побитовый сдвиг вправо числа 5 на 2 знака: {a} ({bin(a)})')
#     return
