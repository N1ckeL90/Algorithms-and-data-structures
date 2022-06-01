# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
# в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
# одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
from random import randint
from cProfile import run


def median_search(arr):
    n = len(arr)
    while n > 1:
        arr.remove(max(arr))
        arr.remove(min(arr))
        n = len(arr)
    return arr[0]


if __name__ == '__main__':
    m = randint(1, 100)
    a = []
    for i in range(2*m+1):
        a.append(randint(0, 100))
    print(a)
    print(median_search(a))
    run('median_search(a)')
    # Временная сложность  - O(4n)
    # пространственная сложность - O(n)
