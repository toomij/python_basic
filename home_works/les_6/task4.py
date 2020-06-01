"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    name = 0
    is_police = None

    def go(self):
        print('Go')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        if direction:
            print(f'Turn {direction}')
        else:
            print('Enter direction')

    def show_speed(self):
        print(f'Speed is {str(self.speed)}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Your speed is very high: {str(self.speed)}')
        else:
            print(f'Your current speed is: {str(self.speed)}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Your speed is very high: {str(self.speed)}')
        else:
            print(f'Your current speed is: {str(self.speed)}')


class PoliceCar(Car):
    pass

car = Car()

car.go()
car.stop()
car.turn('left')
car.speed = 60
car.show_speed()

town_c = TownCar()
town_c.speed = 70
town_c.show_speed()

w_car = WorkCar()
w_car.speed = 50
w_car.show_speed()