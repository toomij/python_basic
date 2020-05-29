import random

class Homo:
    _height = 0.3
    _weight = 3.2
    __age = 0

    def __init__(self, sex, hair_color):
        self.sex = sex
        self.hair_color = hair_color

    def say(self):
        print(f'sdsdsdsdf {self.hair_color}')


class Neander:

    def __init__(self, hunt):
        self.hunt = hunt

    def say(self):
        print('AAAGGGGGRRRR')


class HomoSap(Homo):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)

    def say(self):
        print(f'IM HOMOSAPIENS. My name is {self.name}')


class SapSap(HomoSap, Neander):
    def __init__(self, body_color, hunt, *args, **kwargs):
        self.bodycolor = body_color
        super().__init__(*args, **kwargs)
        Neander.__init__(self, hunt)


adam = SapSap('white', True, 'Igor', 'm', hair_color='red')
print(1)
adam.say()
