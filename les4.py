import sys
from my_module import r_sum

print(sys.argv)

_, *vars = sys.argv

# сжатый цикл работает быстрее

tmp = [int(itm) for itm in vars if itm.isdigit()]

print(r_sum([int(itm) for itm in vars if itm.isdigit()]))


def my_f(n):
    tmp = 0
    while tmp != n:
        yield tmp ** 2
        tmp += 1

for itm in my_f(2):
    print(itm)


