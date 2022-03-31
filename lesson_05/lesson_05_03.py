# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32


def data_salary(surname, salary):
    """ Из текстового файла возвращает словарь, где ключ - фамилия сотрудника,
    значение - величина заработной платы сотрудника.

    :param surname: Фамилия сотрудника
    :param salary: Заработная плата сотрудника
    :return: dict(surname: salary)
    """
    return {surname: float(salary)}


with open("salary_03.txt", 'r', encoding='utf-8') as f:
    staff = {}
    for line in f.readlines():
        staff.update(data_salary(line.split(' ')[0], line.split(' ')[1][:-1]))

print(f'Средняя заработная плата: {round(sum(staff.values()) / len(staff.values()), 2)}')

print('\nФамилии сотрудников, кто имеет оклад менее 20 тысяч:')
for employee, e_salary in staff.items():
    if e_salary < 20000:
        print(f'{employee} : {e_salary}')
