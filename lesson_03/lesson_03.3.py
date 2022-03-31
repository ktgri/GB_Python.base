# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.


def my_func():
    """ Возвращает сумму наибольших двух аргументов из трех

    """
    num1, num2, num3 = map(int, input(f"Введите три числа через запятую: ").split(','))
    if num2 >= num1 <= num3:
        return num2 + num3
    elif num1 >= num2 <= num3:
        return num1 + num3
    else:
        return num1 + num2


print(my_func())
