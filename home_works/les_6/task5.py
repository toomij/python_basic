"""Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ''

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()