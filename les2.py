"""
Lesson 2
"""


var_str = "ЭТО СТРОКА"
var_list = [1, 2, 3, 4, ]
var_tuple = (1, 2, 3, 4, 5, 6, 7, [1, 2, 3, 4])
var_set = {1, 2, 3, 4, 'hello', 1, 2, 3, 4}
# ключ. хешируемые данные. неизменяемые типы данных
var_dict = {'KEY':12345, 'KEY2': 'HELLO'}

var_list2 = [(1, 2), (3, 4), (5, 6)]
for a, b in var_list2[::-1]:
    var_list2.append((a, b))
    print(a, b)

print(var_list2)

# нет счетчика в отличии от других языков
for itm in var_set:
    print(itm)