# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
from collections import Counter
import cProfile


def cnt_profit():
    num_of_enterprises = int(input('Введите количество предприятий: '))
    n = 1
    enterprise_profit = {}  # словарь предприятий и их прибыль
    while n <= num_of_enterprises:  # Сбор данных
        name = input('Введите название предприятия: ')
        quarter1 = float(input('Введите прибыль за 1 квартал: '))
        quarter2 = float(input('Введите прибыль за 2 квартал: '))
        quarter3 = float(input('Введите прибыль за 3 квартал: '))
        quarter4 = float(input('Введите прибыль за 4 квартал: '))
        enterprise_profit[n] = [name, quarter1, quarter2, quarter3, quarter4]
        n += 1
    # подсчет средней прибыли за год
    total_avr_profit = 0  # общая средняя прибыль
    for i in range(1, num_of_enterprises + 1):  # расчет средней прибыли по предприятиям
        avr_profit = 0
        for k in range(1, 5):
            avr_profit += enterprise_profit[i][k]
        avr_profit = avr_profit / 4  # средняя прибыль предприятия за год
        enterprise_profit[i] = (enterprise_profit[i][0], avr_profit)  # заменям прибыль по кварталам на среднюю за год
        total_avr_profit += avr_profit
    total_avr_profit = total_avr_profit / num_of_enterprises  # общая средняя прибыль
    above_avr = []  # список предприятий с доходом выше среднего
    below_avr = []  # список предприятий с доходом ниже среднего
    for i in range(1, num_of_enterprises + 1):
        if enterprise_profit[i][1] > total_avr_profit:
            above_avr.append(enterprise_profit[i][0])
        else:
            below_avr.append(enterprise_profit[i][0])
    print('Общая средняя прибыль предприятий за год = ', total_avr_profit)
    print('предприятия с доходом выше среднего - ', ", ".join(above_avr))
    print('предприятия с доходом ниже среднего - ', ", ".join(below_avr))


cProfile.run("cnt_profit()")
# сложность алгоритма примерно O(n)
