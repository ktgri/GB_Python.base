# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = 'канцелярская принадлежность'
    ending = ['ой', 'ю', 'ом']

    # методы класса
    def draw(self):
        words = self.title.split(' ')
        print(f'Запуск отрисовки {words[0][:-2]}{self.ending[0]} {words[1]}{self.ending[1]}')


class Pen(Stationery):
    title = 'ручка'

    # методы класса
    def draw(self):
        print(f'Запуск отрисовки {self.title[:-1]}{self.ending[0]}')


class Pencil(Stationery):
    title = 'карандаш'

    # методы класса
    def draw(self):
        print(f'Запуск отрисовки {self.title}{self.ending[2]}')


class Handle(Pencil):
    title = 'маркер'


s = Stationery()
s.draw()

p1 = Pen()
p1.draw()

p2 = Pencil()
p2.draw()

h = Handle()
h.draw()
