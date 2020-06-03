"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
 Определить, кто из сотрудников имеет оклад менее 20 тыс.,
 вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников."""

with open('task3.txt', 'rt', encoding='UTF-8') as f:
    data = f.read()

words = data.split()
db = dict(zip(words[::2], words[1::2]))

for name, salary in db.items():
    if int(salary) < 20000:
        print(name)

salary = 0
for name, salary in db.items():
    salary_int = int(salary)
    salary_int += salary_int

av_salary = int(salary_int)/len(db)
print('Средняя ЗП = ' + str(av_salary))
