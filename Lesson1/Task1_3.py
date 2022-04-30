# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
print('Введите координаты 1 точки A(x1;y1):')
x1 = float(input('x1: '))
y1 = float(input('y1: '))
print('Введите координаты 2 точки B(x2;y2):')
x2 = float(input('x2: '))
y2 = float(input('y2: '))
#находим коэффициенты k и b
k = (y1-y2)/(x1-x2)
b = y2-k*x2
if b > 0:
    print(f'y = {k:.02f}x+{b:.02f}')
elif b == 0:
    print(f'y = {k:.02f}x')
else:
    print(f'y = {k:.02f}x{b:.02f}')
