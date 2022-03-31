# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

a, b = map(float, input(f"Введите\033[31m делимое и делитель\033[0m через разделитель '/': ").split('/'))


def division(divisible, divider):
    """ Возвращает частное от деления

    :param divisible: делимое
    :param divider: делитель
    :return: divisible / divider
    """
    while divider == 0:
        divider = float(input(f"\033[31mНа ноль делить нельзя!\033[0m\nВведите чило, отличное от нуля: "))
    return round(divisible / divider, 2)


print(division(a, b))
