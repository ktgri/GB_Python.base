# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 'x + y * i'

    def __add__(self, other):
        print(f'Сумма чисел равна')
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Произведение чисел равно')
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.y * other.x} * i'

    def __str__(self):
        return f'z = {self.x} + {self.y} * i'


z_1 = ComplexNum(3, 5)
z_2 = ComplexNum(2, 8)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
