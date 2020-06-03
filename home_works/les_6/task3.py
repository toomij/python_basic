"""Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например,
 {"wage": wage, "bonus": bonus}.
 Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
 дохода с учетом премии (get_total_income).
 Проверить работу примера на реальных данных
 (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = 'test'
    surname = 'test'
    position = 'head'
    wage = 0
    bonus = 0
    _income = {"wage": wage, "bonus": bonus}


first = Worker()


class Poistion(Worker):
    def __init__(self, name, surname, postition, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = postition
        self.wage = wage
        self.bonus = bonus
        Worker.income = {"wage": self.wage, "bonus": self.bonus, }

    def get_fulname(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return Worker.income['wage'] + Worker.income['bonus']


one = Poistion('Ivan', 'Petrov', 'TL', 2000, 300)

print(one.get_fulname())
print(one.get_total_income())
