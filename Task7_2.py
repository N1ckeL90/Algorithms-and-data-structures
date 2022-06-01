# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50]. Выведите на экран исходный и отсортированный
# массивы.
from random import uniform
from cProfile import run


def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])
    n = m = k = 0
    c = [0] * (len(left) + len(right))
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            c[k] = left[n]
            n += 1
        else:
            c[k] = right[m]
            m += 1
        k += 1
    while n < len(left):
        c[k] = left[n]
        n += 1
        k += 1
    while m < len(right):
        c[k] = right[m]
        m += 1
        k += 1
    for i in range(len(arr)):
        arr[i] = c[i]
    return arr


if __name__ == '__main__':
    a = []
    for x in range(50):
        a.append(uniform(0, 50))
    print(a)
    run('merge_sort(a)')
    print(merge_sort(a))
    # Временная сложность  - O(nlogn)
    # Пространственная сложность O(n)
