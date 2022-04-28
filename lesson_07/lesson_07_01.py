# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, lines=[]):
        self.lines = lines
        self.strings = len(lines)
        self.columns = len(lines[0])

    def __str__(self):
        return '\n'.join(' '.join([str(i) for i in el]) for el in self.lines)

    def __eq__(self, other):
        if self.strings == other.strings and self.columns == other.columns:
            return True
        else:
            return False

    def __add__(self, other):
        if self != other:
            return 'Для сложения мартрицы должны быть одинакового размера! Aij = Bij.'
        else:
            sum_matrix = [[a + b for a, b in zip(mA, mB)] for mA, mB in zip(self.lines, other.lines)]
            return sum_matrix


A = Matrix([[31, 32], [37, 43], [37, 43]])
B = Matrix([[30, 3], [7, 3], [5, 2]])
# print(A == B)
C = A + B
print(C)

D = Matrix([[31, 32], [37, 43], [37, 43]])
E = Matrix([[30, 3], [7, 3]])
F = D + E
print(F)
