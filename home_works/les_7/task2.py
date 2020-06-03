"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).

Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import abstractmethod


class Clothes:
    def __init__(self, name, s):
        self._name = name
        self.s = s

    @abstractmethod
    def tissue_con(self) -> float:
        pass

    def __add__(self, other):
        return self.tissue_con() + other.tissue_con()

    @property
    def size(self):
        return self.tissue_con()

class Сoat(Clothes):

    def tissue_con(self) -> float:
        return float(self.s / 6.5 + 0.5)


class Suit(Clothes):

    def tissue_con(self) -> float:
        return float(2 * self.s + 0.3)


if __name__ == '__main__':
    palto = Сoat('пальто', 65)
    kostum = Suit('костюм', 10)

    print(palto.size)
    print(kostum.size)

    print(kostum + palto)
