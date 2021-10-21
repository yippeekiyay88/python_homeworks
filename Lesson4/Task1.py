# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys import argv

if len(sys.argv) < 4:
    print(f"Enter data(output in hours, rate per hour and bonus)")
else:
    output_in_hours = float(sys.argv[1])
    rate_per_hour = float(sys.argv[2])
    bonus = float(sys.argv[3])
    salary = output_in_hours * rate_per_hour + bonus
    print(salary)


