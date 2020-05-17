# First day
a_str = input('Введите расстояние в 1-й день\n')

if a_str.isdigit():
    a = float(a_str)
else:
    print('Вы не ввели число')
    exit(0)
# Second day

b_str = input('Введите целевое расстояние\n')

if b_str.isdigit():
    b = float(b_str)
else:
    print('Вы не ввели число\n')
    exit(0)

delta = 0.1

x_day = 1

print('1-й день: {}'.format(a))

while a <= b:
    x_day += 1
    a = a + (a * delta)
    print('{}-й день: {:.2f}'.format(x_day, a))

print('на {}-й день спортсмен достиг результата -- не менее {:.0f} км'.format(x_day, a))