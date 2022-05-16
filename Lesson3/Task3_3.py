# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint


#Создаем список натуральных числел из 10 значений
random_array = []
for i in range(10):
    x = randint(0, 100)
    while x in random_array:
        x = randint(0, 100)
    random_array.append(x)
print(random_array)
#находим индексы и значения максимального и минимального числа
max_val = 0
min_val = random_array[0]
min_ind = 0
max_ind = 0
for i in range(len(random_array)):
    if random_array[i] > max_val:
        max_ind = i
        max_val = random_array[i]
    if random_array[i] < min_val:
        min_ind = i
        min_val = random_array[i]
# смена максимального и минимального чисел
random_array[max_ind] = min_val
random_array[min_ind] = max_val
print(random_array)
