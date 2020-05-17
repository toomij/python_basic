# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


expanses_str = input("Enter company's losses\n")
income_str = input("Enter company's profit\n")

if expanses_str.isdigit():
    expanses = int(expanses_str)
if income_str.isdigit():
    income = int(income_str)

if int(income) > int(expanses):
    print('Your company are profitable')
    print('Your profitability is {:.3f}'.format(expanses/income))
    employees = input('Enter number of employees\n')
    print('Your profit per employee is {:.3f}'.format(income/int(employees)))
else:
    print('Your company are unprofitable')

