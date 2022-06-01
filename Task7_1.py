# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100]. Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции. По
# возможности доработайте алгоритм (сделайте его умнее).
from random import randint


def bubble_sorting(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n += 1
    return arr


if __name__ == '__main__':
    a = []
    for j in range(20):
        a.append(randint(-100, 100))
    print(a)
    print(bubble_sorting(a))

# Временная сложность - O(n**2)
# Пространственная сложность  - O(n)
