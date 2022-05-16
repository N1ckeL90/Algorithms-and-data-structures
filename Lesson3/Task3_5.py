# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.
from random import randint


random_array = []
for i in range(100):
    x = randint(-100, 100)
    while x in random_array:
        x = randint(-100, 100)
    random_array.append(x)
print(random_array)

min_val = 0
min_ind = 0
for i in range(len(random_array)):
    if random_array[i] < min_val:
        min_val = random_array[i]
        min_ind = i
print(f'Минимальное число {min_val} с индексом {min_ind}')
