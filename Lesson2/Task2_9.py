# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
def sum_num(a):
    if len(a) == 1:
        return int(a)
    else:
        return int(sum_num(a[:-1])) + int(a[-1])


max_sum = 0
num = 0
while True:
    b = input('Введите число: ')
    if int(b) == 0:
        print(f'наибольшее по сумме число - {num}.\nСумма чисел = {max_sum}')
        break
    c = sum_num(b)
    if c > max_sum:
        max_sum = c
        num = b
