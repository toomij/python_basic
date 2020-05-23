"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""

var_list_str = input('Введите элементы списка: ')
if var_list_str.isdigit():
    var_list = list(var_list_str)
else:
    print('Вы вели не цифры')
if len(var_list) % 2:
    var_list.append(None)
var_list[1::2], var_list[::2] = var_list[::2], var_list[1::2]
var_list.remove(None)
print(var_list)
