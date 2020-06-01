"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
 и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
 Важно, чтобы для каждого предмета не обязательно были все типы занятий.
 Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
import re

db = {}
tasks = []
number_tasks = []

with open('task6.txt', 'r', encoding='UTF-8' ) as f:
    data = f.readlines()

for data_el in data:

    numbers_task = re.findall('\d+', data_el)
    task = re.findall('^\w+', data_el)
    if len(numbers_task) >= 2:
        int_i = 0
        sum_int = 0
        for i in numbers_task:
            int_i = int(i)
            sum_int += int_i
        str_list = str(task)
        db[str_list] = sum_int
    else:
        str_list = str(task)
        db[str_list] = number_tasks
    # db.update(task, numbers_task)
    #tasks.append(task)
    # str_list = str(task)
    # db[str_list] = number_tasks

print(db)