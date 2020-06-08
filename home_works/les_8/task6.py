"""Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class ListTypeExeption(Exception):
    def __init__(self, data):
        self.data = data
        if type(self.data) is not type(int):
            return None


class OfficeEq:
    def __init__(self, l=None, w=None, price=None):
        self.l = l
        self.w = w
        self.price = price
        self.depart = None

    def belong(self):
        return self.depart


class printer(OfficeEq):
    def __init__(self, cartrigetype=None, **kwargs):
        super().__init__(**kwargs)

        self.cartrigetype = cartrigetype


class scanner(OfficeEq):
    def __init__(self, scan_size='A4', **kwargs):
        super().__init__(**kwargs)

        self.scan_size = scan_size


class xerox(OfficeEq):
    def __init__(self, speed=5, **kwargs):
        super().__init__(**kwargs)

        self.speed = speed


class OfficeEqWarehouse:
    place = {}

    def __init__(self, width, length, height, num_cells):
        self.width = width
        self.lenght = length
        self.height = height
        if type(int(num_cells)) is int:
            self.num_cells = num_cells
        else:
            raise ListTypeExeption(num_cells)


    def store(self, equipment=None):
        self.place[self.num_cells] = equipment
        self.num_cells -= 1
        return self


    def brought(self, equipment=None, department=None):
        self.place.pop(*[k for k, v in self.place.items() if v == equipment])
        self.num_cells += 1

        equipment.depart = department
        return self


if __name__ == '__main__':
    pr = printer(cartrigetype='one', w=100, l=120, price=12500)

    sc = scanner(scan_size='A5', w=220, l=20, price=20000)

    xr = xerox(speed=6, w=156, l=123, price=10000)

    wh = OfficeEqWarehouse(1000, 2000, 30, 20)

    wh.store(pr)

    print(wh.place)

    wh.brought(pr, 'IT')

print(wh.place)
print(pr.depart)

print(1)
