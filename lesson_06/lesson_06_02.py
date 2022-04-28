# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина *
# масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    # атрибуты класса
    def __init__(self, length, width, density=25, depth=5):
        self._length = length
        self._width = width
        self.density = density
        self.depth = depth

    # методы класса
    def area(self):
        return self._length * self._width

    def weight(self):
        return self.area() * self.density * self.depth


r = Road
print(r(10, 3, 5, 4).area())
print(r(10, 3, 5, 4).weight())
print(r(10, 3).weight())
