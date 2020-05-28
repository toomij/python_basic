"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

import random as rd

data = [ rd.randint(0,10) for _ in range(12) ]

var_str = ' '.join(map(str, data))

with open('task5.txt', 'w', encoding='UTF-8') as out:
    out.write(var_str)

with open('task5.txt', 'r', encoding='UTF-8') as f:
    data_r = f.read()

number = data_r.split(' ')

sum_num = 0
for i in number:
    int_i = int(i)
    sum_num += int_i

print(sum_num)
