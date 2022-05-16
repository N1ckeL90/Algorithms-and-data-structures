# 4.Определить, какое число в массиве встречается чаще всего
from random import randint


#Создаем список натуральных числел из 10 значений
random_array = []
for i in range(10):
    x = randint(0, 10)
    random_array.append(x)
print(random_array)
# поиск числа
print(max(set(random_array), key=lambda z: random_array.count(z)))
