# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
# число представляется как коллекция, элементы которой это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque
from cProfile import run

# словарь для перевода из шестнадцатиричной системы в десятичную и обратно
HEX_CONVERT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


# Проверка и подготовка данных перед вычислением
def check_input_data(a, b):
    # проверяем длину очередей и при необходимости выравниваем их путем добавления перед ними нулей
    if len(a) > len(b):
        tmp = len(a) - len(b)
        b.extendleft(['0'] * tmp)
    if len(a) < len(b):
        tmp = len(b) - len(a)
        a.extendleft(['0'] * tmp)
    # Разворачиваем очередь для удобства при дальнейшем вычислении
    a.reverse()
    b.reverse()
    return a, b


# Сумма hex чисел
def sum_hex(a, b):
    a, b = check_input_data(a, b)  # Проверка и подготовка данных перед вычислением
    result = deque()
    tmp = 0  # Временная переменная
    for i in range(len(a)):  # Расчет суммы
        sum_tmp = HEX_CONVERT.get(a[i]) + HEX_CONVERT.get(b[i]) + tmp
        if sum_tmp > 15:
            sum_tmp = sum_tmp - 16
            result.appendleft(HEX_CONVERT.get(sum_tmp))
            tmp = 1
        else:
            tmp = 0
            result.appendleft(HEX_CONVERT.get(sum_tmp))
        if i == len(a) - 1 and tmp == 1:  # Проверка суммы на последней итерации
            result.appendleft('1')
    return list(result)


def mul_hex(a, b):
    a, b = check_input_data(a, b)  # Проверка и подготовка данных перед вычислением
    result = deque()
    tmp_deq1 = deque()  # Временая переменная
    tmp_deq2 = deque()  # Временая переменная
    for i in range(len(a)):
        tmp = 0  # Временная переменная
        for j in range(len(b)):  # Расчет произведения чисел
            mul_tmp = HEX_CONVERT.get(a[j]) * HEX_CONVERT.get(b[i]) + tmp
            tmp_deq1.appendleft(HEX_CONVERT.get(mul_tmp % 16))  # Запоминаем промежуточный результат
            tmp = mul_tmp // 16
            if j == len(b) - 1 and tmp > 0:  # Проверка последней итерации
                tmp_deq1.appendleft(HEX_CONVERT.get(tmp % 16))
        if i > 0:
            tmp_deq1.extend(['0'] * i)  # Добавляем нули после частичного перемножения, чтобы потом сложить
            tmp_deq2.extend(sum_hex(tmp_deq1, result))
            result.clear()
            result.extend(list(tmp_deq2))
            tmp_deq2.clear()
        if i == 0:
            result.extend(list(tmp_deq1))
        tmp_deq1.clear()
    return list(result)


# Функция сложения и умножения hex чисел
def hex_arithmetic(a, b, sign='+'):
    a = deque(a.upper())
    b = deque(b.upper())
    result = []
    if sign == '+':
        result = sum_hex(a, b)
    if sign == '*':
        result = mul_hex(a, b)
    return result


run("hex_arithmetic('A2', 'C4F')")
run("hex_arithmetic('A2', 'C4F', '*')")
print(hex_arithmetic('A2', 'C4F'))
print(hex_arithmetic('A2', 'C4F', '*'))

# Временная сложность алгоритма при суммировании - примерно O(n), при умножении  - примерно O(n**2)
