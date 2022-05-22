# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в
# рамках практического задания первых трех уроков.
import cProfile


# Функция подсчета четных и нечетных цифр введенного натурального числа
def count_even_odd(num):
    i = 0
    even = 0
    odd = 0
    for i in range(len(num)):
        if int(num[i]) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'В числе - {even} четных и {odd} нечетных чисел')


if __name__ == "__main__":
    a = input('Введите число: ')
    cProfile.run('count_even_odd(a)')
# Сложность алгоритма примерно - O(1), т.е. алгоритм не нуждается в оптимизации

# py -m timeit -n 100 -s "import Task4_1" "Task4_1.count_even_odd('123456789')"
# 100 loops, best of 5: 76.6 usec per loop
