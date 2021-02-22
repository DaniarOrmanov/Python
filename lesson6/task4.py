# 4. Реализуйте базовый класс Car. У данного класса
# должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40
# (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=0):
        self.speed = speed
        self.color = color
        self.name = name
        if is_police == 1:
            self.is_police = 'Это полицейская машина.'
        else:
            self.is_police = 'Это гражданская машина.'

    def go(self):
        print(f'Авто {self.name} поехал.')

    def stop(self):
        print(f'Авто {self.name} остановился.')

    def turn(self, direction):
        self.direction = direction
        print(f'Авто {self.name} повернул {self.direction}.')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч.')


class TownCar(Car):

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч.')
        if self.speed > 60:
            print('Внимание, превышение допустивой скорости в 60 км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч.')
        if self.speed > 40:
            print('Внимание, превышение допустивой скорости в 40 км/ч!')


class PoliceCar(Car):
    pass


print('')
vw = TownCar(80, 'red', 'Volkswagen')
vw.show_speed()
vw.go()
vw.turn('налево')
vw.stop()
print('')
nissan = WorkCar(40, 'yellow', 'Nissan')
nissan.show_speed()
nissan.go()
nissan.turn('направо')
print(nissan.is_police)
print('')
police = PoliceCar(100, 'Black', 'Ford', 1)
police.show_speed()
print(police.is_police)
print('')
pe = SportCar(300, 'Blue', 'Porsche')
pe.show_speed()
pe.go()
pe.turn('налево')
pe.stop()
print(pe.is_police)