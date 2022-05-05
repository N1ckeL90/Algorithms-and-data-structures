# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
def sum_numbers(n):
    if n == 0:
        return n
    else:
        return sum_numbers(n-1) * -0.5 + 1


nn = int(input('Введите количество элементов: '))
print(sum_numbers(nn))
# list_of_num = [1]
# result = 0
#
# for i in range(1, nn):
#     list_of_num.append(list_of_num[i-1] * -0.5)
# for i in range(0, len(list_of_num)):
#     result += list_of_num[i]
# print(result)
