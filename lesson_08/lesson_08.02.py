# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.


class ZeroError(Exception):
    def __int__(self, message):
        self.mess = message


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

try:
    if not b:
        raise ZeroError('Вы пытаетесь разделить на ноль!')
    c = a / b
except ZeroError as error:
    c = 0
    print(error)
finally:
    print(f'{a} / {b} = {c:.2f}')
