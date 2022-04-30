# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
import random


sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
# Случайное целое число
a = int(input('Введите начальную границу (целое число): '))
b = int(input('Введите конечную границу (целое число): '))
result = random.randint(a, b)
print(result)
# Случайное вещественное число
a = float(input('Введите начальную границу (вещественное число): '))
b = float(input('Введите конечную границу (вещественное число): '))
result = random.uniform(a, b)
print(f'{result:.02f}')
# Случайный символ
a = input('Введите начальную границу (символ): ')
b = input('Введите конечную границу (символ): ')
a_index = sequence.index(a)
b_index = sequence.index(b)
result = random.randint(a_index, b_index)
print(sequence[result])
