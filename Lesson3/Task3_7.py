# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.
from random import randint


#Создаем список натуральных числел из 20 значений
random_array = []
for i in range(20):
    x = randint(0, 100)
    random_array.append(x)
print(random_array)
#поиск 2x наименьших чисел
min_val1 = min_val2 = random_array[0]
tmp = 0
for i in range(len(random_array)):
    if random_array[i] < min_val1:
        min_val1 = random_array[i]
        if min_val1 < min_val2:
            tmp = min_val1
            min_val1 = min_val2
            min_val2 = tmp

print(f'Минимальные числа в массиве - {min_val1} и {min_val2}')
