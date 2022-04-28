# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    # атрибуты класса
    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    # атрибуты класса
    def __init__(self, name, surname, position, wage=0, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    # методы класса
    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Уровень дохода: {sum(self._income.values())}'

    def get_position(self):
        return f'Позиция: {self.position}'


Ivan = Worker('Ivan', 'Andreev', 'lead')
print(Ivan.surname)

Igor = Position('Igor', 'Ivanov', 'lead', 200, 35)
print(Igor.get_full_name())
print(Igor.get_total_income())

Masha = Position('Маша', 'Гром', 'директор', 300)
print(Masha.get_full_name())
print(Masha.get_total_income())
print(Masha.get_position())
