"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyOwnEx(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


inp = input('Введите делитель: ')
if inp.isdigit():
    inp_in = int(inp)

if not inp_in:
    raise MyOwnEx('Devide by zero')
