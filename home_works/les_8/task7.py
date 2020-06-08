"""Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
 Проверьте корректность полученного результата.
"""


class ComplexNumber:
    # Суммой двух комплексных чисел z1=a1+b1i и z2=a2+b2i называется комплексное число z, которое равно
    # z=(a1+a2)+(b1+b2)i
    complex_num = []
    a = 0
    b = 0

    def __init__(self, a1, b1):
        self.a1 = a1
        self.b1 = b1
        self.complex_num *= 0

    def __add__(self, other):

        a = self.a1 + other.a1
        b = self.b1 + other.b1

        self.complex_num.append(a)
        self.complex_num.append(b)
        return self.complex_num

    def __mul__(self, other):
        # Произведением двух комплексных чисел z1=a1+b1i и z2=a2+b2iz2=a2+b2i называется комплексное число z, равное
        # z=z1⋅z2=(a1a2−b1b2)+(a1b2+b1a2)i
        a = (self.a1 * other.a1 - self.b1 * other.b1)
        b = (self.a1 * other.b1 + self.b1 * other.a1)

        self.complex_num *= 0
        self.complex_num.append(a)
        self.complex_num.append(b)

        return self.complex_num

    def __str__(self):
        if self.complex_num:
            result = ''
            for _ in self.complex_num:
                result += _
            return result

        else:
            return str(self.a1) + ',' + str(self.b1) + 'i'


if __name__ == '__main__':
    cn = ComplexNumber(3, 5)
    cn2 = ComplexNumber(4, 2)
    print(cn + cn2)
    print(cn * cn2)
