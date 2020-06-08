"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

args = []
num1 = input('Введите первое число для деления: ')
if num1.isdigit():
    args.append(int(num1))
num2 = input('Введите второе число для деления: ')
if num2.isdigit():
    args.append(int(num2))


def my_div(*args):
    """Функция деления"""
    args = args
    result = 0
    try:
        result = args[0] / args[1]
    except ZeroDivisionError as e:
        print("Деление на ноль", e)

    return result


print(my_div(*args))
