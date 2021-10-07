# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Enter proceed: "))
outlay = int(input("Enter outlay: "))
if  proceeds > outlay:
    profitability = proceeds - outlay
    rent = profitability / proceeds
    print(f"Perfect!!! You have {profitability} profitability")
    employee = int(input("Quantity of employees: "))
    print(f"{profitability / employee} for employee")
if  proceeds < outlay:
    print(f"Bad new!!! You haven't profitability")
elif proceeds == outlay:
    print("Proceeds are equal the outlay")
else:
    print('Procceds calculated')

