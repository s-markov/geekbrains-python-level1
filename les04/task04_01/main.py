# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

import sys

from les04.task04_01 import my_mod

try:
    file, user, worked_time, hourly_rate, bonus = sys.argv
except ValueError:
    print("Invalid args")
    exit()

print(f"{user}, зарплата составляет {my_mod.calculate(float(worked_time), float(hourly_rate), float(bonus))} рублей")
