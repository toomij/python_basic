"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""



with open('task4.txt', 'r', encoding='UTF-8') as f:
    data = f.readlines()

for el in data:
    word, number = el.split('—')
    if int(number) == 1:

            out_str = 'Один -' + number

    if int(number) == 2:

            out_str += 'Два -' + number

    if int(number) == 3:

            out_str += 'Три -' + number

    if int(number) == 4:

            out_str += 'Четыре -' + number

with open('task4_out.txt', 'w', encoding='UTF-8') as out:
    out.writelines(out_str)