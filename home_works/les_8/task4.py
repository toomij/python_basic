"""Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class OfficeEqWarehouse:

    def __init__(self, width, length, height, num_cells):
        self.width = width
        self.lenght = length
        self.height = height
        self.num_cells = num_cells


class OfficeEq:
    def __init__(self, l=None, w=None, price=None):
        self.l = l
        self.w = w
        self.price = price



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


pr = printer(cartrigetype='one', w=100, l=120, price=12500)

sc = scanner(scan_size='A5', w=220, l=20, price=20000)

xr = xerox(speed=6, w=156, l=123, price=10000)

print(1)
