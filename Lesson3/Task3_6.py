# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.

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
print([min_ind, min_val], [max_ind, max_val])
#находим сумму
sum_num = 0
if min_ind < max_ind:
    sum_num = sum(random_array[min_ind + 1: max_ind])
else:
    sum_num = sum(random_array[max_ind + 1: min_ind])
print(sum_num)
