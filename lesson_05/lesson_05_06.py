# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: training_06.txt

import re


def data_training(subject, hours):
    """ Из текстового файла возвращает словарь где ключ - учебный предмет,
    значение - сумма часов(занятий) по предмету.

    :param subject: Учебный предмет
    :param hours: сумма часов(занятий)
    :return: dict(subject: hours)
    """
    return {subject: sum(hours)}


with open("training_06.txt", 'r', encoding='utf-8') as f:
    training = {}
    for line in f.readlines():
        classes = []
        for i in re.findall(r"\d+", line):
            classes.append(int(i))
        training.update(data_training(line.split(' ')[0][:-1], classes))


for key, val in training.items():
    print(f'{key} : {val}')
