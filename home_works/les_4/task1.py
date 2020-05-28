"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

import sys


def salary(hours, rate, kpi):
    if hours.isdigit() and rate.isdigit() and kpi.isdigit():
        return int(hours) * int(rate) + int(kpi)
    else:
        print("Введите чиловые значения")


print(salary(sys.argv[1], sys.argv[2], sys.argv[3]))
