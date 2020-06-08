"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


# Не смог получить помощь в задании, в итоге много плагиата

class MatrixError(Exception):
    """ An exception class for Matrix """
    pass


class SomeIter:

    def __init__(self, data):
        self.__data = data
        self.i = 0
        self.j = 0

    def __next__(self):
        self.__unzip_lst = zip(*self.__data)
        for self.i in self.__unzip_lst:
            for self.j in self.i:
                return self.j
        raise StopIteration


class Matrix:
    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0] * n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __repr__(self):
        s = str(self.rows)
        rank = str(self.getRank())
        rep = "Matrix: \"%s\", rank: \"%s\"" % (s, rank)
        return rep

    def __iter__(self):
        return SomeIter(self.m)

    def __add__(self, mat):
        """ Add a matrix to this matrix and
        return the new matrix. Doesn't modify
        the current matrix """

        if self.getRank() != mat.getRank():
            raise MatrixError("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __sub__(self, mat):
        """ Subtract a matrix from this matrix and
        return the new matrix. Doesn't modify
        the current matrix """

        if self.getRank() != mat.getRank():
            raise MatrixError("Trying to add matrixes of varying rank!")

        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [item[0] - item[1] for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def getRank(self):
        return (self.m, self.n)

    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        # Validity check
        if any([len(row) != n for row in rows[1:]]):
            raise MatrixError("inconsistent row length")
        mat = Matrix(m, n, init=False)
        mat.rows = rows

        return mat

    @classmethod
    def fromList(cls, listoflists):
        """ Create a matrix by directly passing a list
        of lists """

        # E.g: Matrix.fromList([[1 2 3], [4,5,6], [7,8,9]])

        rows = listoflists[:]
        return cls._makeMatrix(rows)

    @property
    def matrix(self):
        return self.matrix


if __name__ == '__main__':
    m1 = Matrix.fromList([[31, 22], [2, 4], [5, 6]])
    m2 = Matrix.fromList([[3, 4], [5, 4], [65, 65]])

    m3 = m1 + m2
    print(m3)