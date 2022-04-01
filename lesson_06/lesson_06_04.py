# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

from time import sleep


class Car:
    # атрибуты класса
    def __init__(self, name, color, speed, direction='D', is_police: bool = False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        self.is_motion = False
        self.dir_keys = {'D': 'прямо', 'R': 'направо', 'L': 'налево'}
        self.direction = direction
        self.limit = 0

    # методы класса
    def go(self):
        if not self.is_motion:
            self.is_motion = True
            print(f'Машина {self.name} поехала')
            if self.name == 'Lada' or self.name == 'Лада':
                sleep(5)
                self.is_motion = False
                print(f'Машина {self.name} сломалась!')
        else:
            print(f'Машина {self.name} уже в пути! Для остановки запустите метод stop')
        return self.is_motion

    def stop(self):
        if self.is_motion:
            self.is_motion = False
            print(f'Машина {self.name} остановлена')
        else:
            print(f'Машина {self.name} стоит! Для старта запустите метод go')
        return self.is_motion

    def direct(self):
        if self.is_motion:
            if self.direction == 'D':
                print(f'Машина {self.name} едет {self.dir_keys.get(self.direction)}')
            else:
                print(f'Машина {self.name} повернула {self.dir_keys.get(self.direction)}')
        else:
            print(f'Машина {self.name} стоит! Для старта запустите метод go')

    def turn(self, direction):
        self.direction = direction
        self.direct()
        return self.direction

    def show_speed(self):
        if self.is_motion:
            print(f'Скорость {self.name} = {self.speed} км/ч')
        else:
            print(f'Машина {self.name} стоит! Для старта запустите метод go')


class TownCar(Car):
    # атрибуты класса
    def __init__(self, name, color, speed, direction='D', is_police: bool = False):
        super().__init__(name, color, speed, direction, is_police)
        self.limit = 60

    # методы класса
    def show_speed(self):
        super().show_speed()
        if self.limit + 30 > self.speed > self.limit:
            print(f'Скорость {self.name} превышает {self.limit} км/ч!\nВам вынесено предупреждение!')
        elif self.speed > self.limit + 30:
            self.is_police = True
            print(f'Скорость {self.name} превышает {self.limit + 30} км/ч!\nВам выписан штраф!')
        return self.is_police


class WorkCar(TownCar):
    # атрибуты класса
    def __init__(self, name, color, speed, direction='D', is_police: bool = False):
        super().__init__(name, color, speed, direction, is_police)
        self.limit = 40

    # методы класса
    def show_speed(self):
        super().show_speed()


a = Car('Toyota', 'red', 90)
a.go()
a.direct()
a.stop()
a.show_speed()
print()
b = Car('BMW', 'black', 80, 'L')
b.go()
b.direct()
b.show_speed()
print()

c = TownCar('Lada', 'green', 60, 'R')
c.go()
c.direct()
c.show_speed()
print()
d = TownCar('Porsche', 'blue', 95)
d.go()
d.direct()
d.show_speed()
print()

e = WorkCar('Mini', 'yellow', 72)
e.go()
e.direct()
e.show_speed()
print()
f = WorkCar('Mitsubishi', 'pink', 40, 'R')
f.go()
f.direct()
f.turn('L')
f.show_speed()

# print('автопарк:')
# for car in [Car('Toyota', 'red', 90), Car('BMW', 'black', 80, 'L'),
#             TownCar('Lada', 'green', 60, 'R'), TownCar('Porsche', 'blue', 95),
#             WorkCar('Mini', 'yellow', 72), WorkCar('Mitsubishi', 'pink', 40, 'R')]:
#     print(car.name, car.color, car.speed, 'едет', car.dir_keys.get(car.direction))
#     car.go()
#     car.direct()
#     car.turn('L')
#     car.turn('R')
#     car.direct()
#     car.show_speed()
#     car.stop()
