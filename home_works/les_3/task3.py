"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(*args):
    b = args
    a = list(b)
    print(type(a), a)
    num1 = max(a)
    idx = a.index(num1)
    a.pop(idx)
    num2 = max(a)
    return num1 + num2


print(my_func(1, 2, 4))
