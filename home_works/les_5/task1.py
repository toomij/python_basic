"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def put_file():
    with open('task1.txt', 'w', encoding='UTF-8') as f:
        my_string = input('text: ')
        while my_string:
            f.writelines(my_string + '\n')
            my_string = input('text: ')


if __name__ == '__main__':
    put_file()
