# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернёт
# строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт
# строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    def __init__(self, cells_count: int):
        self.cells_count = cells_count
        self.cells_line = 0

    def __str__(self):
        return f'Создана клетка с количеством ячеек = {self.cells_count}'

    def __add__(self, other):
        return self.cells_count + other.cells_count

    def __sub__(self, other):
        if self.cells_count >= other.cells_count:
            return self.cells_count - other.cells_count
        else:
            return f'Вычитаемая клетка должна быть меньше! {self.cells_count} - {other.cells_count} < 0!'

    def __mul__(self, other):
        return Cell(self.cells_count * other.cells_count)

    def __truediv__(self, other):
        return Cell(self.cells_count // other.cells_count)

    def __mod__(self, other):
        return self.cells_count % other.cells_count

    def __floordiv__(self, other):
        return Cell(self.cells_count / other.cells_count)

    def make_order(self, cells_line):
        self.cells_line = cells_line
        char = '*'
        return ''.join([(char * self.cells_line + '\n') for _ in range(self.cells_count // self.cells_line)])\
               + char * (self.cells_count % self.cells_line)
        # cells_chars = ''
        # for _ in range(self.cells_count // self.cells_line):
        #     cells_chars += (char * self.cells_line + '\n')
        # cells_chars += (char * (self.cells_count % self.cells_line))
        # return cells_chars


a = Cell(13)
b = Cell(4)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(b - a)

print(a.make_order(4))
