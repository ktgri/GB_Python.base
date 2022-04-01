# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта
# для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

file_name, arg_01, arg_02, arg_03 = argv


def salary_calculation(productivity, per_hour, premium):
    """ Возвращает расчёт заработной платы сотрудника

    :param productivity: выработка сотрудника в часах
    :param per_hour: ставка в час
    :param premium: премия
    :return: productivity * per_hour + premium
    """
    return float(productivity) * float(per_hour) + float(premium)


print(f'Заработная плата сотрудника = {salary_calculation(arg_01, arg_02, arg_03)}')
