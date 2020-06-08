# magic methods


# Абстрактные классы
# Для создания публичного класса

from abc import ABC, abstractclassmethod


class MyAbstract(ABC):

    @abstractclassmethod
    def some_method(self, a: int, b: str) -> str:
        pass

    @abstractclassmethod
    def some_method2(self, a: int, b: str) -> str:
        pass


class SomeCls(MyAbstract):
    def __init__(self):
        self.a = 1
        self.b = 2

    def some_method(self, a: int, b: str) -> str:
        return str(a) + b

    def some_method2(self, a: int, b: str) -> str:
        return str(a) + b


class SomeIter:
    def __init__(self, data):
        self.__data = data
        self.i = 0

    def __next__(self):
        if self.i < len(self.__data):
            self.i += 2
            return self.__data[self.i - 2]
        raise StopIteration


class MyCollection:
    def __init__(self, *args):
        self.__box = list(args)

    def __add__(self, other):
        result = map(sum, zip(self, other))
        return MyCollection(*result)

    def __bool__(self):
        return True if len(self.__box) & 1 else False

    def __str__(self) -> str:
        return str(self.__box)

    def __getitem__(self, item):
        return self.__box[item]

    def __call__(self, x, y):
        return sum((self[0], x, y))

    def __iter__(self):
        return SomeIter(self.__box)

    @property
    def box(self):
        return tuple(self.__box)

    @box.setter
    def box(self, item):
        print('Я не изменил я добавил')
        self.__box.append(item)


def my_deco(func):
    def some(*args, **kwargs):
        print(f'Вызвана функция {func.__name__}')
        result = func(*args, **kwargs)
        print(f'функция {func.__name__} звершила работу')
        return result

    return some


@my_deco
def my_some(a, b):
    return a + b


if __name__ == '__main__':
    a = MyCollection(1, 2, 3, 4)
    print(1)
