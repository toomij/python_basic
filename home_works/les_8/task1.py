"""1. Реализовать класс «Дата», функция-конструктор
которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:

    def __init__(self, date: str):
        self.date = date
    #
    # def __str__(self):
    #     return list(self.date)

    @classmethod
    def to_num(cls, date):
        num_date = [[x for x in map(int, date.split('-'))]]
        cls.valid_date(*num_date)
        return cls(*num_date)

    @staticmethod
    def valid_date(date):
        day, month, year = date
        if 1 < day >= 31:
            raise OwnError('Wrong day')
        if 1 < month >= 12:
            raise OwnError('Wrong month')
        if 0 < year >= 9999:
            raise OwnError('Wrong year')


if __name__ == '__main__':
    dt = Date.to_num('1-6-2020')
    print(dt.date)
