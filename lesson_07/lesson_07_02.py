# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом
# проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter
        pass

    @property
    @abstractmethod
    def expense(self):
        pass

    def __add__(self, other):
        return self.expense + other.expense


class Coat(Clothes):
    @property
    def expense(self):
        return round(self.parameter / 6.5 + 0.5, 3)


class Suit(Clothes):
    @property
    def expense(self):
        return round(self.parameter * 2 + 0.3, 3)


c = Coat(42)
print(c.expense)

s = Suit(1.65)
print(s.expense)

print(c + s)
